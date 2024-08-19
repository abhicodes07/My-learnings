class Base:
    def __init__(self):
        self.a = int(input("Enter the number a: "))
        self.b = int(input("Enter the number b:"))
    
    def __str__(self):
        return f"Two numbers: {self.a} and {self.b}"

    def __mul__(self, other):
        return f"Their multiplication: {self.a * other.a} and {self.b * other.b}"


num1 = Base()
num2 = Base()

num3 = num1 * num2

print(num3)
print(type(num3))
