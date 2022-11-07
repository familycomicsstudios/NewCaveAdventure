"""
Colossal Cave Adventure Sequel
v0.6

Created by TheMadPunter
© 2022

INFO:
Game points max:
number of rooms + total of itemScore + 30
"""
import sys
#-------------------METADATA----------------#
version = "v0.6.0"
branch_creator = "TheMadPunter"
python_version = sys.version
mods = ["Vanilla CCA Engine by Themadpunter"]
mod_versions = ["v1.0 Completed"]
modpack_name = "Vanilla CCA Engine"
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


"""
For documentation purposes:
ALL ITEMS TO DROP FOR MAX POINTS
Pearl (25)
Gold (25)
Vase (25)
Stick (1)
DON'T DROP THE FIRST 2 COINS!
Coins #3 (10)
Silver (25)
Scale (25)
Platinum Sword (50)
OTHER STUFF
Get well in (25)
Don't die (30)
Get Excalibur (25)
SCORE: 196
"""
#Other
vmach = 0
tookCoins = 0
isKey = 1
#Scores
ss = 30
ts = 0
wis = 0
hs = 0
os = 0
#Inventory, items list
invent = []
items = [
    "knife", "rod", "stick", "coins", "oyster", "pearl", "gold", "vase",
    "chips", "silver", "letter", "doormat", "key", "sword", "dragon", "scale",
    "excalibur"
]
itemDesc = [
    "A butter knife lies on the ground.", "A black rod lies on the ground.",
    "A stick lies on the ground.", "Some coins are on the ground here!",
    "An oyster lies on the ground here.", "A pearl lies on the ground here!",
    "There is a gold nugget here!", "There is a vase here!",
    "There is a bag of potato chips here for some reason.",
    "There is a bar of silver here!", "A letter lies on the ground.",
    "A doormat reading, \"Come in\" is on the ground.",
    "A key is on the ground.",
    "A golden sword heroically lies on the ground here.",
    "There is a dragon here!", "There is a dragon scale here!",
    "A platinum sword (Excalibur?) EVEN MORE HEROICALLY lies on the ground here."
]
invDesc = [
    "A butter knife", "A black rod", "A short stick", "Some coins",
    "An oyster", "A valuable pearl", "A gold nugget", "An Oriental vase",
    "A bag of potato chips", "A bar of silver", "A letter from a mailbox",
    "A doormat", "A house key", "A golden sword",
    "why the heck do you have a dragon in your inventory lol",
    "A dragon scale", "A platinum sword (Excalibur)"
]
itemScore = [0, 0, 1, 10, 0, 25, 25, 25, 0, 25, 0, 0, 0, 25, -99999, 25, 50]
#Hints
hints = [
    "Try using directions to move, e.g. \"east\".",
    "A butter knife may eventually be useful for something...", "", "",
    "Hmm. I remember a magic rod from the first game...", "", "", "",
    "Why is \"xyzzy\" written on the wall? Maybe it does something.", "",
    "I wonder what the chute does? Try dropping something down it and seeing if your score increases.",
    "What does the rod do? Well, you can swing it... you can wave it... you can drop it... There are so may possibilites.",
    "What does the rod do? Well, you can swing it... you can wave it... you can drop it... There are so may possibilites.",
    "I feel like there is something inside the oyster. You should open it.",
    "", "Maybe you should just sit down here and look around.", "", "",
    "I wonder if you can buy something from the vending machine?",
    "Try giving him what he wants.", "", "", "What's in the mailbox?",
    "Where would they hide the key? Is it under something?", "",
    "I wonder what you can do with your sword. Can you swing it?",
    "Deposit a golden sword here."
]

#cprint(str(len(hints)), "blue")

#Make rooms
rooms = createList(0, 9999)
rooms[0] = Room(
    0, ["q", 1, "q", "q"],
    "You are at the end of a small brick road. A small building lies to the east.",
    0)
rooms[1] = Room(
    1, ["q", 2, "q", 0],
    "You are inside a building near a small brick road. A door to the east leads outside to a stream.\nThere is a table here.",
    1)
rooms[2] = Room(
    2, ["q", "q", 3, 1],
    "You are outside next to a small building. A stream continues south, but a wall blocks your way north.",
    0)
rooms[3] = Room(
    3, [2, "q", 4, "q"],
    "You are at the south end of the stream. A cave appears to be to the south.",
    0)
rooms[4] = Room(
    4, [3, "q", "q", 5],
    "You are at the mouth of the cave. There is a stream to the north, and a small passageway here to the west.",
    2)
