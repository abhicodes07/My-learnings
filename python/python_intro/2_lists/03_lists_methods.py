# INTIALISED LIST
l1 = ['Abhi', 'sam', 4.5, True, 100]
print(f"Initialised list: {l1}\n")

# LISTS METHODS
# 1 len() METHOD:
print(f"Length of list: {len(l1)}\n")

# 2 TAKING LIST AS A INPUT FROM THE USER
string = input("Enter list elements [seperated by spaces]: ")
lst = string.split()
print(lst,'''Size of the list: ''' ,len(lst))

# print(help(map))

# SORT METHOD - sort()
list = [1, 2, 45, 7.8, 234]
list.sort()
print(list)
