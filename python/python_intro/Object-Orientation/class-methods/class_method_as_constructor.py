class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def from_string(cls, string):
        name, age = string.split(",")
        return cls(name, int(age))

person = Person.from_string("Flynn steph, 20")
print(person.age)
print(person.name)
