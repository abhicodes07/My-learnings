# this is a program abpu *args in python arguments

def func(*args):
    """
    This args argument method allows us to take in more 
    arguments than the formal arguments defined previously. 
    """
    print(func.__doc__)
    for items in args:
        print(items)

x = [1, 2, 3, 4, 'abhi', 'josh', 'shank']
func(*x)


print()
print()

def funcArgs(normal, *argsemployee):
    """
    1. *args take argumeents as a tuple
    2. we can name *args anything like above or
                *args________(name) 
    """
    print(funcArgs.__doc__)
    
    print(normal)
    for items in argsemployee:
        print(items)
    

emp = ['Abhi', 'Harry', 'flynn', 'sicko', 'julie']
normal = "I am a normal argument"

funcArgs(normal, *emp)

