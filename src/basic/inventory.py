from bs4 import BeautifulSoup
from ..connection.session import account
from .useful import utilities

class inventory:
    """
        Dinoz are represented by their IDs
    """
    def checkFood(dinoz, content = None):
        """
            Return HP missing from a dinoz
        """

        if not content:
            content = account().run(f"dino/{dinoz}").content

        food = BeautifulSoup(content, "html.parser").find(class_ = "lifetext").text.split(" ")
        return int(food[2]) - int(food[0])
    
    def eat30(dinoz):
        """
            Eat some tarte à la viande and refill if necessary
        """

        #Reloading food
        if (not inventory.isStock("item_3")):
            inventory.reloadItem("3")

        content = inventory.isInventory(dinoz)

        link = BeautifulSoup(content, "html.parser").find(id = "inv_tartev_use").get_attribute_list("href")[0][1:]

        account().run(link)

    def isStock(item):
        """
            Returns True if there is some of the item left
            Only works on items of the basic shop
        """

        stock = BeautifulSoup(account().run("shop").content, "html.parser").find(id = item).find().text.replace("\t", "").replace("\n", "").split("/")[0]
        return (stock != "\r0")

        
    def isInventory(dino = None, content = None):
        """
            Making the session player look in inventory
            Content is any dinoz page
        """

        if content == None:
            if dino == None:
                dino = utilities.getDinoz()[0]
            content = account().run(f"dino/{dino}").content
        
        if not BeautifulSoup(content, "html.parser").find(id = "inventory"):
            if dino == None:
                dino = utilities.getDinoz()[0]
            content = BeautifulSoup(account().run(f"dino/{dino}/setTab?t=inv").content, "html.parser")
        
        return content
            
    def reloadItem(item_num, num = "24"):
        """
            num (string) : quanity that need to be bought, default 24, maximum from 0
            item_num : the ID of the item in shop as a string
            Reload the item buying in shop
        """
        
        action = BeautifulSoup(account().run("shop").content, "html.parser").find(id = f"form_{item_num}").get_attribute_list("action")[0]
        account().session.post(f"http://www.dinorpg.com" + action,
            data = {
                "oindex": item_num,
                "chk": account().sid, 
                "qty": num
            }
        )