print("This cruise ship has Four cabin classes (LUX, A, B, C) ")
cabin_class = input("Enter your cabin class for this cruise \nNOTE enter only uppercase letters. ")
if cabin_class == "LUX":
    print("upper-deck cabin with a balcony")
elif cabin_class == "A":
    print("above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("windowless cabin above the car deck")
elif cabin_class == "C":
    print("windowless cabin below the car deck")
else:
    print("Invalid cabin class.")