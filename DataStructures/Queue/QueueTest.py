import unittest
from Queue import Queue


class MyTestCase(unittest.TestCase):
    """
        Test cases for Queue class
    """

    def setUp(self):
        self.queue = Queue()
        self.queue.enqueue("John")
        self.queue.enqueue("Fred")
        self.queue.enqueue("Tim")
        self.queue.enqueue("Jim")
        self.queue.enqueue("Tony")

    def test_enqueue(self):
        """
            Test the enqueue() method to ensure the node is inserted at the
            end of the queue
        """
        self.queue.enqueue("Joe")
        self.assertEqual(self.queue.tail.data, "Joe")  # add assertion here

    def test_dequeue(self):
        """
            Test the dequeue() method removes the node at the beginning of the
            queue
        """
        self.queue.dequeue()
        self.assertEqual(self.queue.head.data, "Fred")


if __name__ == '__main__':
    unittest.main()
