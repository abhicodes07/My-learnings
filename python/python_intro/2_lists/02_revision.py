import string
l1 = [1, 2, 3, 4, 5]
l2 = ['Abhi', 'Sam', 'Flynn', 'Jhon']
l3 = [1 ,2, 'Abhi', True, 12.5]
l4 = [[10, 20], [30, 40]]

l5 = [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]],[['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j']]]

print(l1)
print(l2)
print(l3)
print(l4)


print(len(l1))
print(len(l2))
print(len(l3))
print(len(l4))

print(l4[0][1])

print(l5[0][0][1])
print("Length: ", len(l5))


for i in range(0, 2):
    for j in range(0, 2):
        for k in range(0, 5):
            print(f"Value of L5[{i}][{j}][{k}] element:",l5[i][j][k])
            
# REVISION 
# string = input("Enter the elements seperated by whitespaces: ")
# lst1 = string.split()
# print(lst1)
k = 1
for i in range(0, 6):
    print()
    for j in range(0, k):
        print("*", end='')  
    k = k+1

print()
print()
print()

for i in range(0, 6):
    print()
    for j in range(0, 6):
        print("#",end='')



print()



list2 = [1, 2, 3, 4, 5]
list_nd = list2.index(3)
print(list_nd)
