try:
    x = int(input("Enter a number: "))
    y = 10/x

except Exception as e:
    print("Sorry! An exception has occurred.")

else:
    print(f"The reslut is {y}")

finally:
    print("This will always excute.")