rooms[5] = Room(
    5, ["q", 4, 6, 7],
    "You are in a small room in the cave. The stream continues through a hole into the cave. The mouth of the cave is to your east. There are small passages to the west and south.",
    0)
rooms[6] = Room(
    6, [5, "q", "q", 8],
    "You are inside a small passage in the cave. To the west there is  a room with washed up debris from the river. Behind you, to the north, a small room in the cave.",
    0)
rooms[7] = Room(
    7, ["q", 5, 8, "q"],
    "You are in a small passage in the cave. To the south from here is a room with debris that came from the river. To the east, there is a small room in the cave.",
    3)
rooms[8] = Room(
    8, [7, 6, "q", 9],
    "You are in a room in the cave where the river from outside continues flowing to the inside. There is lots of debris in this room. Passages spring from the north, east, and west.\nAn engraving on the wall reads:\n\"MAGIC WORD XYZZY\".",
    0)
rooms[9] = Room(
    9, ["q", 8, 10, 11],
    "You are in a small hallway in the cave. To the east there is a room with lots of debris, and to the south a room with a mysterious chute. The hallway continues to the west.",
    4)
rooms[10] = Room(
    10, [9, "q", "q", "q"],
    "You are in a room with a mysterious chute. You can deposit items in it, it appears. There is a small hallway to the north.",
    0)
rooms[11] = Room(
    11, ["q", 9, "q", "q"],
    "You are at the end of the hallway. The cave appears to continue on, but there is a giant pit in the way.",
    0)
rooms[12] = Room(
    12, ["q", "q", "q", 13],
    "You are at a continuation of the hallway. There is a giant pit to the west. The hallway continues to the west.",
    0)
rooms[13] = Room(
    13, ["q", 12, "q", 14],
    "You are in a hallway. The walls are slightly smoother on the left side of the wall, but look like swiss cheese on the right. The hallway continues to both the west and the east.",
    5)
rooms[14] = Room(
    14, [15, 13, 16, "q"],
    "You are at the end of a hallway. The hall branches to the north and the south.",
    7)
rooms[15] = Room(
    15, ["q", "q", 14, "q"],
    "You are inside a room with a lot of rocks on the floor. One big rock here reads: \"Y2\".",
    0)
rooms[16] = Room(
    16, [14, 17, "q", "q"],
    "You are inside a room with a lot of antique items. A hallway is to the north, and another to the east.",
    8)
rooms[17] = Room(
    17, ["q", 18, "q", 16],
    "You are inside a room with a slab on the floor that appears to have fallen from the ceiling. There is another room to the west, and to the east.",
    0)
rooms[18] = Room(
    18, [20, 19, "q", 17],
    "You are inside a room with warm walls. There is a passage to the west, the east, and the north.",
    0)
rooms[19] = Room(
    19, ["q", 21, "q", 18],
    "You are inside a room with slightly warm walls. There is a passage to the west and the east. There is a vending machine here!\nThe vending machine reads: Pay me some coins for a prize!",
    0)
rooms[20] = Room(
    20, ["q", "q", 18, "q"],
    "You are inside a room next to the edge of a cliff. You can see an exit to the cave, but can't reach it due to a cliff being in your way.\nAn old man is here, asking if he can borrow some potato chips.",
    0)
rooms[21] = Room(
    21, ["q", 22, "q", 19],
    "You are inside a room with cold walls. A path loops around to the east and eventually comes out to a exit of the cave.",
    0)
rooms[22] = Room(
    22, [23, 25, "q", 21],
    "You are at a different enterance to the cave. There is a house to the north. There is a mailbox here. Part of the cave is to the west, and part is to the east.",
    0)
rooms[23] = Room(
    23, ["q", "q", 22, "q"],
    "You are at a house. An enterance to the cave is to the south. It appears you can't get in without a key.",
    12)
rooms[24] = Room(24, ["q", "q", 23, "q"],
                 "You are inside a house. An exit is to the south.", 14)
rooms[25] = Room(
    25, ["q", 26, "q", 22],
    "You are inside the cave again. There is an exit to the west and to the east.",
    15)
rooms[26] = Room(
    26, ["q", "q", "q", 25],
    "You are inside a lit room in the cave. There is a brilliant stone here with an inscription on it: \"Yummy Sword\". I think it wants your sword.",
    0)


