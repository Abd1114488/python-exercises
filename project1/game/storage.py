import os
from game.item import Item
from game.player import Player

# Work out where the data folder is, so the game runs from any folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
SAVE_FILE = os.path.join(DATA_DIR, "savegame.txt")


# Return the text of a file in the data folder
def read_text_file(filename):
    path = os.path.join(DATA_DIR, filename)
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return f"[{filename} not found]"


# Return True if a save file exists
def save_exists():
    return os.path.exists(SAVE_FILE)


# Write the player's state to the save file, one value per line
def save_game(player):
    item_text = ";".join(f"{i.name}:{i.weight}" for i in player.items)
    lines = [player.name, str(player.age), str(player.gold),
             player.location.name.lower(), item_text]
    with open(SAVE_FILE, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))


# Remove an already collected item from the rooms, so it can't be taken twice
def remove_from_world(rooms, item_name):
    for room in rooms.values():
        if room.item and room.item.name == item_name:
            room.item = None


# Read the save file and return a Player, or None if loading fails
def load_game(rooms):
    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as file:
            lines = file.read().split("\n")
        player = Player(lines[0], int(lines[1]), rooms[lines[3]], int(lines[2]))
        for part in lines[4].split(";"):
            if part:
                item_name, weight = part.split(":")
                player.items.append(Item(item_name, float(weight)))
                remove_from_world(rooms, item_name)
        return player
    except (FileNotFoundError, ValueError, KeyError, IndexError):
        return None