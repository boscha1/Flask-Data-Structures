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
        """
        self.assertEqual(self.stack.peek(), "Tim")  # add assertion here

    def test_push(self):
        """
            Test the push() method to see if a new node is inserted at the beginning
            of the stack
        """
        self.stack.push("Joe")
        self.assertEqual(self.stack.peek(), "Joe")

    def test_pop(self):
        """
            Test the pop() method to see if the first node in the stack is deleted
        """
        self.stack.pop()
        self.assertEqual(self.stack.peek(), "Fred")


if __name__ == '__main__':
    unittest.main()
