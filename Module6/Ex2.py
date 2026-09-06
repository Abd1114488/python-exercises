numbers = []
while True:
    text = input("Enter a number (empty to quit): ")
    if text == "":
        break
    numbers.append(int(text))
numbers.sort(reverse=True)

print("Five greatest numbers:")
for n in numbers[0:5]:
    print(n)