class Student:
    def __init__(self, name, age, fname, mname):
        self.name = name
        self.age = age
        self.fname = fname
        self.mname = mname 
    
    def details(self):
        """This is an example of class method as an alternative constructor.
        The purpose of of it to create an object from data that is stored in different data format such as string or dictionary."""

    @classmethod
    def from_details(cls, string):
        name, age, fname, mname = string.split(",")
        return cls(name, int(age), fname, mname)

s = Student.from_details("Flynn steph, 19, Josh, queena")
print(s.name)
print(s.age)
print(s.fname)
print(s.mname)
print(s.details.__doc__)
