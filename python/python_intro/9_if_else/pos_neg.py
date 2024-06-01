# Creating a program to demonstrate if whether the 
# entered number is positive or negative

num = int(input("Enter a number: "))

if num < 0:
    print("Entered number is negative.")
elif num > 0:
    print("Entered number is positive.")
else:
    print("Entered number is equal to 0.")

