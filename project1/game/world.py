from game.item import Item
from game.room import Room

# The three ways to win. Each route has the items needed and an ending text
ROUTES = {
    "Engineer": {
        "needs": ["filter part", "pipes"],
        "hint": "Build a water filter (you need a filter part and pipes).",
        "ending": "You build a filter on the well. The water runs clear!",
    },
    "Community": {
        "needs": ["trash bag", "gloves"],
        "hint": "Clean the source with the villagers (you need a trash bag and gloves).",
        "ending": "The villagers clean the river together. The well is pure again!",
    },
    "Nature": {
        "needs": ["seedling", "spring water"],
        "hint": "Protect the source with nature (you need a seedling and spring water).",
        "ending": "You plant the tree and add spring water. The well heals itself!",
    },
}


# Create all rooms and items, connect them, and return a dictionary of rooms
def build_world():
    rooms = {
        "village": Room("Village", "Your village. The well water looks dirty."),
        "shop": Room("Shop", "A small shop run by an old shopkeeper."),
        "forest": Room("Forest", "A quiet forest with tall trees.", Item("seedling", 0.5)),
        "river": Room("River", "The river carries trash downstream.", Item("trash bag", 1.0)),
        "workshop": Room("Workshop", "An old workshop full of tools.", Item("pipes", 3.0)),
        "school": Room("School", "A small village school.", Item("gloves", 0.3)),
        "spring": Room("Spring", "A clean mountain spring.", Item("spring water", 2.0)),
    }
    rooms["village"].connect(rooms["shop"])
    rooms["village"].connect(rooms["forest"])
    rooms["village"].connect(rooms["workshop"])
    rooms["village"].connect(rooms["school"])
    rooms["forest"].connect(rooms["river"])
    rooms["forest"].connect(rooms["spring"])
    return rooms