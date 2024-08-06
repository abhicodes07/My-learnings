class Employee:
    def __init__(self, name, id):
        self.name = name 
        self.id = id

    def showDetails(self):
        print(f"Name: {self.name}\nAge: {self.id}")

class Programmer(Employee):
    def showlanguage(self):
        print("The default language is python")

e = Employee("Abhi", 31)
p = Programmer("Jhon", 30)
e.showDetails()

p.showDetails()
p.showlanguage()
