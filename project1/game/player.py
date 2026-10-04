# The Player stores name, age, gold, items and the room where the player is
class Player:
    def __init__(self,name,age, location,gold=42):
        self.name = name
        self.age = age
        self.location = location
        self.gold = gold
        self.items = []

    # Move to another room
    def move(self, destination):
        self.location = destination

    # Pick up the item in the current room. Returns the item or None
    def collect_item(self):
        item = self.location.take_item()
        if item:
            self.items.append(item)
        return item

    # Pay gold if possible. Returns True on success, False if too poor
    def spend_gold(self, amount):
        if amount > self.gold:
            return False
        self.gold -= amount
        return True

    # Return the combined weight of all carried items
    def total_weight(self):
        return sum(item.weight for item in self.items)

    # Return True if the player carries every item name in the list
    def has_items(self, needed_names):
        carried = [item.name for item in self.items]
        return all(name in carried for name in needed_names)