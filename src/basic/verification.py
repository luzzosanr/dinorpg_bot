from bs4 import BeautifulSoup

from .inventory import inventory
from ..connection.session import account
from .leveling import leveling
from .simpleActions import simpleActions
from ..path.destinations import pathFinder
from ..basic.useful import utilities

class verification:
    def checks(dinoz):
        """
            dinoz : array integer iding the dinos in party, first is leader (on element if alone)
            Checking things between actions and act on it (between moving around and fighting)
            Returns True if everything was ok, False otherwise
        """
        
        # Checking dinoz : levelup, food and death
        for id in dinoz:
            content = account().run(f"dino/{id}").content
            if verification.isDead(id, content):
                simpleActions.revive(id)
                return False
            if leveling.checkLevelUp(id, content):
                leveling.simpleLevelup(id)
                return False
            if (inventory.checkFood(id, content) >= 30):
                inventory.eat30(id)
                return False
        
        return True
        
    def isDead(dinoz, content = None):
        """
            Checking if the dinoz corresponding to the ID is dead
        """

        if not content:
            content = account().run(f"dino/{dinoz}").content

        # Return the dead indicator is there
        if BeautifulSoup(content, "html.parser").find(id = "act_resurrect"):
            return True
        
        return False
    
    def checkFood(dinoId):
        """
            dinoId : integer iding the dino in links
            return : hp missing
        """

        food = BeautifulSoup(account().run(f"dino/{dinoId}").content, "html.parser").find(class_ = "lifetext").text.split(" ")
        return int(food[2]) - int(food[0])
        
    def getPlace(dinoId):
        """
            Returns the ID of the place of the dinoz
        """

        all = BeautifulSoup(account().run().content, "html.parser").find(id = "dinozList").find_all("a")

        for dino in all:
            if dino.get_attribute_list("href")[0] == f"/dino/{dinoId}" and dino.find("em") != None:
                return pathFinder().nameToId[dino.find("em").text]

    def getItems(dinoId):
        """
            Get the list of permanent items that the dinoz have
        """

        return [i.get_attribute_list("src")[0].replace("/img/icons/", "").replace(".gif", "") for i in BeautifulSoup(account().run(f"dino/{dinoId}").content, "html.parser").find(class_ = "fx").find_all()]
        
    def hasItem(dinoIds, item, or_ = None):
        """
            dinoIds : ids of the dinoz to be verified
            item : item to be checked
            or_ : condition on dinoId replacing possessing the item
            return : True if all the dinoz have the specified item, False otherwise
        """

        for d in dinoIds:
            if not item in verification.getItems(d) and (or_ == None or not or_(d)):
                return False
        
        return True
        
    def isLeader(dinoId):
        """
            If the dino corresponding to the dinoId is the leader of a group, returns True, otherwise, returns False
        """

        a = BeautifulSoup(account().run().content, "html.parser").find(id = "dinozList").find_all("a")
        for i in a:
            if i.get_attribute_list("href")[0] == f"/dino/{dinoId}" and i.find(src = "/img/icons/small_leader.gif"):
                return True
        
        return False
        
    def teamFromLeader(leader):
        """
            leader : id of the dinoz leader of a group
            return : a list of each of all dinos in the group
        """
        

        if not verification.isLeader(leader):
            return False
        team = [leader]

        # To avoid for the selected dinoz to be on top of the list
        dinoz = utilities.getDinoz()
        if len(dinoz) > 2:
            account().run(f"dino/{dinoz[-1]}")
            account().run(f"dino/{dinoz[1]}")

        a = BeautifulSoup(account().run().content, "html.parser").find(id = "dinozList").find_all("a")
        start = False

        for i in a:
            if start:
                if i.find(src = "/img/icons/small_follow.gif"):
                    team.append(i.get_attribute_list("href")[0][6:])
                else:
                    return team
            if i.get_attribute_list("href")[0] == f"/dino/{leader}":
                start = True
                
    def getName(dinoId):
        """
            return the name of a dino from its id
        """

        return BeautifulSoup(account().run(f"dino/{dinoId}").content, "html.parser").find(class_ = "dinoz").find(class_ = "title").text