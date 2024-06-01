a = int(input("Enter the number: "))
b = int(input("Enter the number: "))

if a == b:
    print("a equals b")
    if a % b == 0:
        print("a is divisible by b")
        print("Answer: ", a/b)
    else:
        print("a is not divisible by b")
elif a > b:
    print("a is larger than b")
    if a % b == 0:
        print("a is divisible by b")
        print("Answer: ", a/b)
    else:
        print("a is not divisible by b")
else:
    print("a is smaller than b")
