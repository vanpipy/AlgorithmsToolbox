import unittest
from src.SLList import Node, SLList

class TestSLList(unittest.TestCase):
    # 1️⃣ 基础操作测试

    def test_empty(self):
        """S1: 新创建的链表 - len=0 ， head=None ， tail=None"""
        s = SLList()
        self.assertEqual(len(s), 0)
        self.assertEqual(s.n, 0)
        self.assertIsNone(s.head)
        self.assertIsNone(s.tail)

    def test_add_first_one(self):
        """S2: 头部加一个元素 - len=1 ，head=tail=该元素"""
        s = SLList()
        a = Node("a")
        s.add_first(a)
        self.assertEqual(len(s), 1)
        self.assertEqual(s.n, 1)
        self.assertIs(s.head, a)
        self.assertIs(s.tail, a)

    def test_add_last_one(self):
        """S3: 尾部加一个元素 - len=1 ，head=tail=该元素"""
        s = SLList()
        a = Node("a")
        s.add_last(a)
        self.assertEqual(len(s), 1)
        self.assertEqual(s.n, 1)
        self.assertIs(s.head, a)
        self.assertIs(s.tail, a)

    def test_add_first_multiple(self):
        """S4: 头部加多个元素 - 顺序正确（后进先出）"""
        s = SLList()
        nodes = [Node(i) for i in [1, 2, 3, 4, 5]]
        for node in nodes:
            s.add_first(node)
        self.assertEqual(len(s), 5)

        out = [s.remove_first().value for _ in range(5)]
        self.assertEqual(out, [5, 4, 3, 2, 1])
        self.assertEqual(len(s), 0)
        self.assertIsNone(s.head)
        self.assertIsNone(s.tail)

    def test_add_last_multiple(self):
        """S5: 尾部加多个元素 - 顺序正确（先进先出）"""
        s = SLList()
        nodes = [Node(i) for i in [1, 2, 3, 4, 5]]
        for node in nodes:
            s.add_last(node)
        self.assertEqual(len(s), 5)

        out = [s.remove_first().value for _ in range(5)]
        self.assertEqual(out, [1, 2, 3, 4, 5])
        self.assertEqual(len(s), 0)
        self.assertIsNone(s.head)
        self.assertIsNone(s.tail)

    # 2️⃣ 移除操作测试

    def test_remove_first_one(self):
        """S6: 移除唯一元素 - 返回该元素，链表变空"""
        s = SLList()
        a = Node("a")
        s.add_first(a)

        removed = s.remove_first()
        self.assertIs(removed, a)
        self.assertEqual(len(s), 0)
        self.assertIsNone(s.head)
        self.assertIsNone(s.tail)

    def test_remove_first_multiple(self):
        """S7: 从头移除多个元素 - FIFO 顺序"""
        s = SLList()
        nodes = [Node(i) for i in [1, 2, 3, 4, 5]]
        for node in nodes:
            s.add_last(node)

        out = [s.remove_first().value for _ in range(5)]
        self.assertEqual(out, [1, 2, 3, 4, 5])
        self.assertEqual(len(s), 0)
        self.assertIsNone(s.head)
        self.assertIsNone(s.tail)

    def test_remove_first_empty(self):
        """S8: 空链表移除 - 抛出异常"""
        s = SLList()
        with self.assertRaises(IndexError):
            s.remove_first()

    def test_remove_last_one(self):
        """S9: 移除唯一元素 - 返回该元素，链表变空"""
        s = SLList()
        a = Node("a")
        s.add_last(a)

        removed = s.remove_last()
        self.assertIs(removed, a)
        self.assertEqual(len(s), 0)
        self.assertIsNone(s.head)
        self.assertIsNone(s.tail)

    def test_remove_last_multiple(self):
        """S10: 从尾移除多个元素 - LIFO 顺序"""
        s = SLList()
        nodes = [Node(i) for i in [1, 2, 3, 4, 5]]
        for node in nodes:
            s.add_last(node)

        out = [s.remove_last().value for _ in range(5)]
        self.assertEqual(out, [5, 4, 3, 2, 1])
        self.assertEqual(len(s), 0)
        self.assertIsNone(s.head)
        self.assertIsNone(s.tail)

    # # 3️⃣ 混合操作测试

    def test_mixed_add(self):
        """S11: 交替头尾添加 - 顺序正确"""
        s = SLList()
        s.add_last(Node(4))
        s.add_first(Node(3))
        s.add_last(Node(5))
        s.add_first(Node(2))
        s.add_last(Node(6))
        s.add_first(Node(1))

        self.assertEqual(len(s), 6)
        out = [s.remove_first().value for _ in range(6)]
        self.assertEqual(out, [1, 2, 3, 4, 5, 6])
        self.assertEqual(len(s), 0)
        self.assertIsNone(s.head)
        self.assertIsNone(s.tail)

    def test_alternating_remove(self):
        """S12: 交替头尾移除 - 顺序正确"""
        s = SLList()
        for i in range(6):
            s.add_last(Node(i))

        out = [
            s.remove_first().value,
            s.remove_last().value,
            s.remove_first().value,
            s.remove_last().value,
            s.remove_first().value,
            s.remove_last().value,
        ]
        self.assertEqual(out, [0, 5, 1, 4, 2, 3])
        self.assertEqual(len(s), 0)
        self.assertIsNone(s.head)
        self.assertIsNone(s.tail)

    def test_add_after_remove(self):
        """S13: 移除后继续添加 - 正常工作"""
        s = SLList()
        s.add_last(Node(1))
        s.add_last(Node(2))
        self.assertEqual(s.remove_first().value, 1)
        self.assertEqual(s.remove_last().value, 2)
        self.assertEqual(len(s), 0)
        self.assertIsNone(s.head)
        self.assertIsNone(s.tail)

        s.add_first(Node(10))
        s.add_last(Node(20))
        self.assertEqual(len(s), 2)
        self.assertEqual(s.remove_first().value, 10)
        self.assertEqual(s.remove_first().value, 20)
        self.assertEqual(len(s), 0)
        self.assertIsNone(s.head)
        self.assertIsNone(s.tail)

    # 4️⃣ 边界条件测试

    def test_head_tail_sync(self):
        """S14: 各种操作后 - head 和 tail 始终正确"""
        s = SLList()

        a = Node("a")
        s.add_first(a)
        self.assertIs(s.head, a)
        self.assertIs(s.tail, a)

        b = Node("b")
        s.add_last(b)
        self.assertIs(s.head, a)
        self.assertIs(s.tail, b)

        c = Node("c")
        s.add_first(c)
        self.assertIs(s.head, c)
        self.assertIs(s.tail, b)

        self.assertIs(s.remove_last(), b)
        self.assertIs(s.head, c)
        self.assertIs(s.tail, a)

        self.assertIs(s.remove_first(), c)
        self.assertIs(s.head, a)
        self.assertIs(s.tail, a)

        self.assertIs(s.remove_first(), a)
        self.assertIsNone(s.head)
        self.assertIsNone(s.tail)
        self.assertEqual(len(s), 0)

    def test_single_element_remove(self):
        """S15: 单元素链表的各种操作 - 正确更新 head/tail"""
        s = SLList()

        a = Node("a")
        s.add_first(a)
        self.assertIs(s.remove_last(), a)
        self.assertIsNone(s.head)
        self.assertIsNone(s.tail)
        self.assertEqual(len(s), 0)

        b = Node("b")
        s.add_last(b)
        self.assertIs(s.remove_first(), b)
        self.assertIsNone(s.head)
        self.assertIsNone(s.tail)
        self.assertEqual(len(s), 0)

    def test_remove_last_after_many(self):
        """S16: 大量操作后尾部删除 - tail 正确更新"""
        s = SLList()
        nodes = [Node(i) for i in range(20)]
        for node in nodes:
            s.add_last(node)

        for _ in range(8):
            s.remove_first()
        self.assertEqual(len(s), 12)
        self.assertIs(s.head, nodes[8])
        self.assertIs(s.tail, nodes[19])

        removed = s.remove_last()
        self.assertIs(removed, nodes[19])
        self.assertEqual(len(s), 11)
        self.assertIs(s.tail, nodes[18])


if __name__ == "__main__":
    unittest.main()
