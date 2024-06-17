# anonymous function in python are used short functions and can be used with lambda keyword
# #
anonymous = lambda x,y:x+y
print(anonymous(2, 3))

a = [[1, 14], [5, 6], [8, 23]]
a.sort(key=lambda x:x[1])
print(a)



cube = lambda x:x*x*x
print(cube(2))


