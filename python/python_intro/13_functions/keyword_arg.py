# program about keyword arguments in python 

def myName(firstname, lastname):
    """
    Keyword arguments allows argument name with its value
    however you need to keep in my mind that order or arguments shouldn't
    change.
    """
    print(f"Hii my name is {firstname} {lastname}")
    print(f"Firstname = {firstname}, Lastname = {lastname}")

myName(firstname='Abhinav', lastname='asthana')
myName(lastname='Abhinav', firstname='asthana')
print(myName.__doc__)




