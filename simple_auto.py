from src.bot import DinorpgApi
from src.destinations import pathFinder
from src.missions import MissionAccomplisher
from bs4 import BeautifulSoup
import requests as req

"""
    Going to level 19 and to be frozen
"""

bot = DinorpgApi()

name = input("Enter the name of the dinoz :\n")
if name == "":
    name = "points"

while bot.getPointsTeam():
    acc = MissionAccomplisher(bot.getPointsTeam(name))
    acc.fromZero_toTheEnd()


while True:
    acc = MissionAccomplisher(bot.newTeam(name))
    acc.fromZero_toTheEnd()
