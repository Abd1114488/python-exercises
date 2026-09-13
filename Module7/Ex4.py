def sum_list(numbers):
    total = 0
    for n in numbers:
        total = total + n
    return total

nums = [1, 2, 3, 4, 5]
print(sum_list(nums))