class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def showDetails(self):
        print()
        print(f"Name: {self.name}\nAge: {self.age}")

class Marks(Student):
    def __init__(self, name:str, age:int, eng:int, maths:int, sci:int):
        super().__init__(name, age)
        print()
        self.eng:int = eng
        self.maths:int = maths
        self.sci:int = sci

    def showMarks(self):
        print()
        print(f"Marks of english: {self.eng}")
        print(f"Marks of maths: {self.maths}")
        print(f"Marks of science: {self.sci}")

    def showTotal(self):
        self.total:int = self.eng + self.maths + self.sci
        self.per:float = (self.total/300)*100
        print()
        print(f"Total marks obtained: {self.total}")
        print(f"Total percentage obtained: {self.per}")

m = Marks("Abhinav", 19, 78, 56, 89)
m.showDetails()
m.showMarks()
m.showTotal()
