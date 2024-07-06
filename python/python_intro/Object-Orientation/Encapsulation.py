class Square:
    def __init__(self):
        self.height = 2
        self.width = 2

    def setSide(self, new_value):
        self.height = new_value
        self.width = new_value
square = Square()
square.height = 3 # not a square anymore so the data needs to be protected 
# so that no one can change it

