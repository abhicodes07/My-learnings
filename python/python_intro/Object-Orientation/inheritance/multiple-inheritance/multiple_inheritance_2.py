from faker import Faker

class Mother:
    mothername = " "
    def mother(self):
        print(self.mothername)

class Father:
    fathername = " "
    def father(self):
        print(self.fathername)

class Son(Mother, Father):
    def parents(self):
        print(f"Father: {self.fathername}")
        print(f"Mother: {self.mothername}")

fake = Faker()
s1 = Son()
s1.fathername = fake.name_male()
s1.mothername = fake.name_female()

s1.parents()

