import unittest
from Stack import Stack


class MyTestCase(unittest.TestCase):
    """
        Test cases for Stack class
    """

    def setUp(self):
        self.stack = Stack()
        self.stack.push("John")
        self.stack.push("Fred")
        self.stack.push("Tim")

    def test_peek(self):
        """
            Test the peek() method to see if it returns correctly
        :return: first Node object in the stack
        """
        self.assertEqual(self.stack.peek(), "Tim")  # add assertion here

    def test_push(self):
        self.stack.push("Joe")
        self.assertEqual(self.stack.peek(), "Joe")

    def test_pop(self):
        self.stack.pop()
        self.assertEqual(self.stack.peek(), "Fred")


if __name__ == '__main__':
    unittest.main()
