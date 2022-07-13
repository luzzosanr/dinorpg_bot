from src.bot import DinorpgApi
from src.destinations import pathFinder
from src.missions import MissionAccomplisher
from bs4 import BeautifulSoup
import requests as req

bot = DinorpgApi()

# def isWorking():
#     r = bot.session.get(f"http://www.dinorpg.com/shop")
#     if BeautifulSoup(r.content, "html.parser").find(id = "item_3"):
#         return True
#     print(r)
#     return False

# while isWorking():
#    pass
