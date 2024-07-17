class Math:
    def __init__(self, num):
        self.num = num

    def addtonum(self, n):
        self.num = self.num + n

    @staticmethod
    def add(a, b):
        return a+b
a = Math(5)
print(a.num)

a.addtonum(6)
print(a.num)

# using class
print(f"Static method: {Math.add(7, 2)}")

# using instance
print(f"Using instance: {a.add(8, 9)}")
