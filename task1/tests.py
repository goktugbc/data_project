import unittest

from task1.exceptions.EmptyStackException import EmptyStackException
from task1.exceptions.NullElementException import NullElementException
from task1.stack import Stack


class StackTester(unittest.TestCase):
    def test_size(self):
        import random

        s = Stack()
        items = random.sample(range(0, 100), random.randrange(0, 100))
        items_size = len(items)

        for item in items:
            s.push(item)

        self.assertEqual(items_size, s.size())

    def test_init_empty(self):
        s = Stack()
        self.assertTrue(s.empty())

    def test_push_pop_and_empty(self):
        s = Stack()
        s.push(1)
        s.pop()
        self.assertTrue(s.empty())

    def test_push_and_not_empty(self):
        s = Stack()
        s.push(1)
        self.assertFalse(s.empty())

    def test_push2_pop1_and_not_empty(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.pop()
        self.assertFalse(s.empty())

    def test_push_null_element(self):
        s = Stack()
        try:
            s.push(None)
        except Exception as e:
            self.assertEqual(NullElementException, type(e))

    def test_push_and_peek(self):
        s = Stack()
        s.push(1)
        self.assertEqual(1, s.peek())

    def test_push_and_size(self):
        s = Stack()
        s.push("a")
        self.assertEqual(1, s.size())

    def test_push2_and_size(self):
        s = Stack()
        s.push("a")
        s.push("b")
        self.assertEqual(2, s.size())

    def test_push2_pop1_and_size(self):
        s = Stack()
        s.push("a")
        s.push("b")
        s.pop()
        self.assertEqual(1, s.size())

    def test_peek_empty_stack(self):
        s = Stack()
        try:
            s.peek()
        except Exception as e:
            self.assertEqual(EmptyStackException, type(e))

    def test_pop_empty_stack(self):
        s = Stack()
        try:
            s.pop()
        except Exception as e:
            self.assertEqual(EmptyStackException, type(e))


if __name__ == '__main__':
    unittest.main()
