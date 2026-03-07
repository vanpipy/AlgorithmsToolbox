# 循环动态队列
class DynamicArrayQueue:
    def __init__(self, size = 4):
        self.size = size
        self.head = 0
        self.n = 0
        self.data = [None] * size

    def __len__(self):
        return self.n

    def add(self, x):
        if self.n >= self.size:
            self.resize()
        self.data[(self.head + self.n) % self.size] = x
        self.n += 1

    def remove(self):
        if self.n <= 0:
            return None
        x = self.data[self.head]
        self.head = (self.head + 1) % self.size
        self.n -= 1
        if self.n <= self.size // 3:
            self.resize(1/2)
        return x

    def resize(self, scale = 2):
        new_size = max(1, int(self.size * scale))
        new_data = [None] * new_size
        for i in range(self.n):
            new_data[i] = self.data[(self.head + i) % self.size]
        self.head = 0
        self.data = new_data
        self.size = new_size
