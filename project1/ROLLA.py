from game.player import Player
from game.world import build_world
from game import actions,storage


# Load a saved game or create a new player. Returns a Player or None
def start_game(rooms):
    if storage.save_exists():
        if input("Saved game found. Continue? (yes/no): ") == "yes":
            player = storage.load_game(rooms)
            if player:
                print(f"Welcome back, {player.name}!")
                return player
            print("Save file could not be read. Starting a new game.")
    name, age = actions.get_player_info()
    if age < 12:
        print("Sorry, you are too young to play this game. Shutting down...")
        return None
    return Player(name, age, rooms["village"])


# The main game loop
def main():
    print(storage.read_text_file("intro.txt"))
    rooms = build_world()
    player = start_game(rooms)
    if player is None:
        return
    print(storage.read_text_file("instructions.txt"))
    print(player.location.describe())

    while True:
        actions.show_menu()
        command = input("What do you want to do? ").lower().strip()

        if command == "lopeta":
            print("See you next time!")
            break
        elif command == "look":
            print(player.location.describe())
        elif command == "move":
            actions.move_player(player)
        elif command == "collect":
            actions.collect_item(player)
        elif command == "gold":
            actions.check_gold(player)
        elif command == "buy":
            actions.buy_item(player)
        elif command == "talk":
            actions.talk_to_shopkeeper(player)
        elif command == "inventory":
            actions.show_inventory(player)
        elif command == "fix":
            if actions.fix_well(player):
                break
        elif command == "save":
            actions.save_progress(player)
        elif command == "help":
            print(storage.read_text_file("instructions.txt"))
        else:
            print("That's not a valid command, try again.")


main()