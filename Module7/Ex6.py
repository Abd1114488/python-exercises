import math

def unit_price(diameter, price):
    radius = diameter / 100 / 2   # cm to meters then radius
    area = math.pi * radius ** 2
    return price / area

d1 = float(input("Diameter of pizza 1 in cm: "))
p1 = float(input("Price of pizza 1 in euros: "))
d2 = float(input("Diameter of pizza 2 in cm: "))
p2 = float(input("Price of pizza 2 in euros: "))

price1 = unit_price(d1, p1)
price2 = unit_price(d2, p2)

print("Pizza 1 unit price:", price1)
print("Pizza 2 unit price:", price2)

if price1 < price2:
    print("Pizza 1 is better value")
else:
    print("Pizza 2 is better value")