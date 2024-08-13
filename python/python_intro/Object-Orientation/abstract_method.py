
from abc import ABC, abstractmethod
#
# abstract method in python is a method that is declared within base class
# but doesn't contain any implementation
# abstract methods are meant to be overridden in every derived class 

class Animals(ABC): # abstract class
    def __init__(self):
        print("Some regular animal sound.")
    
    @abstractmethod
    def sound(self): #abstract method
        pass

class Dog(Animals):
    def sound(self):
        print("Bark!")

class Cat(Animals):
    #class that is not implementing the abstract method
    def s(self):
        print("Meow!")

# a = Animals()
b = Dog()
b.sound()
# c = Cat() will throw error
# c.sound()
# c.s()
