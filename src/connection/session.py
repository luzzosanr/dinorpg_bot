from bs4 import BeautifulSoup
from matplotlib.pyplot import connect
import requests as req


class account(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(account, cls).__new__(cls)
        return cls.instance
    
    def __init__(self):
        self.sk = None
        self.connect()

    def connect(self):
        self.session = req.session()

        with open("./src/connection/.env", "r") as f:
            logins = [line.replace("\n", "") for line in f.readlines()]
        
        with open("./src/connection/.sid", "r") as f:
            sids = [line.replace("\n", "") for line in f.readlines()]

        # Find connexion sid
        # some = BeautifulSoup(self.session.get("http://www.dinorpg.com").content, "html.parser").find(id = "hiddenVars").get_attribute_list("value")
        # print(some)

        # Connexion
        r = self.session.post("https://twinoid.com/user/login/" ,
            data = {
                "login": logins[0],
                "pass": logins[1],
                "sid": sids[0],
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
        self.sid = sids[1]
        self.session.cookies.set("sid", self.sid)

    def run(self, link = "", fullLink = None):
        """
            Run the website
            Link is what comes after http://www.dinorpg.com/
            Use full link to start from the begining
        """

        if fullLink:
            self.session.get(fullLink)

        return self.session.get(f"http://www.dinorpg.com/{link}")

    def getSk(self):
        """
            Giving the sk through shop
            sk is a code needed for each new action, probably to avoid bot

            sk can be set if a page is loaded but no action is done
        """

        if self.sk:
            return self.sk
        
        t = self.session.get(f"http://www.dinorpg.com/shop").text
        p = t.find("sk=")
        return t[p + 3 : p + 11]