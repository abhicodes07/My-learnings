      #
      #           VEHICAL 
      #              |
      #       _________________
      #       |               |
      #      CAR            TRUCK
      #       |
      #   __________ 
      #   |        |
      # SEDAN     SUV
      #
class Vehical:
    def __init__(self):
        print("This is vehical.")

class Car(Vehical):
    def __init__(self):
        super().__init__()
        print("This vehical is a car.")

class Truck(Vehical):
    def __init__(self):
        super().__init__()
        print("This vehical is a truck.")

class Sedan(Car):
    def __init__(self):
        super().__init__()
        print("This car is sedan.")

class SUV(Car):
    def __init__(self):
        super().__init__()
        print("This car is suv.")


v1 = SUV()
v2 = Sedan()

v3 = Truck()
v4 = Car()
