print("Welcome, Player!")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"player name: {name}")
print(f"player age: {age}")

if age < 12:
    print("Sorry, you are too young to play this game. Shutting down...")
else:
    print(f"\nHey {name}, welcome to the shop!")

    while True:
        print("\nMENU")
        print("gold check how much gold you have")
        print("buy buy an item from the shop")
        print("talk talk to the shopkeeper")
        print("lopeta leave the shop")

        command = input("What do you want to do? ")

        if command == "lopeta":
            print("You leave the shop. See you next time!")
            break
        elif command == "gold":
            print("You check your pockets... you have 42 gold coins.")
        elif command == "buy":
            print("The shopkeeper shows you a rusty old sword.")
            print(f"{name}: 'Hmm, this looks kinda weak...'")
            print("You decide not to buy it. Maybe next time.")
        elif command == "talk":
            print("Shopkeeper: 'Welcome traveler, take your time looking around!'")
            print(f"{name}: 'Thanks, I will.'")
        else:
            print("That's not a valid command, try again.")