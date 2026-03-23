import random
import unittest

from src.DLList import DLList, DLNode


class TestDLList(unittest.TestCase):
    def _values_forward(self, d: DLList):
        out = []
        node = d.dummy.next
        while node is not d.dummy:
            out.append(node.value)
            node = node.next
        return out

    def _values_backward(self, d: DLList):
        out = []
        node = d.dummy.prev
        while node is not d.dummy:
            out.append(node.value)
            node = node.prev
        return out

    def _nodes_forward(self, d: DLList):
        out = []
        node = d.dummy.next
        while node is not d.dummy:
            out.append(node)
            node = node.next
        return out

    def _assert_integrity(self, d: DLList, expected_values=None):
        self.assertEqual(len(d), d.n)
        self.assertIsNotNone(d.dummy)
        self.assertIs(d.dummy.next.prev, d.dummy)
        self.assertIs(d.dummy.prev.next, d.dummy)

        nodes = self._nodes_forward(d)
        self.assertEqual(len(nodes), len(d))

        if len(d) == 0:
            self.assertIs(d.dummy.next, d.dummy)
            self.assertIs(d.dummy.prev, d.dummy)
        else:
            self.assertIs(d.dummy.next, nodes[0])
            self.assertIs(d.dummy.prev, nodes[-1])

        for node in nodes:
            self.assertIs(node.prev.next, node)
            self.assertIs(node.next.prev, node)

        if expected_values is not None:
            self.assertEqual(self._values_forward(d), expected_values)
            self.assertEqual(self._values_backward(d), list(reversed(expected_values)))

    def test_empty(self):
        """D1: 新创建的链表 - len=0，dummy.prev 和 dummy.next 都指向自身"""
        d = DLList()
        self.assertEqual(len(d), 0)
        self.assertIs(d.dummy.next, d.dummy)
        self.assertIs(d.dummy.prev, d.dummy)
        self._assert_integrity(d, [])

    def test_add_first_one(self):
        """D2: 头部加一个元素 - len=1，该节点同时是 dummy.next 和 dummy.prev"""
        d = DLList()
        a = DLNode("a")
        d.add_first(a)
        self.assertEqual(len(d), 1)
        self.assertIs(d.dummy.next, a)
        self.assertIs(d.dummy.prev, a)
        self._assert_integrity(d, ["a"])

    def test_add_last_one(self):
        """D3: 尾部加一个元素 - len=1，该节点同时是 dummy.next 和 dummy.prev"""
        d = DLList()
        a = DLNode("a")
        d.add_last(a)
        self.assertEqual(len(d), 1)
        self.assertIs(d.dummy.next, a)
        self.assertIs(d.dummy.prev, a)
        self._assert_integrity(d, ["a"])

    def test_add_first_multiple(self):
        """D4: 头部加多个元素（1,2,3） - 顺序为 3→2→1"""
        d = DLList()
        for v in [1, 2, 3]:
            d.add_first(DLNode(v))
        self.assertEqual(len(d), 3)
        self._assert_integrity(d, [3, 2, 1])

    def test_add_last_multiple(self):
        """D5: 尾部加多个元素（1,2,3） - 顺序为 1→2→3"""
        d = DLList()
        for v in [1, 2, 3]:
            d.add_last(DLNode(v))
        self.assertEqual(len(d), 3)
        self._assert_integrity(d, [1, 2, 3])

    def test_dummy_prev_after_add_first(self):
        """D6: 多次 add_first 后 - dummy.prev 指向尾部节点"""
        d = DLList()
        nodes = [DLNode(v) for v in [1, 2, 3]]
        for node in nodes:
            d.add_first(node)
        self.assertIs(d.dummy.prev, nodes[0])
        self._assert_integrity(d, [3, 2, 1])

    def test_dummy_next_after_add_first(self):
        """D7: 多次 add_first 后 - dummy.next 指向头部节点"""
        d = DLList()
        nodes = [DLNode(v) for v in [1, 2, 3]]
        for node in nodes:
            d.add_first(node)
        self.assertIs(d.dummy.next, nodes[2])
        self._assert_integrity(d, [3, 2, 1])

    def test_dummy_prev_after_add_last(self):
        """D8: 多次 add_last 后 - dummy.prev 指向最后添加的元素"""
        d = DLList()
        nodes = [DLNode(v) for v in [1, 2, 3]]
        for node in nodes:
            d.add_last(node)
        self.assertIs(d.dummy.prev, nodes[2])
        self._assert_integrity(d, [1, 2, 3])

    def test_dummy_next_after_add_last(self):
        """D9: 多次 add_last 后 - dummy.next 指向第一个添加的元素"""
        d = DLList()
        nodes = [DLNode(v) for v in [1, 2, 3]]
        for node in nodes:
            d.add_last(node)
        self.assertIs(d.dummy.next, nodes[0])
        self._assert_integrity(d, [1, 2, 3])

    def test_prev_pointers(self):
        """D10: 添加元素后，检查每个节点的 prev - prev 指向前一个节点（或 dummy）"""
        d = DLList()
        n1, n2, n3 = DLNode(1), DLNode(2), DLNode(3)
        d.add_last(n1)
        d.add_last(n2)
        d.add_last(n3)

        self.assertIs(d.dummy.next, n1)
        self.assertIs(n1.prev, d.dummy)
        self.assertIs(n2.prev, n1)
        self.assertIs(n3.prev, n2)
        self.assertIs(d.dummy.prev, n3)
        self._assert_integrity(d, [1, 2, 3])

    def test_next_pointers(self):
        """D11: 添加元素后，检查每个节点的 next - next 指向后一个节点（或 dummy）"""
        d = DLList()
        n1, n2, n3 = DLNode(1), DLNode(2), DLNode(3)
        d.add_last(n1)
        d.add_last(n2)
        d.add_last(n3)

        self.assertIs(n1.next, n2)
        self.assertIs(n2.next, n3)
        self.assertIs(n3.next, d.dummy)
        self._assert_integrity(d, [1, 2, 3])

    def test_prev_next_symmetry(self):
        """D12: 随机添加后 - node.prev.next == node 且 node.next.prev == node"""
        rng = random.Random(123)
        d = DLList()
        ref = []
        for i in range(200):
            if rng.random() < 0.5:
                d.add_first(DLNode(i))
                ref.insert(0, i)
            else:
                d.add_last(DLNode(i))
                ref.append(i)
        self._assert_integrity(d, ref)

    def test_remove_first_one(self):
        """D13: 单元素链表 remove_first - 链表变空，dummy 指向自身"""
        d = DLList()
        a = DLNode("a")
        d.add_first(a)
        removed = d.remove_first()
        self.assertIs(removed, a)
        self.assertEqual(len(d), 0)
        self.assertIs(d.dummy.next, d.dummy)
        self.assertIs(d.dummy.prev, d.dummy)
        self._assert_integrity(d, [])

    def test_remove_first_multiple(self):
        """D14: 多元素链表连续 remove_first - 顺序为 FIFO（先添加的先被移除）"""
        d = DLList()
        for v in [1, 2, 3]:
            d.add_last(DLNode(v))
        out = [d.remove_first().value for _ in range(3)]
        self.assertEqual(out, [1, 2, 3])
        self._assert_integrity(d, [])

    def test_remove_last_one(self):
        """D15: 单元素链表 remove_last - 链表变空，dummy 指向自身"""
        d = DLList()
        a = DLNode("a")
        d.add_last(a)
        removed = d.remove_last()
        self.assertIs(removed, a)
        self.assertEqual(len(d), 0)
        self.assertIs(d.dummy.next, d.dummy)
        self.assertIs(d.dummy.prev, d.dummy)
        self._assert_integrity(d, [])

    def test_remove_last_multiple(self):
        """D16: 多元素链表连续 remove_last - 顺序为 LIFO（后添加的先被移除）"""
        d = DLList()
        for v in [1, 2, 3]:
            d.add_last(DLNode(v))
        out = [d.remove_last().value for _ in range(3)]
        self.assertEqual(out, [3, 2, 1])
        self._assert_integrity(d, [])

    def test_remove_alternating(self):
        """D17: 交替 remove_first 和 remove_last - 始终正确维护链表结构"""
        d = DLList()
        for v in range(6):
            d.add_last(DLNode(v))

        out = [
            d.remove_first().value,
            d.remove_last().value,
            d.remove_first().value,
            d.remove_last().value,
            d.remove_first().value,
            d.remove_last().value,
        ]
        self.assertEqual(out, [0, 5, 1, 4, 2, 3])
        self._assert_integrity(d, [])

    def test_mixed_add(self):
        """D18: 交替 add_first 和 add_last - 顺序正确"""
        d = DLList()
        d.add_last(DLNode(4))
        d.add_first(DLNode(3))
        d.add_last(DLNode(5))
        d.add_first(DLNode(2))
        d.add_last(DLNode(6))
        d.add_first(DLNode(1))
        self._assert_integrity(d, [1, 2, 3, 4, 5, 6])

    def test_add_after_remove(self):
        """D19: 移除后继续添加 - 链表结构正确"""
        d = DLList()
        d.add_last(DLNode(1))
        d.add_last(DLNode(2))
        self.assertEqual(d.remove_first().value, 1)
        self.assertEqual(d.remove_last().value, 2)
        self._assert_integrity(d, [])

        d.add_first(DLNode(10))
        d.add_last(DLNode(20))
        self._assert_integrity(d, [10, 20])

    def test_clear_sequence(self):
        """D20: 添加一批，全部移除 - 最终空链表，dummy 指向自身"""
        d = DLList()
        for v in range(10):
            d.add_last(DLNode(v))
        out = [d.remove_first().value for _ in range(10)]
        self.assertEqual(out, list(range(10)))
        self._assert_integrity(d, [])

    def test_remove_first_empty(self):
        """D21: 空链表 remove_first - 抛出 IndexError"""
        d = DLList()
        with self.assertRaises(IndexError):
            d.remove_first()

    def test_remove_last_empty(self):
        """D22: 空链表 remove_last - 抛出 IndexError"""
        d = DLList()
        with self.assertRaises(IndexError):
            d.remove_last()

    def test_after_last_remove(self):
        """D23: 移除最后一个元素后 - dummy.next == dummy.prev == dummy"""
        d = DLList()
        d.add_first(DLNode(1))
        d.remove_first()
        self.assertIs(d.dummy.next, d.dummy)
        self.assertIs(d.dummy.prev, d.dummy)
        self._assert_integrity(d, [])

    def test_prev_next_after_remove(self):
        """D24: 移除中间节点后 - 前后节点的指针正确连接"""
        d = DLList()
        nodes = [DLNode(i) for i in range(5)]
        for node in nodes:
            d.add_last(node)

        removed_front = d.remove_first()
        removed_back = d.remove_last()

        remaining = self._nodes_forward(d)
        remaining_values = [n.value for n in remaining]
        self.assertEqual(remaining_values, [1, 2, 3])

        self.assertIs(d.dummy.next, nodes[1])
        self.assertIs(d.dummy.prev, nodes[3])

        self.assertIs(nodes[1].prev, d.dummy)
        self.assertIs(nodes[1].next, nodes[2])
        self.assertIs(nodes[2].prev, nodes[1])
        self.assertIs(nodes[2].next, nodes[3])
        self.assertIs(nodes[3].prev, nodes[2])
        self.assertIs(nodes[3].next, d.dummy)

        reachable = set(self._nodes_forward(d))
        self.assertNotIn(removed_front, reachable)
        self.assertNotIn(removed_back, reachable)
        self._assert_integrity(d, [1, 2, 3])

    def test_forward_traversal(self):
        """D25: 从 dummy.next 开始正向遍历 - 按添加顺序访问所有节点"""
        d = DLList()
        for v in [1, 2, 3]:
            d.add_last(DLNode(v))
        self.assertEqual(self._values_forward(d), [1, 2, 3])
        self._assert_integrity(d, [1, 2, 3])

    def test_backward_traversal(self):
        """D26: 从 dummy.prev 开始反向遍历 - 按相反顺序访问所有节点"""
        d = DLList()
        for v in [1, 2, 3]:
            d.add_last(DLNode(v))
        self.assertEqual(self._values_backward(d), [3, 2, 1])
        self._assert_integrity(d, [1, 2, 3])

    def test_traversal_after_operations(self):
        """D27: 混合操作后双向遍历 - 两种遍历得到的顺序互为反向"""
        d = DLList()
        d.add_last(DLNode(2))
        d.add_first(DLNode(1))
        d.add_last(DLNode(3))
        d.add_last(DLNode(4))
        d.remove_first()
        d.add_first(DLNode(0))
        d.remove_last()
        self._assert_integrity(d, [0, 2, 3])

        forward = self._values_forward(d)
        backward = self._values_backward(d)
        self.assertEqual(forward, list(reversed(backward)))

    def test_large_sequence(self):
        """D28: 大量元素添加（如 10000） - 不崩溃，链表结构正确"""
        d = DLList()
        for i in range(10000):
            d.add_last(DLNode(i))
        self.assertEqual(len(d), 10000)
        self.assertIs(d.dummy.next.prev, d.dummy)
        self.assertIs(d.dummy.prev.next, d.dummy)

        node = d.dummy.next
        for i in range(10000):
            self.assertIsNot(node, d.dummy)
            self.assertEqual(node.value, i)
            node = node.next
        self.assertIs(node, d.dummy)

    def test_random_ops(self):
        """D29: 随机混合操作 - 始终满足双向链表的对称性"""
        rng = random.Random(12345)
        d = DLList()
        ref = []
        next_value = 0

        for i in range(2000):
            if len(ref) == 0:
                if rng.random() < 0.5:
                    d.add_first(DLNode(next_value))
                    ref.insert(0, next_value)
                else:
                    d.add_last(DLNode(next_value))
                    ref.append(next_value)
                next_value += 1
            else:
                op = rng.choice(["add_first", "add_last", "remove_first", "remove_last"])
                if op == "add_first":
                    d.add_first(DLNode(next_value))
                    ref.insert(0, next_value)
                    next_value += 1
                elif op == "add_last":
                    d.add_last(DLNode(next_value))
                    ref.append(next_value)
                    next_value += 1
                elif op == "remove_first":
                    v = d.remove_first().value
                    self.assertEqual(v, ref.pop(0))
                else:
                    v = d.remove_last().value
                    self.assertEqual(v, ref.pop())

            if i % 50 == 0:
                self._assert_integrity(d, ref)

        self._assert_integrity(d, ref)

    def test_memory_leak(self):
        """D30: 大量添加删除后 - 所有被移除的节点不再被链表引用"""
        d = DLList()
        nodes = [DLNode(i) for i in range(200)]
        for node in nodes:
            d.add_last(node)

        removed = [d.remove_first() for _ in range(120)]
        reachable = set(self._nodes_forward(d))
        for node in removed:
            self.assertNotIn(node, reachable)

        while len(d) > 0:
            removed.append(d.remove_last())

        self.assertEqual(len(d), 0)
        self.assertIs(d.dummy.next, d.dummy)
        self.assertIs(d.dummy.prev, d.dummy)


if __name__ == "__main__":
    unittest.main()

