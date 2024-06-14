# adding two numbers using two function syntaxes 

# SYNTAX 1

def __firstsynadd__(num1, num2):
    print("Adding two numbers using first syntax of function: ")
    print(num1+num2)
num1, num2 = input("Enter num1 and num2 for syntax one: ").split()
__firstsynadd__(int(num1), int(num2))

# SYNTAX 2

def __scndsynadd__(num3, num4: int) -> int:
    add = num3+num4
    print("Adding two numbers using syntax two: ", add)
    print(type(add))
num3, num4 = input("Enter num1 and num2 for syntax one: ").split()
__scndsynadd__(int(num3), int(num4))


