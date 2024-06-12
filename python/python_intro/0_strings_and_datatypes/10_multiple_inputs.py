# TAKING MULTIPLE INPUTS FROM THE USER USING SPLIT FUNCTION

# TAKING TWO INPUTS FROM THE USER
a, b = input("Enter the value of a and b: ").split()
print("\tValue of a: {}\n\tValue of b: {}".format(a, b))

# TAKING THREE INPUTS FROM THE USER
c, d, e = input("Enter three values c, d and e: ").split()
print("\tValue of c: {}\n\tValue of d: {}\n\tValue of e: {}".format(c, d, e))

# TYPECASTING AND USING LIST() FUNCTION
lst = list(map(str, input("Enter multiple values: " ).split())) 
print("Entered values: ", lst)

num1, num2, num3 = input("Enter the three numbers: ").split()
print('''\t Value of num1: {}
         Value of num2: {}
         Value of num3: {}'''.format(num1, num2, num3))
