from faker import Faker
import random

class Student:
    def __init__(self):
        self.name = fake.name()
        self.age = random.randint(20, 30)
        self.email = fake.email()
        self.city = fake.city()

    def details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"City: {self.city}")

class Marks:
    eng = random.randint(60, 100)
    math = random.randint(60, 100)
    sci = random.randint(60, 100)
    com = random.randint(60, 100)

    def marks(self):
        print(f"Marks in English: {self.eng}")
        print(f"Marks in Maths: {self.math}")
        print(f"Marks in Science: {self.sci}")
        print(f"Marks in Computer: {self.com}")

class Result(Student, Marks):
    def result(self):
        # super(Student).__init__()
        # super(Marks).__init__()
        self.total = self.eng + self.math + self.sci + self.com
        self.per = (self.total/400) * 100
        self.details()
        self.marks()
        print(f"Total marks obtained: {self.total}")
        print(f"Total percentage: {self.per}")


fake = Faker()
s1 = Result()
s1.result()
# print()
# s2 = Student()
# s2.details()
# print()
# s3 = Marks()
# s3.marks()
# print()
