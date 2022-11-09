from src.strategy.basic import basicStrategy
from src.strategy.missions import missionAccomplisher

"""
    Going to level 19 and to be frozen
"""

name = input("Enter the name of the dinoz :\n")
if name == "":
    name = "points"

while basicStrategy.oldTeam(name):
    acc = missionAccomplisher(basicStrategy.oldTeam(name))
    acc.fromZero_toTheEnd()


while True:
    acc = missionAccomplisher(basicStrategy.newTeam(name))
    acc.fromZero_toTheEnd()
