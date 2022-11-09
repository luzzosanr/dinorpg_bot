from bs4 import BeautifulSoup

from ..basic.useful import utilities

from ..connection.session import account
from ..basic.simpleActions import simpleActions
from ..basic.verification import verification
from ..basic.leveling import leveling

class basicStrategy:
    def newTeam(name = "points"):
        """
            Buy 3 new dinoz, name them, make them follow each other
            name : names of the dinoz of this new team
            return : id of the 3 dinoz of this new team (first one as leader)
        """
    
        def getId(content):
            lines = BeautifulSoup(content, "html.parser").find(id = "dinozList").find("ul").find_all("li")
            for l in lines:
                c = l.find(class_ = "unknown")
                if c != None and c.text == "?":
                    return l.find("a").get_attribute_list("href")[0].split("/")[-1]
        
        dinoz = ["","",""]

        for i in range(3):
            link = BeautifulSoup(account().run("shop/dinoz").content, "html.parser").find(id = "detail_0").find(class_ = "button bSmall").get_attribute_list("href")[0][1:]
            dinoz[i] = getId(account().run(link).content)
            account().session.post(f"dino/{dinoz[i]}/name", data = {"name": name})
        
        for i in range(1, 3):
            simpleActions.follow(dinoz[0], dinoz[i])
        
        return dinoz
    
    
    def oldTeam(name = "points"):
        """
            name : names of the dinoz of the team searched, only a string
            This function is used to get a leftout from zero to the end team

            Only return a team of 3 for now
        """

        for d in utilities.getDinoz():
            if verification.getName(d) == name and verification.isLeader(d):
                return verification.teamFromLeader(d)
        
        return False
        
    def partySimpleFight(dinoIds):
        """
            dinoIds : array integer iding the dinos in party, first is leader (on element if alone)
            Fight and levelup with simple choice or eat when needed (in party)
        """

        while not verification.checks(dinoIds):
            pass

        #Making dino fight
        simpleActions.fight(dinoIds[0])
        
    def goToLevel(dinoIds, level):
        """
            dinoIds : array integer iding the dinos in party, first is leader (on element if alone)
            level : level aimed
            Fight until all dinoz have the level aimed
        """

        def test():
            # Return True if all dinoz got the right level
            for id in dinoIds:
                if leveling.getLevel(id) < level:
                    return False
            return True
        
        while not test():
            basicStrategy.partySimpleFight(dinoIds)
    