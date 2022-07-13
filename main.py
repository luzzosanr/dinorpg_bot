from src.bot import DinorpgApi
from src.destinations import pathFinder
from src.missions import MissionAccomplisher
from bs4 import BeautifulSoup
import requests as req

bot = DinorpgApi()

def r():
    return bot.session.get(f"http://www.dinorpg.com/shop")

i = 0
while BeautifulSoup(r().content, "html.parser").find(id = "item_3"):
    i += 1

print(i)

    