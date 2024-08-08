class Callable:
    def __init__(self, value):
        self.value = value
    
    # call is a special method that allows an instance of class as a it were a function 
    def __call__(self, increment):
        self.value += self.increment
        return self.value
obj = Callable(10)
print(obj(10))
print(obj(50))
        
