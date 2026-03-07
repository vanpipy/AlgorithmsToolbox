import unittest
from src.ArrayQueue import ArrayQueue


class TestArrayQueue(unittest.TestCase):
    def test_empty_queue(self):
        q = ArrayQueue(4)
        self.assertEqual(len(q), 0)
        with self.assertRaises(IndexError):
            q.remove()

    def test_add_one(self):
        q = ArrayQueue(4)
        q.add(1)
        self.assertEqual(len(q), 1)

    def test_add_remove_one(self):
        q = ArrayQueue(4)
        q.add("a")
        v = q.remove()
        self.assertEqual(v, "a")
        self.assertEqual(len(q), 0)

    def test_add_multiple(self):
        q = ArrayQueue(4)
        q.add(1)
        q.add(2)
        q.add(3)
        self.assertEqual(q.remove(), 1)
        self.assertEqual(q.remove(), 2)
        self.assertEqual(q.remove(), 3)
        self.assertEqual(len(q), 0)

    def test_remove_until_empty(self):
        q = ArrayQueue(3)
        for i in range(3):
            q.add(i)
        for _ in range(3):
            q.remove()
        with self.assertRaises(IndexError):
            q.remove()

    def test_wrap_around(self):
        q = ArrayQueue(3)
        q.add(1)
        q.add(2)
        q.add(3)
        self.assertEqual(q.remove(), 1)
        q.add(4)
        self.assertEqual(q.remove(), 2)
        self.assertEqual(q.remove(), 3)
        self.assertEqual(q.remove(), 4)

    def test_remove_wrap(self):
        q = ArrayQueue(4)
        for i in range(3):
            q.add(i)
        q.remove()
        q.remove()
        q.add(3)
        q.add(4)
        self.assertEqual(q.remove(), 2)
        self.assertEqual(q.remove(), 3)
        self.assertEqual(q.remove(), 4)

    def test_full_cycle(self):
        q = ArrayQueue(5)
        for i in range(5):
            q.add(i)
        vals = [q.remove() for _ in range(5)]
        self.assertEqual(vals, [0, 1, 2, 3, 4])
        self.assertEqual(len(q), 0)
        q.add(99)
        self.assertEqual(q.remove(), 99)

    def test_interleaved_ops(self):
        q = ArrayQueue(5)
        q.add(1)
        q.add(2)
        q.remove()
        q.add(3)
        q.add(4)
        q.remove()
        q.add(5)
        out = [q.remove(), q.remove(), q.remove()]
        self.assertEqual(out, [3, 4, 5])

    def test_add_to_full_fixed(self):
        q = ArrayQueue(2)
        q.add(1)
        q.add(2)
        with self.assertRaises(OverflowError):
            q.add(3)

    def test_large_capacity(self):
        q = ArrayQueue(10**6)
        q.add(1)
        self.assertEqual(q.remove(), 1)

    def test_order_preserved(self):
        q = ArrayQueue(16)
        for i in range(8):
            q.add(i)
        out = [q.remove() for _ in range(8)]
        self.assertEqual(out, list(range(8)))

    def test_no_data_corruption(self):
        q = ArrayQueue(8)
        for i in range(8):
            q.add(i)
        q.remove()
        q.remove()
        q.add(8)
        q.add(9)
        out = [q.remove() for _ in range(8)]
        self.assertEqual(out, [2, 3, 4, 5, 6, 7, 8, 9])

    def test_alternating_add_remove(self):
        q = ArrayQueue(4)
        ref = []
        for i in range(20):
            if len(ref) < 4 and (i % 2 == 0):
                q.add(i)
                ref.append(i)
            else:
                if ref:
                    self.assertEqual(q.remove(), ref.pop(0))


if __name__ == "__main__":
    unittest.main()
