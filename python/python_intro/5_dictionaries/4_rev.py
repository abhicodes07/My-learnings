devil = {
    'Devil' : 'The devil that is apart timer and is a main character.',
    'Name' : 'Maou sadao',
    'Crush' : 'Chio chan',
    'villain side-kick' : 'Emilia or Emi',
    'General' : 'Ashiya',
    'Anime' : 'A evil is a part-timer.'
}

print("Initialised string: ", devil)

# Printing all the items of evil dict

print("Printing the key values: ")
print("\n\n")

for i in devil:
    print(i, ":", devil[i])

print(devil.keys())


nested = {
    1 : 'Flynn',
    2 : 'Sam',
    3 : 'Abhi',
    4 : {
        'Name' : 'Abhinav',
        'Course' : 'BCA'
    }
}

for i in nested:
    print(i, ":", nested[i])
    
