class Vector:
    obj = 0
    def __init__(self):
        self.count()
        self.x = int(input(f"Enter value of x in vector {self.obj}: "))
        self.y = int(input(f"Enter value of y in vector {self.obj}: "))
        
    # here repr is used to provide an "official" string representation of an object 
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    # self is the instance on the left side of +
    # other is the instance on the right side of +
    @classmethod
    def count(cls):
        cls.obj+=1

    def __add__(self, other):
        return f"Vector({self.x + other.x}, {self.y + other.y})"

    def __sub__(self, other):
        return f"Vector({self.x - other.x}, {self.x - other.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
v1 = Vector()
v2 = Vector()

print(repr(v1))
print()
print(f"{v1} + {v2} = {v1+v2}")
print(f"{v1} - {v2} = {v1-v2}")
print(f"{v1} == {v2} = {v1 == v2}")


