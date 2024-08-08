class Complex:
    def __init__(self, r, i):
        self.real = r
        self.imag = i

    def __str__(self):
        return f"Complex: {self.real} + {self.imag}i"

    def __add__(self, other):
        return f"Addition of complex: {self.real + other.real} + {self.imag + other.imag}i"

c1 = Complex(10, 20)
print(c1)

c2 = Complex(20, 30)
print(c2)

print(c1 + c2)
