# 固长循环队列
class ArrayQueue:
    def __init__(self, size = 4):
        self.size = size
        self.head = 0
        self.n = 0
        self.data = [None] * size

    def __len__(self):
        return self.n

    def add(self, x):
        if self.n >= self.size:
            raise OverflowError("Cannot add, queue is full")
        self.data[(self.head + self.n) % self.size] = x
        self.n += 1

    def remove(self):
        if self.n <= 0:
            raise IndexError("Cannot remove, queue is empty")
        x = self.data[self.head]
        self.data[self.head] = None
        self.head = (self.head + 1) % self.size
        self.n -= 1
        return x
