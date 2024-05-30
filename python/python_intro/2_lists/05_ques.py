list1 = []
size = int(input("Enter the size: "))
gap = int(input("Enter the gap in-between: "))
 
for i in range(0, size, gap):
    list1.extend([i])
print("Initialised list: ", list1)

list = []
for i in list1:
    list1.remove(i)
    list.extend([i])
print("Removed list: ", list)
print("New List: ",list1)
    
