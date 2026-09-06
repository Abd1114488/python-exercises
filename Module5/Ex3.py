numbers_entered = 0
smallest = 0
largest = 0

while True:
    value = input("Enter your number: ")
    if value == "":
        break
    num = float(value)
    if numbers_entered == 0 or num < smallest:
        smallest = num
    if numbers_entered == 0 or num > largest:
        largest = num
    numbers_entered = numbers_entered + 1