print("Welcome, Player!")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"player name: {name}")
print(f"player age: {age}")

inventory = []

def check_gold():
    print("You check your pockets... you have 42 gold coins.")

def buy_item():
    print("The shopkeeper shows you a rusty old sword.")
    print(f"{name}: 'Hmm, this looks kinda weak...'")
    item = input("Do you want to buy it anyway? Type the item name to buy it, or press enter to skip: ")
    if item != "":
        inventory.append(item)
        print(item, "was added to your inventory.")
    else:
        print("You decide not to buy it. Maybe next time.")

def show_inventory():
    print("Your inventory:")
    if len(inventory) == 0:
        print("You don't have any items yet.")
    else:
        for item in inventory:
            print("-", item)

def talk_to_shopkeeper():
    print("Shopkeeper: 'Welcome traveler, take your time looking around!'")
    print(f"{name}: 'Thanks, I will.'")

if age < 12:
    print("Sorry, you are too young to play this game. Shutting down...")
else:
    print(f"\nHey {name}, welcome to the shop!")

    while True:
        print("\nMENU")
        print("gold check how much gold you have")
        print("buy buy an item from the shop")
        print("talk talk to the shopkeeper")
        print("inventory check your inventory")
        print("lopeta leave the shop")

        command = input("What do you want to do? ")

        if command == "lopeta":
            print("You leave the shop. See you next time!")
            break
        elif command == "gold":
            check_gold()
        elif command == "buy":
            buy_item()
        elif command == "talk":
            talk_to_shopkeeper()
        elif command == "inventory":
            show_inventory()
        else:
            print("That's not a valid command, try again.")