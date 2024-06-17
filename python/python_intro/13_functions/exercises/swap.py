#  a program to show swapping of two numbers

def swap(x, y):
    print(f"Before swap x: {x}")
    print(f"Before swap y: {y}")
    print()
    temp = x
    x = y
    y = temp
    print(f"After swap x: {x}")
    print(f"After swap y: {y}")

swap (10, 20)



