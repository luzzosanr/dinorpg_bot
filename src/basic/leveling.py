from bs4 import BeautifulSoup
from ..connection.session import account

class leveling:
    """
        Dinoz are identified by ID
    """
    
    def checkLevelUp(dino, content = None):
        """
            Returns False if the dinoz can't level up
            Set the sk code if it can (and return True)
        """

        if not content:
            content = account().run(f"dino/{dino}")
        levelUp = BeautifulSoup(content, "html.parser").find(id = "act_levelup")

        if (levelUp != None):
            account().sk = levelUp.find().get_attribute_list("onclick")[0].split('=')[-1][:-2]
            return True

        return False
    
    def simpleLevelup(dino):
        """
            Returns link to level up without taking in account() the capacity
            This method gives priority to getting a new capacity before unlocking the other ones
        """

        # Get all capacities
        menu = account().run(f"dino/{dino}/act/levelup?sk={account().getSk()}")
        capacities = BeautifulSoup(menu.content, "html.parser").find(id = "view").find_all("tr")[1:-2]

        if (capacities == []):
            # Get link to unlock new capacities
            td = BeautifulSoup(menu.content, "html.parser").find(id = "view").find_all("td")[-1]
            link = td.get_attribute_list("onclick")[0].split("'")[-2]
        else:
            # Get link to unlock the new capacity
            levels = [tr.get_attribute_list("onclick")[0].split("'")[-2] for tr in capacities]
            link = levels[0]

        account().run(link[1:])
        
    def levelup(dino, capacity):
        """
            capacity is the ID of the capacity the dinoz is going to learn while leveling up

            Learn a new capacity when leveling up
        """
        account().run(f"dino/{dino}/levelup?learn={capacity};sk={account().getSk()}")

    def getLevel(dinoId):
        """
            dinoId : integer iding the dino in links
            return (int) : level of the dino 
        """

        return int(BeautifulSoup(account().run(f"dino/{dinoId}").content, "html.parser").find(class_ = "over").text)