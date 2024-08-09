class Vehicle:
    def __init__(self):
        print("This is a Vehicle.")

class FourWheeler(Vehicle):
    def __init__(self):
        super().__init__()
        print("This vehicle is four wheeler.")

class Car(FourWheeler):
    # invoking constructor of other classe
    def __init__(self):
        super().__init__()
        print("This vehicle is four wheeler car.")

c = Car()


