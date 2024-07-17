class Employee:
    def __init__(self, name, id):
        self.name = name # Instance variable
        self.id = id # Instance variable

    def printInfo(self):
        print(self.name)
        print(self.id)

e1 = Employee("Rohan", 102)
e1.printInfo()

e2 = Employee("Sam", 103)
e2.printInfo()
