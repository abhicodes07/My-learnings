# This is a class introduction 
# Class is created using 'class' keyword

class Person:
    # The following variables are known as attributes 
    name = "Abhi"
    age = 19
    occ = "Software developer"
    
    # This is a class method with a self as a parameter
    # self parameter is used to access variables inside the class
    def details(self):
        print(f"My name is {self.name}, age is {self.age} and my occupation is {self.occ}")

# Here this is a object of a class
obj = Person()

# accessing class methods using initialised object
obj.details()

