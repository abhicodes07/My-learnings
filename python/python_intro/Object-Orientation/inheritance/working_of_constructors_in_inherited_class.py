class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang


dev = Employee("Flynn", 20)

flynn = Programmer("Abhi", 19, "Python")

print(dev.name)
print(dev.id)

print(flynn.name)
print(flynn.id)
print(flynn.lang)
