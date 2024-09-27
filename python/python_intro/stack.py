
class Stack:
    MAX = 1000
    TOP = 0
    arr = []

    def __init__(self):
        TOP = -1

    def Push(self, x):
        if self.TOP > self.MAX - 1:
            print("Overflow!")
        else:
            self.arr[self.TOP] = x
            print(f"{x} pushed into stack.")

    def Pop(self):
        pass



