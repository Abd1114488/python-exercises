from game.item import Item
from game.world import ROUTES
from game import storage


# Ask for name and age. Returns (name, age)
def get_player_info():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    return name, age


# Print the list of commands
def show_menu():
    print("\nMENU")
    print("look       look around")
    print("move       go to another room")
    print("collect    pick up the item here")
    print("gold       check your gold")
    print("buy        buy an item (in the shop)")
    print("talk       talk to the shopkeeper (in the shop)")
    print("inventory  check your inventory")
    print("fix        try to fix the well (in the village)")
    print("save       save your game")
    print("help       show instructions")
    print("lopeta     leave the game")


# Show how much gold the player has
def check_gold(player):
    print(f"You check your pockets... you have {player.gold} gold coins.")


# Buy the filter part in the shop
def buy_item(player):
    if player.location.name != "Shop":
        print("There is no shop here.")
        return
    if player.has_items(["filter part"]):
        print("You already bought the filter part.")
        return
    filter_part = Item("filter part", 2.0, price=20)
    print(f"The shopkeeper shows you a {filter_part.name} for {filter_part.price} gold.")
    if input("Buy it? (yes/no): ") == "yes":
        if player.spend_gold(filter_part.price):
            player.items.append(filter_part)
            print(f"{filter_part.name} was added to your inventory.")
        else:
            print("You don't have enough gold.")
    else:
        print("You decide not to buy it. Maybe next time.")


# Talk to the shopkeeper (only works in the shop)
def talk_to_shopkeeper(player):
    if player.location.name != "Shop":
        print("There is nobody to talk to here.")
        return
    print("Shopkeeper: 'Welcome traveler, take your time looking around!'")
    print(f"{player.name}: 'Thanks, I will.'")
    print("Shopkeeper: 'A filter part could help your well, you know.'")


# Show everything the player carries
def show_inventory(player):
    print("Your inventory:")
    if not player.items:
        print("You don't have any items yet.")
    for item in player.items:
        print("-", item)
    print(f"Total weight: {player.total_weight()} kg")


# Ask where to go, then move the player there
def move_player(player):
    print("Exits:", ", ".join(player.location.exits))
    choice = input("Where do you want to go? ").lower().strip()
    if choice in player.location.exits:
        player.move(player.location.exits[choice])
        print(player.location.describe())
    else:
        print("You can't go there.")


# Pick up the item in the current room
def collect_item(player):
    item = player.collect_item()
    if item:
        print(f"You picked up: {item.name}")
    else:
        print("There is nothing to pick up here.")


# Save the game to the save file
def save_progress(player):
    storage.save_game(player)
    print("Game saved.")


# Try to finish the game. Returns the route name if won, otherwise None
def fix_well(player):
    if player.location.name != "Village":
        print("The well is in the Village. Go there first.")
        return None
    for route_name, route in ROUTES.items():
        if player.has_items(route["needs"]):
            print("\n" + route["ending"])
            print(f"*** YOU WIN! Route: {route_name} ***")
            return route_name
    print("You don't have what you need yet. Ideas:")
    for route in ROUTES.values():
        print("-", route["hint"])
    return None