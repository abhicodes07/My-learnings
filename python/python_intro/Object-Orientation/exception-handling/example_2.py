def fun(a):
    if a < 4:
        b = a/(a-3)
    print(f"Value of n: {b}")

try:
    fun(3)
    # fun(5)
except ZeroDivisionError as e:
    print("ZeroDivisionError Occurred and handled.")
except NameError as e:
    print("Name error occurred and handled.")

    
