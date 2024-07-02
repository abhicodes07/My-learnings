def greet(fx):
    def efx(*args, **kwargs):
        print("Hello!")
        fx(*args, **kwargs)
        print("Bye!")
    return efx

@greet # this is a decorator
def name():
    print("Abhinav")

# without @ syntax
def add(a, b):
    print(a+b)

# either we can use above func or this one
# greet(name)()

greet(add)(10, 20)
