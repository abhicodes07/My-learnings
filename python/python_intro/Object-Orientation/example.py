class Person:
    name = "Abhi"
    occ = "Software developer"
    networth = 10

    def info(self):
        print(f"{self.name} is {self.occ}")

# Initialising a objet out of class
a = Person()

a.name = "Sam"
a.occ = "Accountant"

# Accessing the information 
a.info()
