# This is a program about even and odd


def even(num: int) -> int:
    if num % 2==0:
        print("Number is even.")
    else:
        print("Number is odd.")
a = int(input("Enter the number: "))
even(a)

