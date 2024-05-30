import array as arr

array = arr.array('i', [])
print(f"Initialised array: {array}")
print()
# Appending items into the array
for i in range(10, 110, 10):
    array.extend([i])
print(f"Extended array: {array}")

# Counting the occurences of any number in an array
print(f"Number of occurences of 10: {array.count(10)}")

# Reverrsing the initiated array 
array.reverse()
print(f"Reversed array: {array}")



