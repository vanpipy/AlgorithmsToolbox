class DLNode:
    __slots__ = "value", "next", "prev"

    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

# 双链表
class DLList:
    def __init__(self):
        self.dummy = DLNode(None)
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy
        self.n = 0

    def __len__(self):
        return self.n

    def add_first(self, node):
        pass

    def add_last(self, node):
        pass

    def remove_first(self):
        pass

    def remove_last(self):
        pass

    def get(self, index):
        pass