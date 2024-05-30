list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Initialised list: \n",list)

list.remove(20)
print("List after element removal: \n",list)
print("\n")

list.pop(5)
print("List after using pop method: ", list)


for i in list:
    list.pop(i)
print("Looped removing: ",list)
