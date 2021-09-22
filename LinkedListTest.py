import unittest
from LinkedList import LinkedList, Node


class MyTestCase(unittest.TestCase):
    """
        Test cases for LinkedList class
    """

    def setUp(self):
        self.linked_list = LinkedList()

        self.node3 = Node("John", None)
        self.node2 = Node("Fred", self.node3)
        self.node1 = Node("Tim", self.node2)

        self.linked_list.head = self.node1

    def test_to_string(self):
        """
            Test the to_string() method to see if it displays the list correctly
        """
        self.assertEqual(self.linked_list.to_string(), " Tim -> Fred -> John -> None")

    def test_insert_head(self):
        """
            Test the insert_head() method to see if a new node is inserted at
            the beginning of the LinkedList
        """
        self.linked_list.insert_head("Joe")
        self.assertEqual(self.linked_list.to_string(), " Joe -> Tim -> Fred -> John -> None")

    def test_insert_tail(self):
        """
            Test the insert_tail() method to see if a new node is inserted at
            the end of the LinkedList
        """
        self.linked_list.insert_tail("Joe")
        self.assertEqual(self.linked_list.to_string(), " Tim -> Fred -> John -> Joe -> None")


if __name__ == '__main__':
    unittest.main()
