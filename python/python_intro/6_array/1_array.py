import array

arr = array.array('i', [1, 2, 3, 4, 5])
print(arr)
print("Type: ",type(arr))
for i in range(0, 5):
    print(arr[i])
print(len(arr))

