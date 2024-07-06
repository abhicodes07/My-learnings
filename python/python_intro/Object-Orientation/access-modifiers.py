# one leading underscore
# Protected data
class Square:
    def __init__(self):
        self._height = 2 # the underscore indicates that this data shouldn't be changed
        self._width = 2

    def setSide(self, new_value):
        self._height = new_value
        self._width = new_value
square = Square()
square._height = 3 # still changes the value or date
