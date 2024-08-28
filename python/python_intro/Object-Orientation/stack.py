import numpy as np 
MAX = 1000

class Stack:
    arr = np.zeros([10], dtype=int)
    TOP = 0
    def __init__(self):
        self.TOP = -1
        
    def value(self):
        self.TOP = self.TOP + 1
        print(self.TOP)

    def Push(self, x):
        if self.TOP >= MAX - 1:
            print("Overflow!")
            return False
        else:
            self.TOP = self.TOP + 1
            self.arr[self.TOP] = x
            print(f"Pushed {x} into the stack.")

    def Pop(self):
        if self.TOP < 0:
            print("Underflow!")
            return False 
        else:
            self.TOP = self.TOP - 1
            return self.arr[self.TOP + 1]
            
stack = Stack()
# stack.value()
stack.Push(10)
stack.Push(20)
stack.Push(30)

pop = stack.Pop()
print(pop)
pop = stack.Pop()
print(pop)
pop = stack.Pop()
print(pop)
pop = stack.Pop()
print(pop)
