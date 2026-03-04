import unittest
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


if __name__ == "__main__":
    unittest.main()
