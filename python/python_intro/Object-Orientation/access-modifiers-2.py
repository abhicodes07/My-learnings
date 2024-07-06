class Square:
    def __init__(self):
        self.__height = 2
        self.__width = 2
    def setSide(self, new_value):
        self.__height = new_value
        self.__width = new_value

square = Square()

square.__height = 3 
print(square.__height)
square._Square__height = 5
print(square._Square__height)

