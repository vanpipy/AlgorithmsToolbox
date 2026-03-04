import random
import unittest
from unittest import mock
from src import ArrayStack


class TestArrayStack(unittest.TestCase):
    def test_empty_stack(self):
        s = ArrayStack()
        self.assertEqual(len(s), 0)
        with self.assertRaises(IndexError):
            s.pop()

    def test_push_one(self):
        s = ArrayStack()
        s.push("a")
        self.assertEqual(len(s), 1)
        self.assertEqual(s.get(0), "a")

    def test_push_pop_one(self):
        s = ArrayStack()
        s.push("x")
        v = s.pop()
        self.assertEqual(v, "x")
        self.assertEqual(len(s), 0)

    def test_push_multiple(self):
        s = ArrayStack()
        for i in range(5):
            s.push(i)
        self.assertEqual(len(s), 5)
        self.assertEqual(s.pop(), 4)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)
        self.assertEqual(s.pop(), 0)
        self.assertEqual(len(s), 0)
        with self.assertRaises(IndexError):
            s.pop()

    def test_pop_until_empty(self):
        s = ArrayStack()
        for i in range(3):
            s.push(i)
        for _ in range(3):
            s.pop()
        self.assertEqual(len(s), 0)
        with self.assertRaises(IndexError):
            s.pop()

    def test_get_invalid_index(self):
        s = ArrayStack()
        for i in range(3):
            s.push(i)
        self.assertIsNone(s.get(-1))
        self.assertIsNone(s.get(len(s)))

    def test_set_invalid_index(self):
        s = ArrayStack()
        for i in range(3):
            s.push(i)
        with self.assertRaises(IndexError):
            s.set(-1, 10)
        with self.assertRaises(IndexError):
            s.set(len(s), 10)

    def test_pop_empty(self):
        s = ArrayStack()
        with self.assertRaises(IndexError):
            s.pop()

    def test_resize_on_push(self):
        s = ArrayStack()
        with mock.patch.object(s, "resize", wraps=s.resize) as spy:
            for i in range(100):
                s.push(i)
            self.assertGreater(spy.call_count, 0)
            for i in range(100):
                self.assertEqual(s.get(i), i)

    def test_resize_factor(self):
        s = ArrayStack()
        with mock.patch.object(s, "resize", wraps=s.resize) as spy:
            for i in range(64):
                s.push(i)
            self.assertGreater(spy.call_count, 0)
            for i in range(64):
                self.assertEqual(s.get(i), i)

    def test_multiple_resizes(self):
        s = ArrayStack()
        with mock.patch.object(s, "resize", wraps=s.resize) as spy:
            for i in range(256):
                s.push(i)
            self.assertGreaterEqual(spy.call_count, 2)
            for i in range(256):
                self.assertEqual(s.get(i), i)

    def test_shrink_on_pop(self):
        s = ArrayStack()
        for i in range(200):
            s.push(i)
        with mock.patch.object(s, "resize", wraps=s.resize) as spy:
            for _ in range(180):
                s.pop()
            self.assertGreater(spy.call_count, 0)
        self.assertEqual(len(s), 20)
        for i in range(20):
            self.assertEqual(s.get(i), i)

    def test_shrink_factor(self):
        s = ArrayStack()
        for i in range(60):
            s.push(i)
        with mock.patch.object(s, "resize", wraps=s.resize) as spy:
            for _ in range(50):
                s.pop()
            self.assertGreater(spy.call_count, 0)
        self.assertEqual(len(s), 10)

    def test_no_shrink_when_not_needed(self):
        s = ArrayStack()
        for i in range(30):
            s.push(i)
        with mock.patch.object(s, "resize", wraps=s.resize) as spy:
            for _ in range(5):
                s.pop()
            self.assertEqual(spy.call_count, 0)

    def test_shrink_to_one(self):
        s = ArrayStack()
        for i in range(10):
            s.push(i)
        with mock.patch.object(s, "resize", wraps=s.resize) as spy:
            for _ in range(10):
                s.pop()
            self.assertGreater(spy.call_count, 0)
        self.assertEqual(len(s), 0)

    def test_set_updates_value(self):
        s = ArrayStack()
        for i in range(5):
            s.push(i)
        s.set(3, 777)
        self.assertEqual(s.get(3), 777)

    def test_push_after_pop(self):
        s = ArrayStack()
        for i in range(5):
            s.push(i)
        for _ in range(3):
            s.pop()
        s.push(100)
        s.push(200)
        self.assertEqual(s.pop(), 200)
        self.assertEqual(s.pop(), 100)
        self.assertEqual(s.pop(), 1)
        self.assertEqual(s.pop(), 0)
        with self.assertRaises(IndexError):
            s.pop()

    def test_random_ops(self):
        rng = random.Random(123)
        s = ArrayStack()
        ref = []
        for _ in range(500):
            op = rng.choice(["push", "pop", "set", "get"])
            if op == "push":
                val = rng.randint(-1000, 1000)
                s.push(val)
                ref.append(val)
                self.assertEqual(len(s), len(ref))
            elif op == "pop":
                if len(ref) == 0:
                    with self.assertRaises(IndexError):
                        s.pop()
                else:
                    v1 = s.pop()
                    v2 = ref.pop()
                    self.assertEqual(v1, v2)
                    self.assertEqual(len(s), len(ref))
            elif op == "set":
                if len(ref) == 0:
                    with self.assertRaises(IndexError):
                        s.set(0, 0)
                else:
                    i = rng.randrange(len(ref))
                    val = rng.randint(-1000, 1000)
                    s.set(i, val)
                    ref[i] = val
                    self.assertEqual(s.get(i), ref[i])
            else:
                if len(ref) == 0:
                    self.assertIsNone(s.get(0))
                else:
                    i = rng.randrange(len(ref))
                    self.assertEqual(s.get(i), ref[i])


if __name__ == "__main__":
    unittest.main()
