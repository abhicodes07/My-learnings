class Dog:
    breed = "German" # Class varible
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
dog1 = Dog("Mike", 3)
dog2 = Dog("Destroyer", 5)

print(dog1.name, dog1.age, dog1.breed)
print(dog2.name, dog2.age, dog2.breed)
print(Dog.breed)
