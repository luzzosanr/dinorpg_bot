from src.bot import DinorpgApi
from src.destinations import pathFinder
from src.missions import MissionAccomplisher
from bs4 import BeautifulSoup
import requests as req

teams = [["2384201", "2384203", "2384204"]]
bot = DinorpgApi()

# for t in teams:
#     acc = MissionAccomplisher(t)
#     acc.fromZero_toTheEnd()

acc = MissionAccomplisher(teams[0])

acc.ingredients()
acc.domeAccess()
acc.zorc()
acc.getFeuille()
acc.getLanterne()

# with open("test.html", "w") as f:
#     f.write(r.text)