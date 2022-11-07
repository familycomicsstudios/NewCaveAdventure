"""
Colossal Cave Adventure Sequel - Engine
v1.0.0 Completed

Created by TheMadPunter
© 2022

INFO:
Game points max:
number of rooms + total of itemScore + 30
"""
import sys
#-------------------METADATA----------------#
version = "v1.0.0 Completed"
branch_creator = "TheMadPunter"
python_version = sys.version
mods = ["New CCA Engine by Themadpunter"]
mod_versions = ["v1.0.0 Completed"]
modpack_name = "New CCA Engine"
acknowledgements = ["Willie Crowther and Don Woods for Original Game"]
other = """"""
#-------------------END META----------------#

########################################
##                                    ##
##       Main program starts          ##
##                                    ##
########################################
import os
from better_profanity import profanity
import random
from termcolor import colored, cprint


class Room:

    def __init__(self, room, dirs, string, item):
        self.dirs = dirs
        self.str = string
        self.item = item
        self.no = room
        #n e s w ne nw se sw


def createList(r1, r2):
    return [item for item in range(r1, r2 + 1)]



#Other
vmach = 0
tookCoins = 0
isKey = 1
#Scores
ss = 30
ts = 0
wis = 0
hs = 0
ots = 0
#Inventory, items list
invent = []
items = [
    "knife"
]
itemDesc = [
    "A butter knife lies on the ground."
]
invDesc = [
    "A butter knife"
]
itemScore = [0]
#Hints
hints = [
    "Try using directions to move, e.g. \"east\"."
]

#cprint(str(len(hints)), "blue")

#Make rooms
rooms = createList(0, 9999)
rooms[0] = Room(
    0, ["q", "q", "q", "q"],
    "You are in a test room.",
    1)


### Need to pre reference
def rscore():
    return (ts + ss + wis + ots)


#funcs
def start_room(room):
    global room_no, wis, invent, hs, vmach, tookCoins
    global isKey, ss, ots
    scores = rscore()
    cprint(room.str, "green")
    room_no = room.no
    if wis < room_no:
        wis = room_no
    if room.item > 0:
        cprint(itemDesc[room.item - 1], "green")
    while True:
        command = input(colored("\nWhat's next? ", "green"))
        print()
        fullcommand = command
        split = command.split(" ")
        command = command[:5]
        try:
            if command == "e" or command == "east":
                if room.dirs[1] == "q":
                    cprint("You can't go that way!", "green")
                else:
                    start_room(rooms[room.dirs[1]])
            elif command == "n" or command == "north":
                if room.dirs[0] == "q":
                    cprint("You can't go that way!", "green")
                else:
                    start_room(rooms[room.dirs[0]])
            elif command == "s" or command == "south":
                if room.dirs[2] == "q":
                    cprint("You can't go that way!", "green")
                else:
                    start_room(rooms[room.dirs[2]])
            elif command == "w" or command == "west":
                if room.dirs[3] == "q":
                    cprint("You can't go that way!", "green")
                else:
                    start_room(rooms[room.dirs[3]])
            elif command == "inven" or command == "i":
                inventory()
            elif command == "look":
                cprint(
                    "Sorry, I am not allowed to give more detail. I will repeat the long description of your location.",
                    "green")
                cprint(room.str, "green")
                if room.item > 0:
                    cprint(itemDesc[room.item - 1], "green")
            
            elif profanity.contains_profanity(
                    command) and not split[0] == "kill":
                cprint("Watch it!", "green")
            elif split[0] == "take" or split[0] == "grab" or split[0] == "get":
                if room.item > 0:
                    room.item = take(split, room.item)
            elif split[0] == "drop" or split[0] == "throw":
                drop(split, room)
            elif command == "help":
                help_cca()
            elif split[0] == "use":
                cprint(
                    "Please be more specific. Use a verb (eg throw, wave, swing)...",
                    "green")
            elif split[0] == "walk" or split[0] == "move":
                cprint("Use cardinal directions to move.", "green")
            elif fullcommand in items:
                cprint(
                    "Try using a verb about this item (eg take item, grab item, drop item, throw item...)",
                    "green")
            elif command == "info":
                info_cca()
            elif command == "score":
                score()
            elif command == "quit":
                score()
                game_over()
            elif command == "news":
                news()
            elif split[0] == "deposit":
                if room_no == 0:
                    deposit(split, room)
                else:
                    cprint("You cannot deposit anything here.", "green")
            elif command == "hint":
                if hints[room_no] == "":
                    cprint("There are no hints right now.", "green")
                else:
                    hs -= 1
                    cprint("Taking one point off your score to get a hint...",
                           "green")
                    cprint(hints[room_no], "green")
            elif command == "nothi" or command == "wait":
                cprint("Waiting...", "green")
            
            elif split[0] == "eat":
                if False:
                    cprint("You're not hungry.", "green")
                else:
                    cprint("You can't eat that!", "green")
            elif split[0] == "drink":
                if False:
                    cprint("You're not thirsty.", "green")
                else:
                    cprint("You can't drink that!", "green")
            elif split[0] == "dbgr":
                start_room(rooms[int(split[1])])
            elif split[0] == "dbgi":
                invent.append(int(split[1]))
            elif command == "debug":
                debug_stuff()
            elif command == "game":
                game_data()
            #----------------MODDING-------------#
            elif False:
                pass
            #------------------------------------#
            else:
                cprint("I don't know what that means!", "green")
        except:
            cprint("I don't think that works.", "green")


