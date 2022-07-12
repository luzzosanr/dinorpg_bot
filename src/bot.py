from bs4 import BeautifulSoup
import requests as req
from src.destinations import pathFinder

class DinorpgApi:
    """
        All functions return link to an action from different parameters
    """

    def __init__(self) -> None:
        self.session = req.session()
 
        with open("./src/.env", "r") as f:
            logins = [line.replace("\n", "") for line in f.readlines()]

        # Find connexion sid
        # some = BeautifulSoup(self.session.get("http://www.dinorpg.com").content, "html.parser").find(id = "hiddenVars").get_attribute_list("value")
        # print(some)

        # Connexion
        r = self.session.post("https://twinoid.com/user/login/" ,
            data = {
                "login": logins[0],
                "pass": logins[1],
                "sid": "Tqh8V4kVMMlWC5Z50qK1iu7VnhhndHyp",
                "keepSession": "on",
                "submit": "Me+connecter",
                "host": "www.dinorpg.com",
                "fver": "100.0.0",
                "ref": "",
                "refid": "",
                "url": "/",
                "mode": "",
                "proto": "http:",
                "mid": ""
            }
        )
        # Checking connected
        isCo = BeautifulSoup(r.content, "html.parser").find(class_ = "warning") != None

        # Getting the link
        if (isCo):
            self.session.get("http://www.dinorpg.com")

        else:
            self.session.get("http://www.dinorpg.com/tid/login?infos=oy5%3Aphashy32%3A5dcEy9wNox8iYw1TW82h6HIVuw7eWrA4y4%3Alangy2%3Afry4%3Anamey8%3Aluzzosany6%3Arightszy11%3AforceCreatefy6%3Aavatary75%3A%252F%252Fimgup.motion-twin.com%252Ftwinoid%252F3%252F3%252Fab93a10f_210418_100x100.gify6%3ArealIdi1374986y5%3Atokeny32%3A46d961cafd0721cc5f72d6440f207fd2y8%3Aredirectny6%3AtwinIdi210418g;chk=f5ba7e0658fdba7281321977c1a6c1c9")
        
        #Update sid form right cookie
        self.sid = "KlHIrLUQgSE0rPlx4zOvRr8ZmFqvMx73"
        self.session.cookies.set("sid", self.sid)


    def fight(self, dinoId):
        """
            dinoId : integer iding the dino in links
            return : link to learn a new capacity when leveling up
        """

        r = self.session.get(f"http://www.dinorpg.com/dino/{dinoId}/")
        sk = BeautifulSoup(r.content, "html.parser").find(id = "act_fight").find().get_attribute_list("onclick")[0].split('=')[-1][:-2]
        
        self.session.get(f"http://www.dinorpg.com/dino/{dinoId}/act/fight?sk={sk}")

    def checkLevelUp(self, dinoId):
        """
            dinoId : id of the dino tested
            return : False if the dino can't level up, the sk code if it can
        """
        r = self.session.get(f"http://www.dinorpg.com/dino/{dinoId}/")

        bs = BeautifulSoup(r.content, "html.parser")
        levelUp = bs.find(id = "act_levelup")
        if (levelUp != None):
            sk = levelUp.find().get_attribute_list("onclick")[0].split('=')[-1][:-2]
            return sk
        return False
        
    def simpleLevelup(self, dinoId, sk):
        """
            capacity : id of the capacity, ex : force
            dinoId : integer iding the dino in links
            sk : code to run an action
            return : link to learn a new capacity when leveling up
        """

        r = self.session.get(f"http://www.dinorpg.com/dino/{dinoId}/act/levelup?sk={sk}")
        trs = BeautifulSoup(r.content, "html.parser").find(id = "view").find_all("tr")[1:-2]

        link = "http://www.dinorpg.com"
        if (trs == []):
            td = BeautifulSoup(r.content, "html.parser").find(id = "view").find_all("td")[-1]
            link = link + td.get_attribute_list("onclick")[0].split("'")[-2]
        else:
            levels = [link + tr.get_attribute_list("onclick")[0].split("'")[-2] for tr in trs]
            link = levels[0]

        self.session.get(link)


    def levelup(self, capacity, dinoId, sk):
        """
            capacity : id of the capacity, ex : force
            dinoId : integer iding the dino in links
            sk : code to run an action
            return : link to learn a new capacity when leveling up
        """
        return f"/dino/{dinoId}/act/levelup?learn={capacity};sk={sk}"
    
    def checks(self, dinoIds):
        """
            dinoIds : array integer iding the dinos in party, first is leader (on element if alone)
            Checking health and level up and act on it
        """
        
        #Checking dinos : levelup and food
        for id in dinoIds:

            #Reloading food
            if (not self.foodStock30()):
                self.reloadFood30()

            lu = self.checkLevelUp(id)
            if (lu):
                self.simpleLevelup(id, lu)
            if (self.checkFood(id) >= 30):
                self.eat30(id)

    def partySimpleAction(self, dinoIds):
        """
            dinoIds : array integer iding the dinos in party, first is leader (on element if alone)
            Fight and levelup with simple choice or eat when needed (in party)
        """

        self.checks(dinoIds)

        #Making dino fight
        self.fight(dinoIds[0])
    
    def checkFood(self, dinoId):
        """
            dinoId : integer iding the dino in links
            return : hp missing
        """

        self.isInventory(dinoId)
        r = self.session.get(f"http://www.dinorpg.com/dino/{dinoId}")
        food = BeautifulSoup(r.content, "html.parser").find(class_ = "lifetext").text.split(" ")
        return int(food[2]) - int(food[0])
    
    def eat30(self, dinoId):
        """
            dinoId : integer iding the dino in links
            Eat some tarte à la viande and refill if necessary
        """

        self.isInventory(dinoId)
        r = self.session.get(f"http://www.dinorpg.com/dino/{dinoId}/")
        link = BeautifulSoup(r.content, "html.parser").find(id = "inv_tartev_use").get_attribute_list("href")[0]
        self.session.get("http://www.dinorpg.com" + link)
    
    def reloadFood30(self, num = "24"):
        """
            num (string) : quanity that need to be bought, default 24, maximum from 0
            Reload tarte à la viande buying in shop
        """
        
        self.isInventory()
        r = self.session.get(f"http://www.dinorpg.com/shop")
        action = BeautifulSoup(r.content, "html.parser").find(id = "form_3").get_attribute_list("action")[0]
        r = self.session.post(f"http://www.dinorpg.com" + action,
            data = {
                "oindex": "3",
                "chk": self.sid,
                "qty": num
            }
        )
    
    def foodStock30(self):
        """
            return True if there is tarte left
        """

        self.isInventory()
        r = self.session.get(f"http://www.dinorpg.com/shop")
        stock = BeautifulSoup(r.content, "html.parser").find(id = "item_3").find().text.replace("\t", "").replace("\n", "").split("/")[0]
        return (stock != "\r0")
    
    def getDinoz(self):
        """
            return : listof available dinoz of the account
        """
        
        a = BeautifulSoup(self.session.get("http://www.dinorpg.com").content, "html.parser").find(id = "dinozList").find_all("a")
        return [i.get_attribute_list("href")[0][6:] for i in a if i.get_attribute_list("href")[0][:6] == '/dino/']

    def isInventory(self, dino = None):
        """
            Making the session player look in inventory
            return : True if it succeded going in the inventory
        """

        if dino == None:
            dino = self.getDinoz()[0]
        def test():
            return BeautifulSoup(self.session.get(f"http://www.dinorpg.com/dino/{dino}").content, "html.parser").find(id = "inventory") != None

        if not test():
            self.session.get(f"http://www.dinorpg.com/dino/{dino}/setTab?t=inv")
        
        return test()

    def move(self, dest, dinoId):
        """
            dinoId : integer iding the dino in links
            dest : destination the dino is moving to
        """

        r = self.session.get(f"http://www.dinorpg.com/dino/{dinoId}/")
        sk = BeautifulSoup(r.content, "html.parser").find(id = "act_fight").find().get_attribute_list("onclick")[0].split('=')[-1][:-2]
        
        self.session.get(f"http://www.dinorpg.com/dino/{dinoId}/act/move?sk={sk};to={dest}")
    
    def traject(self, path, dinoIds):
        """
            dinoIds : array integer iding the dinos in party, first is leader (on element if alone)
            path : destination the dino will go through
        """

        for d in path:
            self.checks(dinoIds)
            self.move(d, dinoIds[0])

    def getLevel(self, dinoId):
        """
            dinoId : integer iding the dino in links
            return (int) : level of the dino 
        """

        r = self.session.get(f"http://www.dinorpg.com/dino/{dinoId}")
        return int(BeautifulSoup(r.content, "html.parser").find(class_ = "over").text)
    
    def goToLevel(self, dinoIds, level):
        """
            dinoIds : array integer iding the dinos in party, first is leader (on element if alone)
            level : level aimed
            Fight until all dinoz have their level
        """

        def test():
            # Return True if all dinoz got the right level
            for id in dinoIds:
                if self.getLevel(id) < level:
                    return False
            return True
        
        while not test():
            self.partySimpleAction(dinoIds)
    
    def getPlace(self, dinoId):
        """
            dinoId : id of the dino concerned
            return : code of the place it's in
        """

        r = self.session.get(f"http://www.dinorpg.com/")
        all = BeautifulSoup(r.content, "html.parser").find(id = "dinozList").find_all("a")

        for dino in all:
            if dino.get_attribute_list("href")[0] == f"/dino/{dinoId}" and dino.find("em") != None:
                return pathFinder().fullNameToCode(dino.find("em").text)
    
    def goTo(self, dinoIds, dest):
        """
            dinoIds : array integer iding the dinos in party, first is leader (on element if alone)
            dest : destination
            Go to a destination in group
        """

        path = pathFinder().goTo(dest, self.getPlace(dinoIds[0]))
        self.traject(path, dinoIds)
    
    def getSK(self, dinoId):
        """
            dinoId : a dino in the team
            return : the code sk needed for any action
            This code is gotten via fight so doesn't work if fight unavailable
        """

        r = self.session.get(f"http://www.dinorpg.com/dino/{dinoId}/")
        return BeautifulSoup(r.content, "html.parser").find(id = "act_fight").find().get_attribute_list("onclick")[0].split('=')[-1][:-2]
    
    def dissolvGroup(self, dinoId):
        """
            dinoId : id of the chef of the group needed to be dissolve
        """

        sk = self.getSK(dinoId)
        self.session.get(f"http://www.dinorpg.com/dino/{dinoId}/act/dissolve_group?sk={sk}")

    def follow(self, leader, follower):
        """
            leader : id of the dino being the future/current leader
            followers : id of the dinoz following the leader
            Make the followers follow the leader
        """

        sk = self.getSK(leader)
        self.session.get(f"http://www.dinorpg.com/dino/{follower}/act/follow?f={leader};sk={sk}")

    def newTeam(self):
        """
            Buy 3 new dinoz, name them, make them follow each other
            return : id of the 3 dinoz of this new team (first one as leader)
        """
    
        def getId(r):
            lines = BeautifulSoup(r.content, "html.parser").find(id = "dinozList").find("ul").find_all("li")
            for l in lines:
                c = l.find(class_ = "unknown")
                if c != None and c.text == "?":
                    return l.find("a").get_attribute_list("href")[0].split("/")[-1]
        
        dinoz = ["","",""]

        for i in range(3):
            r = self.session.get("http://www.dinorpg.com/shop/dinoz")
            link = BeautifulSoup(r.content, "html.parser").find(id = "detail_0").find(class_ = "button bSmall").get_attribute_list("href")[0]
            r = self.session.get(f"http://www.dinorpg.com{link}")
            dinoz[i] = getId(r)
            self.session.post(f"http://www.dinorpg.com/dino/{dinoz[i]}/name", data = {"name": "points"})
        
        for i in range(1, 3):
            self.follow(dinoz[0], dinoz[i])
        
        return dinoz
        
    
