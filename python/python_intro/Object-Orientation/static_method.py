class Math:
    def __init__(self, num):
        self.num = num

    def addtonum(self, n):
        self.num = self.num + n

    @staticmethod
    def add(a, b):
        """
        Static method in python are  methods that belongs to 
        the class rather than an instance of the class.
        They are called on the basis of the class not on an 
        instance of a class
        """
        print(Math.add.__doc__)
        return a+b
a = Math(5)
print(a.num)

a.addtonum(6)
print(a.num)
# print(Math.add.__doc__)

# using class
print(f"Static method: {Math.add(7, 2)}")

# using instance
print(f"Using instance: {a.add(8, 9)}")
