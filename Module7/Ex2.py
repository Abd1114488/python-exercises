import random
def roll_dice(sides):
    return random.randint(1, sides)

max_num = int(input("Enter the max number on the dice: "))
result = 0
while result != max_num:
    result = roll_dice(max_num)
    print(result)