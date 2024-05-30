# INITIALISING LIST
# LIST OF MUTABLE NUMBERS WITH HOMOGENOUS BEHAVIOUR

l1 = [1, 2, 3, 4 , 5, 6, 7, 8, 9, 10]
print(l1[1])

# LIST OF DISTINCT ELEMENTS
l2 = ['abhi', True, False, 'Gummy bear', 5.6, 5]
print(l2)

for i in range(0, 6):
    print(l2[i])

l3 = [['Apple', 'Banana', 'Strawberry', 'Watermelon'], [1, 2, 3, 4], [76.6, 8.9, 34.65, 23.54]]
print("Length of list: \n",len(l3))

for i in range(0, len(l3)):
    for j in range(0, len(l3)):
        print(l3[i][j])




