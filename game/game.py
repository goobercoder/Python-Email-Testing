import time
from gameassets import *
line = "--------------------------------------------------------------------"
print(line)
class you:
    def __init__(self, name = None, hp = 100, strength = 20, age = 0, gender = "undefined", home = "undefined"):
        self.name = name
        self.hp = hp
        self.age = age
        self.gender = gender
        self.home = home
        self.strength = strength
        self.money = 100
class npc:
    def __init__(self, name = None, hp = 100, strength = 20, age = 0, gender = "undefined", home = "undefined"):
        self.name = name
        self.hp = hp
        self.age = age
        self.gender = gender
        self.home = home
        self.strength = strength
print("Hello Adventurer, welcome to your new adventure!\nBut first, create your Character:")
c = you()
load()
c.name = input("First, what will be your name?: ")
dd = input("what difficulty do you want? (easy, med, hard): ") 
if dd.lower() == "easy":
    difficulty = "easy"
    c.hp = 150
    c.strength = 50
    print("difficulty set to " + difficulty)
elif dd.lower() == "med":
    difficulty = "medium"
    c.hp = 110
    c.strength = 35
    print("difficulty set to " + difficulty)
elif dd.lower() == "hard":
    difficulty = "hard"
    c.hp = 85
    c.strength = 20
    print("difficulty set to " + difficulty)
else:
    print("INVALID!")
    exit()
c.age = int(input("How old will you be? (this will not affect any other stats): "))
c.gender = input("what is your gender?: ")
c.home = input("lastly, where do you come from?: ")
print("well, character completion is done, just to remember here are you stats: ")
time.sleep(1)
print(line)
print(f"name: {c.name}\nage: {c.age}\nhp: {c.hp}\nstrength: {c.strength}\ngender: {c.gender}\nhome: {c.home}\nmoney: {c.money}\ndifficulty: {difficulty}")
print(line)
time.sleep(0.5)
y()
print(line)
load()
print("you start in a bar, you can see lots of people of lots of races.")
time.sleep(1)
print("you go and sit down and order a drink, but what drink?")
time.sleep(1)
print("1. water.\n2. beer.\n3. wine.\n4. soda.")
while True:
    try:
        drink = int(input("what do you choose?: "))
        break
    except:
        print("not a number")
if drink == 1 or drink == 2 or drink == 3 or drink == 4:
    drink = int(drink)
else:
    print("not one of the options, you get no drink.")
    drink = 0
    