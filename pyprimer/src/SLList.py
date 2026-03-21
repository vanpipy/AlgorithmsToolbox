class Node:
    __slots__ = ("value", "next")

    def __init__(self, value):
        self.value = value
        self.next = None

# 单链表
class SLList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.n = 0

    def __len__(self):
        return self.n

    def add_first(self, node):
        if self.n == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.n += 1

    def add_last(self, node):
        if self.n == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.n += 1

    def remove_first(self):
        x = self.head
        if self.n == 0:
            raise IndexError("remove from empty list")
        elif self.n == 1:
            self.head = None
            self.tail = None
        elif self.n == 2:
            self.head = self.tail
            x.next = None
        else:
            self.head = x.next
            x.next = None
        self.n -= 1
        return x

    def remove_last(self):
        x = self.tail
        if self.n == 0:
            raise IndexError("remove from empty list")
        elif self.n == 1:
            self.head = None
            self.tail = None
        elif self.n == 2:
            self.tail = self.head
            self.head.next = None
        else:
            current = self.head
            for _ in range(self.n - 2):
                current = current.next
            current.next = None
            self.tail = current
        self.n -= 1
        return x
