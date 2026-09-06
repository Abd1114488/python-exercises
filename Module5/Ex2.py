inches = float(input("Give inches (negative to quit): "))

while inches >= 0:
    cm = inches * 2.54
    print("That is", cm, "centimeters")
    inches = float(input("Give inches (negative to quit): "))

print("Program ended")