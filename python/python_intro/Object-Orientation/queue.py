import numpy as np
MAX = 1000

class Queue:
    HEAD = 0 # Dequeue
    TAIL = 0 # Enqueue
    arr = np.zeros([MAX], dtype=int)
    def __init__(self):
        self.TAIL = -1
        self.HEAD = -1

    def Enqueue(self, x):
    # check overflow condition
        if self.TAIL == MAX:
            print("Overflow")
            return False
        
        else:
            self.TAIL += 1
            self.arr[self.TAIL] = x
            print(f"{x} Enqueued.")

    def Dequeue(self):
    # check underflow condtion
        if self.HEAD > self.TAIL:
            print("Queue Underflow!")
            return False
        else:
            self.HEAD += 1
            self.val = self.arr[self.HEAD]
            print(f"{self.val} Dequeued.")

queue = Queue()
queue.Enqueue(10)
queue.Enqueue(20)
queue.Enqueue(30)
queue.Enqueue(40)

queue.Dequeue()
queue.Dequeue()


