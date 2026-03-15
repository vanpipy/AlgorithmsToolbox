from .ArrayStack import ArrayStack

MIN_LEN_TO_BALANCE = 4

class DualArrayDeque:
    def __init__(self):
        self.front = ArrayStack()
        self.rear = ArrayStack()
        self.n = 0

    def __len__(self):
        return self.n

    def get(self, i):
        if i < 0 or i >= self.n:
            return None
        if i >= len(self.front):
            return self.rear.get(i - len(self.front))
        else:
            return self.front.get(len(self.front) - 1 - i)

    def set(self, i, x):
        if i < 0 or i >= self.n:
            raise IndexError("Index out of range")
        if i >= len(self.front):
            self.rear.set(i - len(self.front), x)
        else:
            self.front.set(len(self.front) - 1 - i, x)

    def add_first(self, x):
        self.front.push(x)
        self.n += 1
        if len(self.front) // 3 > len(self.rear) and len(self.front) > MIN_LEN_TO_BALANCE:
            self.balance()

    def add_last(self, x):
        self.rear.push(x)
        self.n += 1
        if len(self.rear) // 3 > len(self.front) and len(self.rear) > MIN_LEN_TO_BALANCE:
            self.balance()

    def remove_first(self):
        if self.n == 0:
            raise IndexError("remove from empty deque")
        if len(self.front) == 0:
            self.balance()
        if len(self.front) == 0 and len(self.rear) == 1:
            self.n -= 1
            return self.rear.pop()
        x = self.front.pop()
        self.n -= 1
        if len(self.rear) // 3 > len(self.front) and len(self.rear) > MIN_LEN_TO_BALANCE:
            self.balance()
        return x

    def remove_last(self):
        if self.n == 0:
            raise IndexError("remove from empty deque")
        if len(self.rear) == 0:
            self.balance()
        if len(self.rear) == 0 and len(self.front) == 1:
            self.n -= 1
            return self.front.pop()
        x = self.rear.pop()
        self.n -= 1
        if len(self.front) // 3 > len(self.rear) and len(self.front) > MIN_LEN_TO_BALANCE:
            self.balance()
        return x

    def balance(self):
        temp = [self.get(i) for i in range(self.n)]
        mid = self.n // 2
        new_front = ArrayStack()
        new_rear = ArrayStack()

        for i in range(mid - 1, -1, -1):
            new_front.push(temp[i])
        for i in range(mid, self.n):
            new_rear.push(temp[i])

        self.front = new_front
        self.rear = new_rear
