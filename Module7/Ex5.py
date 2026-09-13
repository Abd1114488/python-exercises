def remove_uneven(numbers):
    new_list = []
    for n in numbers:
        if n % 2 == 0:
            new_list.append(n)
    return new_list

nums = [1, 2, 3, 4, 5, 6, 7, 8]
even_nums = remove_uneven(nums)
print("Original:", nums)
print("Even only:", even_nums)