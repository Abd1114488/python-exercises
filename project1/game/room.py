# A Room is a location in the game. Rooms connect to each other through exits
class Room:
    def __init__(self,name, description,item=None):
        self.name = name
        self.description = description
        self.item = item      # one Item or None
        self.exits = {}    

    # Make a two way path between this room and another room
    def connect(self, other):
        self.exits[other.name.lower()] = other
        other.exits[self.name.lower()] = self

    # Remove the item from the room and return it (None if there is no item)
    def take_item(self):
        item = self.item
        self.item = None
        return item

    # Return a text that describes the room, its item and its exits
    def describe(self):
        text = f"\n== {self.name} ==\n{self.description}"
        if self.item:
            text += f"\nYou see: {self.item.name}"
        text += "\nExits: " + ", ".join(self.exits)
        return text