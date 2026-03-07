import random
import unittest
from unittest import mock
from src.DynamicArrayQueue import DynamicArrayQueue


class TestDynamicArrayQueue(unittest.TestCase):
    def test_empty_queue(self):
        q = DynamicArrayQueue(4)
        self.assertEqual(len(q), 0)
        self.assertIsNone(q.remove())

    def test_add_one(self):
        q = DynamicArrayQueue(4)
        q.add(1)
        self.assertEqual(len(q), 1)

    def test_add_remove_one(self):
        q = DynamicArrayQueue(4)
        q.add("a")
        v = q.remove()
        self.assertEqual(v, "a")
        self.assertEqual(len(q), 0)

    def test_add_multiple(self):
        q = DynamicArrayQueue(4)
        q.add(1)
        q.add(2)
        q.add(3)
        self.assertEqual(q.remove(), 1)
        self.assertEqual(q.remove(), 2)
        self.assertEqual(q.remove(), 3)
        self.assertEqual(len(q), 0)

    def test_remove_until_empty(self):
        q = DynamicArrayQueue(3)
        for i in range(3):
            q.add(i)
        for _ in range(3):
            q.remove()
        self.assertIsNone(q.remove())

    def test_wrap_around(self):
        q = DynamicArrayQueue(3)
        q.add(1)
        q.add(2)
        q.add(3)
        self.assertEqual(q.remove(), 1)
        q.add(4)
        self.assertEqual(q.remove(), 2)
        self.assertEqual(q.remove(), 3)
        self.assertEqual(q.remove(), 4)

    def test_remove_wrap(self):
        q = DynamicArrayQueue(4)
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
        q = DynamicArrayQueue(5)
        for i in range(5):
            q.add(i)
        vals = [q.remove() for _ in range(5)]
        self.assertEqual(vals, [0, 1, 2, 3, 4])
        self.assertEqual(len(q), 0)
        q.add(99)
        self.assertEqual(q.remove(), 99)

    def test_interleaved_ops(self):
        q = DynamicArrayQueue(5)
        q.add(1)
        q.add(2)
        q.remove()
        q.add(3)
        q.add(4)
        q.remove()
        q.add(5)
        out = [q.remove(), q.remove(), q.remove()]
        self.assertEqual(out, [3, 4, 5])

    def test_resize_on_add(self):
        q = DynamicArrayQueue(4)
        with mock.patch.object(q, "resize", wraps=q.resize) as spy:
            for i in range(100):
                q.add(i)
            self.assertGreater(spy.call_count, 0)
            for i in range(100):
                self.assertEqual(q.remove(), i)

    def test_resize_factor(self):
        q = DynamicArrayQueue(4)
        with mock.patch.object(q, "resize", wraps=q.resize) as spy:
            for i in range(5):
                q.add(i)
            self.assertGreaterEqual(spy.call_count, 1)
            args, _ = spy.call_args
            scale = args[0] if args else 2
            self.assertGreaterEqual(scale, 1.5)

    def test_resize_with_wrap(self):
        q = DynamicArrayQueue(4)
        for i in range(3):
            q.add(i)
        q.remove()
        for i in range(3, 10):
            q.add(i)
        out = [q.remove() for _ in range(len(q))]
        self.assertEqual(out, list(range(1, 10)))

    def test_multiple_resizes(self):
        q = DynamicArrayQueue(2)
        with mock.patch.object(q, "resize", wraps=q.resize) as spy:
            for i in range(200):
                q.add(i)
            self.assertGreaterEqual(spy.call_count, 2)
            for i in range(200):
                self.assertEqual(q.remove(), i)

    def test_shrink_on_remove(self):
        q = DynamicArrayQueue(4)
        for i in range(60):
            q.add(i)
        with mock.patch.object(q, "resize", wraps=q.resize) as spy:
            for _ in range(55):
                q.remove()
            self.assertGreater(spy.call_count, 0)

    def test_shrink_factor(self):
        q = DynamicArrayQueue(32)
        for i in range(24):
            q.add(i)
        with mock.patch.object(q, "resize", wraps=q.resize) as spy:
            for _ in range(20):
                q.remove()
            self.assertGreaterEqual(spy.call_count, 1)
            args, _ = spy.call_args
            scale = args[0] if args else 0.5
            self.assertLessEqual(scale, 0.5)

    def test_shrink_with_wrap(self):
        q = DynamicArrayQueue(8)
        for i in range(6):
            q.add(i)
        for _ in range(3):
            q.remove()
        for i in range(6, 20):
            q.add(i)
        with mock.patch.object(q, "resize", wraps=q.resize) as spy:
            for _ in range(15):
                q.remove()
            self.assertGreater(spy.call_count, 0)

    def test_no_shrink_when_not_needed(self):
        q = DynamicArrayQueue(16)
        for i in range(12):
            q.add(i)
        with mock.patch.object(q, "resize", wraps=q.resize) as spy:
            for _ in range(2):
                q.remove()
            self.assertEqual(spy.call_count, 0)

    def test_shrink_to_one(self):
        q = DynamicArrayQueue(8)
        for i in range(8):
            q.add(i)
        with mock.patch.object(q, "resize", wraps=q.resize) as spy:
            for _ in range(8):
                q.remove()
            self.assertGreater(spy.call_count, 0)
        self.assertIsNone(q.remove())

    def test_remove_empty(self):
        q = DynamicArrayQueue(4)
        self.assertIsNone(q.remove())

    def test_large_capacity(self):
        q = DynamicArrayQueue(10**6)
        q.add(1)
        self.assertEqual(q.remove(), 1)

    def test_order_preserved(self):
        q = DynamicArrayQueue(16)
        for i in range(8):
            q.add(i)
        out = [q.remove() for _ in range(8)]
        self.assertEqual(out, list(range(8)))

    def test_no_data_corruption(self):
        q = DynamicArrayQueue(8)
        for i in range(8):
            q.add(i)
        q.remove()
        q.remove()
        q.add(8)
        q.add(9)
        out = [q.remove() for _ in range(8)]
        self.assertEqual(out, [2, 3, 4, 5, 6, 7, 8, 9])

    def test_alternating_add_remove(self):
        rng = random.Random(42)
        q = DynamicArrayQueue(2)
        ref = []
        for _ in range(200):
            op = rng.choice(["add", "remove"])
            if op == "add":
                v = rng.randint(-1000, 1000)
                q.add(v)
                ref.append(v)
            else:
                if ref:
                    self.assertEqual(q.remove(), ref.pop(0))
                else:
                    self.assertIsNone(q.remove())


if __name__ == "__main__":
    unittest.main()
