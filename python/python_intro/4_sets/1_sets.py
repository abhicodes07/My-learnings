# sets example
# using set() method
my_set = set([1, 2, 3, 4, 5])
print("First set: ",my_set)

# using curly braces and commas
anthr_set = {'abhi', 5, True, 7.6}
print("Second set: ",anthr_set)

for i in my_set:
    print("Elements in set: ",i)

# Initialising a set
set1 = set() # an empty set
set1.add(12)
set1.add(13)
set1.add(14)
# iterating elements 
for i in range(10):
    set1.add(i)
print("Third set: ", set1)

set1.update(['abhi', 'is', 'me'])
set1.update([("This", "is", "a", "tuple.")])
print("Set after updatation: ", set1)

print("Length of set: ",len(set1))