def score():
    cprint("Treasures: " + str(ts), "green")
    cprint("Survival: " + str(ss), "green")
    cprint("Getting well in: " + str(wis), "green")
    cprint("Hints used: " + str(0 - hs), "green")
    if ots > 0:
        cprint("Other: " + str(ots), "green")
    cprint("Score: " + str(ts + ss + wis + hs + ots), "green")


def inventory():
    cprint("You are holding:", "green")
    for item in invent:
        cprint(invDesc[item - 1].capitalize(), "green")
    cprint("A headlamp", "green")
    if len(invent) < 1:
        cprint("Some lint in your pockets", "green")


def take(split, item):
    global invent, items
    if split[1] == items[item - 1]:
        invent.append(item)
        cprint("You took the " + items[item - 1] + ".", "green")
        item = 0
        return item
    cprint("What's a " + split[1] + "?", "green")
    return item


def drop(split, room):
    global invent, items, room_no, rooms
    try:
        if not items.index(split[1]) + 1 in invent:
            cprint("You have no " + split[1] + ".", "green")
            return room.item
    except:
        cprint("What's a " + split[1] + "?", "green")
        return room.item

    if room.item > 0:
        cprint("There is not enough room for you to drop this item!", "green")
        return room.item
    items.index(split[1], 0, 9999)
    cprint("You dropped the " + split[1] + ".", "green")
    room.item = items.index(split[1]) + 1
    invent.remove(items.index(split[1], 0, 9999) + 1)
    return room.item


def deposit(split, room):
    global invent, items, room_no, rooms, ts
    try:
        if not items.index(split[1]) + 1 in invent:
            cprint("You have no " + split[1] + ".", "green")
            return room.item
    except:
        cprint("What's a " + split[1] + "?", "green")
        return room.item

    if room.item > 0:
        cprint("There is not enough room for you to drop this item!", "green")
        return room.item
    items.index(split[1], 0, 9999)
    cprint("You deposited the " + split[1] + ".", "green")
    invent.remove(items.index(split[1], 0, 9999) + 1)
    ts += itemScore[items.index(split[1], 0, 9999)]
    return room.item


