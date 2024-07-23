
# GETTERS, SETTER AND DELETER

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = f"{self.first}.{self.last}@gmail.com"
    
    # In order to continue using email like an attribute we add an @property decorator i.e., a setter
    @property
    # we are defining email as an method but we can use it as an attribute
    def email(self):
        return f"{self.first}.{self.last}@gmail.com"
    @property
    def fullName(self):
        return f"{self.first} {self.last}"

    @fullName.setter
    def fullName(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    # a deleter
    @fullName.deleter
    def fullName(self):
        print("Deleter Name")
        self.first = None
        self.last = None

emp1 = Employee('Flynn', 'Steph')

# emp1.first = "Abhinav"
# emp1.last = "Asthana"

emp1.fullName = 'Chiffler Hans'

print(emp1.first)
print(emp1.email) # using email as property 
print(emp1.fullName)

# del emp1.fullName

# print(emp1.first)
# print(emp1.email) # using email as property 
# print(emp1.fullName)

