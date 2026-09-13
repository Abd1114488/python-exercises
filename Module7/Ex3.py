def gallons_to_liters(gallons):
    return gallons * 3.78541

gallons = float(input("Enter gallons (negative to stop): "))
while gallons >= 0:
    liters = gallons_to_liters(gallons)
    print("That is", liters, "liters")
    gallons = float(input("Enter gallons (negative to stop): "))