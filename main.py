import os


class Room:

    def __init__(self, dirs, string):
        self.dirs = dirs
        self.str = string
        #n e s w ne nw se sw


def createList(r1, r2):
    return [item for item in range(r1, r2 + 1)]


#Start main gen
invent = []
rooms = createList(0, 9999)
for i in range(1, 9999):
    rooms[0] = Room([
        "q", rooms[1], "q", "q"
    ], "You are at the end of a small brick road. A small building lies to the east."
                    )
    rooms[1] = Room([
        "q", rooms[2], "q", rooms[0]
    ], "You are inside a building near a small brick road. A door to the east leads outside to a stream.\nThere is a table here."
                    )
    rooms[2] = Room([
        "q", "q", rooms[3], rooms[1]
    ], "You are outside next to a small building. A stream continues south, but a wall blocks your way north."
                    )
    rooms[3] = Room([
        rooms[2], "q", "q", "q"
    ], "You are at the south end of the stream. A cave appears to be to the south."
                    )


#funcs
def start_room(room):
    print(room.str)
    while True:
        command = input("\nWhat's next? ")
        print()
        command = command[:5]
        if command == "e" or command == "east":
            if room.dirs[1] == "q":
                print("You can't go that way!")
            else:
                start_room(room.dirs[1])
        if command == "n" or command == "north":
            if room.dirs[0] == "q":
                print("You can't go that way!")
            else:
                start_room(room.dirs[0])
        if command == "s" or command == "south":
            if room.dirs[2] == "q":
                print("You can't go that way!")
            else:
                start_room(room.dirs[2])
        if command == "w" or command == "west":
            if room.dirs[3] == "q":
                print("You can't go that way!")
            else:
                start_room(room.dirs[3])
        if command == "inven":
            inventory()


def inventory():
    print("You are holding:")
    for item in invent:
        print(item.capitalize())
    if len(invent) < 1:
        print("Some lint in your pockets")


def game_over():
    os._exit(1)


print("Welcome to Adventure Fangame!")
print("Original development by Willie Crowther.")
print("Major features added by Don Woods.")
print("Fangame created by Noah Condoluci.")
print("Would you like instructions?")
input("What's next? ")
print(
    "You're not getting any instructions, I don't have that big of a budget. Play the original game: https://rickadams.org/adventure/advent/."
)
start_room(rooms[0])
