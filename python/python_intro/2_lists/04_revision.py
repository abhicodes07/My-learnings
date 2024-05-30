import string

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lst)

for i in range(len(lst)):
    print(lst[i]+1)
print("\n")
print("Sum of numbers in list: ",sum(lst))

# lst2 = int(input("Enter the numbers seperated by spaces: "))
# lst3 = lst2.split()
# print(lst3)





lst3 = [2, 3, 12, 4, 0, 234, 7.6]
# lst4 = lst3.sort()
lst3.sort()
print(lst3)

