# Modding
To mod this game, here are some basic instructions.
## How to make Seperate File mods
Instead of changing the code in the game itself, you can make a new file for the game to open up (aka reference). Just do everything here. But when adding new code, copy a code definition (like a score function, etc) and redefine it in the mod file.
## Metadata
You may change the game's metadata to document new modifications.
```
version = "v0.6.0"   # Working version of this file
branch_creator = "TheMadPunter"   # Creator of this file
python_version = sys.version   # Don't change this
mods = ["Vanilla CCA Engine by Themadpunter"]   # Add your mod to this list
mod_versions = ["v1.0 Completed"]   # Add your mod version to this list
modpack_name = "Vanilla CCA Engine"   # Add the name of the working file modpack here
acknowledgements = ["Willie Crowther and Don Woods for Original Game"]   # Add any acknowledgements
other = """"""   # Anything else goes here
```
## Rooms
To create a new room, create code to replace an item of the 'Rooms' list with a Room item. Here are the parameters for the Room item:

1. Room_no - Just set to the item number of the list.

2. Exits - Make a list of four values. Each can be either a room number or the value "q". The first value is north, then east, then south, then west. EXAMPLE: `["q",1,3,"q"]` (A room with one exit to room 1 from the east, and an exit to room 3 to the south.)

3. Description - Just enter the description for the room!
4. Item in room - If you want there to be any items already in a room, just put their ID here. Otherwise, put 0. (To clarify, the ID would be the item number in the "items" list plus one.)

Remember to add a hint for the room you create! For none, just use `""`.
## Adding commands
At the end of the code, in the marked section, all you need to do is add an "elif" to detect for your command. Here are some ways to use commands:

```
elif command == "defen":
    #for "Defenestrate"
    cprint("You threw it out the window!","green")

elif fullcommand == "northeast":
    cprint("Going northeast!","green")

elif split[0] == "use":
    cprint("You used the "+split[1]+".","green")
```
### Using prebuilt commands
Please note that when using the built in commands to this game, some of the commands may reference the variable "room_no". Change these to the rooms in which your command can be used. Do the same with references to the list "invent", replace them with the item number of the item you are referencing.
## Adding new items
Adding new items is one of the simplest things in this game. Add your item to `[items]`, your description to `[itemDesc]`, a shorter description (in your inventory) to `[invDesc]`, and the score you get for depositing it to `[itemScore]`. 
## Legal stuff
When you mod this game, you do not get copyright for any of the code provided in this package. You may, however, get copyright for any changes you make. You do not have permission to change the liscense for this software on any mods you make for it. See the GNU GPLv3: [GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)

When you modify this game, please do not remove any credit from any other designers or modmakers for this game. They deserve credit for their work.

If you would like to distribute a mod of this software under a different liscense, please contact me (Github: familycomicsstudios).
### Notes
This software's base gameplay was created by Willie Crowther and Don Woods. I did not use any code from the original game, however, please note that I made some references to the original game's text. The original game is currently in the public domain, feel free to play it at some point.
## Importing Seperate File Mods
To import a "Seperate File Mod", all you need to do is find this piece of code:
```
#-----------------IMPORT MODS---------------#
# IMPORTING MODS:
# To import a mod, just type here:
# exec(open(sys.path[0]+"/mod.py").read())
# CREATING MODS:
# Basically just copy the functions you want to change, and change them.
if debug == 1:
    cprint("Adding mods...", "red")
#-------------------------------------------#
## Run modpack functions here!
if debug == 1:
    cprint("Loading mods...", "red")
```
Add your mod here:
```
# Basically just copy the functions you want to change, and change them.
if debug == 1:
    cprint("Adding mods...", "red")
## My mod
exec(open(sys.path[0]+"/mod.py").read())
if debug == 1:
    cprint("Added a mod!", "red")
#-------------------------------------------#
```