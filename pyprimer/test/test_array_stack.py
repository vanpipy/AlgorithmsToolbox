import unittest
from unittest import mock
from src import ArrayStack


class TestArrayStack(unittest.TestCase):
    def test_push_pop_order(self):
        s = ArrayStack()
        self.assertEqual(len(s), 0)
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(len(s), 3)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)
        self.assertEqual(len(s), 0)

    def test_resize_growth(self):
        s = ArrayStack()
        for i in range(50):
            s.push(i)
        self.assertEqual(len(s), 50)
        self.assertEqual(s.pop(), 49)
        self.assertEqual(s.pop(), 48)

    def test_get_set(self):
        s = ArrayStack()
        for i in range(5):
            s.push(i)
        self.assertEqual(s.get(0), 0)
        self.assertEqual(s.get(4), 4)
        s.set(2, 99)
        self.assertEqual(s.get(2), 99)
        self.assertIsNone(s.get(5))
        with self.assertRaises(IndexError):
            s.set(5, 100)
        with self.assertRaises(IndexError):
            s.set(-1, 100)

    def test_pop_empty_raises(self):
        s = ArrayStack()
        with self.assertRaises(IndexError):
            s.pop()

    def test_resize_invocation_push_and_pop(self):
        s = ArrayStack()
        with mock.patch.object(s, "resize", wraps=s.resize) as spy:
            for i in range(100):
                s.push(i)
            first = spy.call_count
            self.assertGreater(first, 0)
            for _ in range(90):
                s.pop()
            self.assertGreater(spy.call_count, first)

    def test_no_resize_on_single_push(self):
        s = ArrayStack()
        with mock.patch.object(s, "resize", wraps=s.resize) as spy:
            s.push(42)
            self.assertEqual(spy.call_count, 0)

    def test_resize_under_alternating_ops(self):
        s = ArrayStack()
        with mock.patch.object(s, "resize", wraps=s.resize) as spy:
            for i in range(30):
                s.push(i)
                if i % 3 == 0:
                    s.pop()
            self.assertGreater(spy.call_count, 0)

if __name__ == "__main__":
    unittest.main()
