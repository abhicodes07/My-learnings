# This is a program about **kwargs in python 

# Function
def funcArgu(nomral, *argslist, **kwargswork):
    
    """
    **kwargs are used to pass keyworded variable length
    arguments argument.
    **kwargs recieve argument as a dictionary (key, value)
    pair. 
    """
    
    print(nomral)
    print("Company employees: ")
    
    # *args
    for items in argslist:
        print(items)
   
    print()
    print()

    # **kwargs
    print("In our department we have: \n")
    print(funcArgu.__doc__)
    for key, value in kwargswork.items():
        print(f"{value} as a {key}.")


# main
x = [1, 2, 3, 4, 5, 'abhi', 'julie']
work = {
    'Coder' : 'Abhi',
    'Monitor' : 'Sam',
    'Sports' : 'Flynn',
    'Instructor' : 'Joseph'
}
normal = "I am just a normal argument."

funcArgu(normal, *x, **work)