def help_cca():
    cprint(
        """I know of places, actions, and things.  Most of my vocabulary describes places and is used to move you there.  To move, try words like forest, building, downstream, enter, east, west, north, south, up, or down.  I know about a few special objects, like a black rod hidden in the cave.  These objects can be manipulated using some of the action words that I know.  Usually you will need to give both the object and action words (in either order), but sometimes I can infer the object from the verb alone. 
Some objects also imply verbs; in particular, "inventory" implies "take inventory", which causes me to give you a list of what you're carrying.  Some objects have unexpected effects; the effects are not always desirable!  Usually people having trouble moving just need to try a few more words. 
Usually people trying unsuccessfully to manipulate an object are attempting something beyond their (or my!) capabilities and should try a completely different tack. One point often confusing to beginners is that, when there are several ways to go in a certain direction (e.g., if there are several holes in a wall), choosing that direction in effect chooses one of the ways at random; often, though, by specifying the place you want to reach you can guarantee choosing the right path. Good luck, and have fun!""",
        "green")


def info_cca():
    cprint(
        """For a summary of the most recent changes to the game, say "news". If you want to end your adventure early, say "quit". To see how well you're doing, say "score".  To get full credit for a treasure, you must have deposited it in the chute.  You lose points for getting killed. There are also points based on how much (if any) of the cave you've managed to explore; in particular, there is a large bonus just for getting in (to distinguish the beginners from the rest of the pack), and there are other ways to determine whether you've been through some of the more harrowing sections.  If you think you've found all the treasures, just keep exploring for a while.  If nothing interesting happens, you haven't found them all yet.  If something interesting *DOES* happen (incidentally, there *ARE* ways to hasten things along), it means you're getting a bonus and have an opportunity to garner many more points in the Master's section.""",
        "green")


def news():
    cprint(
        "V1.0.0 Working: Turned the game into an engine.",
        "green")


def game_data():
    cprint("GAME DATA", "yellow")
    cprint("GAME LAUNCHER: " + modpack_name, "blue")
    cprint("LAUNCHER CREATOR: " + branch_creator, "blue")
    cprint("GAME VERSION: " + version, "blue")
    mod_no = 0
    cprint("MODIFICATIONS ADDED", "yellow")
    for mod in mods:
        cprint(mod + " (" + mod_versions[mod_no] + ")", "blue")
        mod_no += 1
    cprint("PYTHON VERSION:", "yellow")
    cprint(python_version, "blue")
    cprint("ACKNOWLEDGMENTS:", "yellow")
    for ackn in acknowledgements:
        cprint(ackn, "blue")
    cprint(other, "blue")


def debug_stuff():
    cprint("DEBUG INFO", "red")
    game_data()
    cprint("VARIBALES", "yellow")
    cprint(str(vmach), "blue")
    cprint(str(isKey), "blue")
    cprint(str(tookCoins), "blue")
    cprint("BASICS", "yellow")
    cprint("Inventory", "blue")
    inventory()
    cprint("Score", "blue")
    score()


def game_over():
    os._exit(1)


cprint("Welcome to Adventure Fangame!", "green")
cprint("Original development by Willie Crowther.", "green")
cprint("Major features added by Don Woods.", "green")
cprint("Fangame created by TheMadPunter.", "green")
cprint("Would you like instructions?", "green")
print()
command = input(colored("\nWhat's next? ", "green"))
print()
try:
    if command[0] == "y":
        cprint(
            "Due to the success of the first game, many have visited the cave in which many treasures dwell.",
            "green")
        cprint(
            "You, as a daring advenurer, have discovered a cave in your hometown, strangely near a building that seems to be unused.",
            "green")
        cprint(
            "I will be your eyes and hands. Direct me with commands of one or two words. I should warn you that I only look at the first five letters of each word, so if you'll have to enter \"Northeast\" as \"ne\" to distinguish it from \"North\". (Should you get stuck, type \"help\" or \"info\" for some general hints.)",
            "green")
        print()
except:
    pass
room_no = 0
start_room(rooms[0])