#funcs
def start_room(room):
    global room_no, wis, invent, hs, vmach, tookCoins
    global isKey, ss, os
    cprint(room.str, "green")
    room_no = room.no
    if wis < room_no:
        wis = room_no
    if room.item > 0:
        cprint(itemDesc[room.item - 1], "green")
    if random.randint(1, 5) == 1:
        if room_no == 15:
            cprint("A hollow voice says, \"Plugh\".", "green")
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
                if (13 in invent and room_no == 23):
                    start_room(rooms[24])
                elif room.dirs[0] == "q":
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
                if random.randint(0, 5) == 1:
                    if room_no == 15:
                        cprint("A hollow voice says, \"Plugh\".", "green")
            elif profanity.contains_profanity(
                    command) and not split[0] == "kill":
                cprint("Watch it!", "green")
            elif split[0] == "take" or split[0] == "grab" or split[0] == "get":
                if room.item > 0:
                    if room.item == 12:
                        if isKey == 1:
                            isKey = 2
                    if room.item == 15:
                        cprint(
                            "You just picked up a dragon! Oh wait. No. You didn't. Please contact a mental health professional.",
                            "green")
                    else:
                        room.item = take(split, room.item)
                    if isKey == 2:
                        cprint("A key is under the doormat!", "green")

                        room.item = 13
                        isKey = 0
            elif split[0] == "drop" or split[0] == "throw":
                drop(split, room)
            elif command == "xyzzy":
                if 2 in invent:

                    if room_no == 1:
                        start_room(rooms[8])
                    elif room_no == 8:
                        start_room(rooms[1])
                    else:
                        cprint("Nothing happens.", "green")
                else:
                    cprint("I don't know how to apply that word here!",
                           "green")
            elif command == "plugh":
                if 2 in invent:

                    if room_no == 15:
                        start_room(rooms[1])
                    elif room_no == 1:
                        start_room(rooms[15])
                    else:
                        cprint("Nothing happens.", "green")
                else:
                    cprint("I don't know how to apply that word here!",
                           "green")
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
                if room_no == 10:
                    deposit(split, room)
                elif room_no == 26:
                    if 14 in invent:
                        cprint(
                            "You heroically deposit your sword into the pedestal. A white light flashes in the sky, and you see a number increase somewhere. The sword floats out of the pedestal back into your inventory, and turns platinum. It's Excalibur now, I think.",
                            "green")
                        i = invent.index(14)
                        invent = invent[:i] + [17] + invent[i + 1:]
                        os += 25
                    else:
                        cprint("You can only deposit a golden sword here!",
                               "green")
                else:
                    cprint("You cannot deposit anything here.", "green")
            elif split[0] == "wave":
                if split[1] == "rod":
                    if 7 in invent:
                        cprint("You can't wave the rod, for some reason.",
                               "green")
                    else:
                        if room_no == 11:
                            start_room(rooms[12])
                        elif room_no == 12:
                            start_room(rooms[11])
                        else:
                            cprint("Nothing happens.", "green")
                else:
                    cprint("You can't wave that!", "green")
            elif split[0] == "open":
                if split[1] == "oyster":
                    if 5 in invent and 1 in invent:
                        i = invent.index(5)
                        invent = invent[:i] + [6] + invent[i + 1:]
                        cprint(
                            "You crack open the oyster. There is a pearl inside!",
                            "green")
                    else:
                        cprint("You can't!", "green")
                elif split[1] == "mailbox":
                    if room_no == 22:
                        cprint(
                            "You open the mailbox. There is a letter inside!",
                            "green")
                        if room.item > 0:
                            cprint(
                                "It was going to fall out onto the ground, but there's already something there.",
                                "green")
                        else:
                            cprint("It falls out on the ground.", "green")
                            room.item = 11

                    else:
                        cprint("What mailbox?", "green")
                elif split[1] == "chips":
                    if 9 in invent:
                        cprint(
                            "Nghhhh... they're... so... dang... hard... to... open... just... like... that... pickle jar...",
                            "green")
                    else:
                        cprint("What chips?", "green")
                else:
                    cprint("Ok. How do you open that?", "green")
            elif split[0] == "swing":
                if split[1] == "rod":
                    if 2 in invent:
                        if 7 in invent:
                            cprint("You can't swing the rod, for some reason.",
                                   "green")
                        else:

                            cprint("Nothing happens.", "green")
                    else:
                        cprint("You don't have one!", "green")
                elif split[1] == "sword":
                    if 14 or 17 in invent:
                        if 7 in invent:
                            cprint(
                                "You can't swing the sword, for some reason.",
                                "green")
                        else:
                            if room_no == 25:
                                if room.item == 15:
                                    cprint(
                                        "Congratulations! You just killed a dragon with a sword! (At least that's believable...)\nYou got 15 EXP!\nYou leveled up!\nYou got a dragon scale!",
                                        "green")
                                    invent.append(16)
                                    room.item = 0
                                else:
                                    cprint("Whoa! That's heavy!", "green")
                            else:
                                cprint("Nothing happens.", "green")
                    else:
                        cprint("You don't have one!", "green")
                else:
                    cprint("You can't swing that!", "green")
            elif command == "hint":
                if hints[room_no] == "":
                    cprint("There are no hints right now.", "green")
                else:
                    hs -= 1
                    cprint("Taking one point off your score to get a hint...",
                           "green")
                    cprint(hints[room_no], "green")
            elif command == "nothing" or command == "wait":
                cprint("Waiting...", "green")
            elif split[0] == "buy":
                if room_no == 19:
                    if 4 in invent:

                        if vmach == 0:
                            cprint(
                                "You deposit coins in the vending machine. You get a bag of potato chips.",
                                "green")
                            i = invent.index(4)
                            invent = invent[:i] + [9] + invent[i + 1:]
                            vmach += 1
                        elif vmach == 1:
                            cprint(
                                "You deposit coins in the vending machine. You get a bar of silver.",
                                "green")
                            i = invent.index(4)
                            invent = invent[:i] + [10] + invent[i + 1:]
                            vmach += 1
                        else:
                            cprint("All out of prizes.", "green")
                    else:
                        cprint("You don't have any money!", "green")
                else:
                    cprint("Nothing to buy here.", "green")
            elif split[0] == "eat":
                if split[1] == "chips":
                    cprint("You're not hungry.", "green")
                else:
                    cprint("You can't eat that!", "green")
            elif split[0] == "drink":
                if False:
                    cprint("You're not thirsty.", "green")
                else:
                    cprint("You can't drink that!", "green")
            elif split[0] == "give":
                if room_no == 20:
                    if split[1] == "chips":
                        cprint(
                            "You give him the chips. He gives you some coins.",
                            "green")
                        i = invent.index(9)
                        invent = invent[:i] + [4] + invent[i + 1:]
                    else:
                        cprint("He doesn't want those.", "green")
                else:
                    cprint("Nobody to give things to.", "green")
            elif split[0] == "read":
                if split[1] == "letter":
                    if 11 in invent:
                        cprint("You read the letter.", "green")
                        cprint(
                            """-----------LATE PAYMENT NOTICE-------------
Dear Mr. Bananalimorangeramnairtime:
Your credit card bill was due 928374928 years ago. We still have not gotten it back.
Please pay this bill, or we will contact the authorities on how much time you have been late on this payment.
My condolences,
Bob

P. S. lolololololololololololololololol

Enclosed are some coins.""", "green")
                        if tookCoins == 0:
                            invent.append(4)
                            tookCoins = 1
                    else:
                        cprint("What letter?", "green")
                else:
                    cprint("I'm game. How do you do that?", "green")
            elif split[0] == "dbgr":
                start_room(rooms[int(split[1])])
            elif split[0] == "dbgi":
                invent.append(int(split[1]))
            elif split[0] == "attack" or split[0] == "kill" or split[
                    0] == "slay":
                if split[1] == "dragon":
                    if room_no == 25:
                        really_what = input(
                            colored("With what? Your bare hands? ", "green"))
                        if really_what[0] == "y":
                            cprint(
                                "You attacked a dragon with your bare hands! It didn't go well!",
                                "green")
                            ss = 0
                            cprint("Game over!", "green")
                            score()
                            game_over()
                        else:
                            cprint("Good. I'm glad you came to your senses.",
                                   "green")
                    else:
                        cprint("Dragon? Where?", "green")
                else:
                    cprint("You can't attack that.", "green")
            elif command == "debug":
                debug_stuff()
            else:
                cprint("I don't know what that means!", "green")
        except:
            cprint("I don't think that works.", "green")


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


def score():
    cprint("Treasures: " + str(ts), "green")
    cprint("Survival: " + str(ss), "green")
    cprint("Getting well in: " + str(wis), "green")
    cprint("Hints used: " + str(0 - hs), "green")
    if os > 0:
        print("Other: " + str(os), "green")
    cprint("Score: " + str(ts + ss + wis + hs + os), "green")


def news():
    cprint("V0.5 more stuff like excalibur", "green")
    cprint("V0.4: Added a lot more treasure and also a dragon", "green")
    cprint("V0.3: We have a 151 point game yay", "green")
    cprint(
        "V0.2: Added some more rooms, some more treasures, some more mechanics...",
        "green")
    cprint("V0.1: Added the basic engine, including picking stuff up, etc.",
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
