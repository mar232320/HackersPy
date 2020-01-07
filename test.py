#For testing purposes only. For final commits please go to HackersPySim.py

import json
woahh = open("worm.json")
woah = json.load(woahh)
woahhhh = woah["DPS"]
level = woahhhh["21"]
print(level)