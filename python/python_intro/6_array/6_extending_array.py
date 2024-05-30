
import array as arr

array = arr.array('i', [10, 20, 30, 40, 50])
for i in array:
    print(i, end=" ")
print()
array.extend([60, 70, 80, 90, 100])

for i in array:
    print(i, end=" ")
print()
