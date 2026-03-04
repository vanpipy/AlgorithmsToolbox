class ArrayStack:
    def __init__(self):
        self._data = [None] * 1
        self._n = 0

    def __len__(self):
        return self._n

    def push(self, x):
        if self._n >= len(self._data):
            self.resize()
        self._data[self._n] = x
        self._n += 1
        return self._n

    def pop(self):
        if self._n == 0:
            raise IndexError("pop from empty stack")
        top = self._n - 1
        temp = self._data[top]
        self._data[top] = None
        self._n -= 1
        if self._n <= len(self._data) // 3:
            self.resize()
        return temp

    def get(self, i):
        if i < 0 or i >= self._n:
            return None
        return self._data[i]

    def set(self, i, x):
        if i < 0 or i >= self._n:
            raise IndexError("Index out of range")
        self._data[i] = x

    def resize(self):
        new_max = max(1, self._n * 2)
        new_array_stack = [None] * new_max
        for i in range(self._n):
            new_array_stack[i] = self._data[i]
        self._data = new_array_stack
