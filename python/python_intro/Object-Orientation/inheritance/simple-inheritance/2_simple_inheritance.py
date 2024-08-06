class Base:
    def __init__(self):
        print("Constructor of Base class Invoked.")

class Derived(Base):
    def __init__(self):
        super().__init__() #accessing Constructor of base class using super keyword
        print("Constructor of Derived class Invoked.")

# b = Base()
d = Derived()



