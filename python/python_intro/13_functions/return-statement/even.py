def find_first_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            return num
    return None

first_even = find_first_even([1, 3, 5, 7, 8, 10])
print(first_even)  # Output: 8
