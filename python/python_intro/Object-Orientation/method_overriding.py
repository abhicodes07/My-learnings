class Animal:
    def speak(self):
        return "some generic sound"

class Dog(Animal):
    def speak(self):
        return "Bark!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

normal = Animal()
dog = Dog()
cat = Cat()

print(normal.speak())
print(dog.speak())
print(cat.speak())





