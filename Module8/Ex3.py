airports = {}

while True:
    print("\n1. Enter new airport")
    print("2. Fetch airport info")
    print("3. Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        code = input("Enter ICAO code: ")
        name = input("Enter airport name: ")
        airports[code] = name
        print("Airport saved")
    elif choice == "2":
        code = input("Enter ICAO code: ")
        if code in airports:
            print("Airport name:", airports[code])
        else:
            print("Airport not found")
    elif choice == "3":
        break
    else:
        print("Invalid choice")