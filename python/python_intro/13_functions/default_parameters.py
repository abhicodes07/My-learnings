# This is program about default parameters

def my_func(x, y=5):
    """
    Here default argument is y. When no value is
    passed to y argument, it's value will automatically be taken as
    5
    """
    print(f"x = {x}")
    print(f"y = {y}")
    print(x+y)
x = 20
# y = 20
my_func(x)
print(my_func.__doc__)




