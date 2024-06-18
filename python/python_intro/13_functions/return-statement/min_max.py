def get_min_max(numbers):
    min_value = min(numbers)
    max_value = max(numbers)
    
    return min_value, max_value

min_value, max_value = get_min_max([4, 5, 3, 34, 2, 65, 23, 5, 32, 78, 2])


print(min_value)
print(max_value)
