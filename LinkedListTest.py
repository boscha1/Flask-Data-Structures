import unittest
from LinkedList import LinkedList, Node


class MyTestCase(unittest.TestCase):
    """
        Test cases for LinkedList class
    """
    def test_print_linked_list(self):
        """
            Given an input file containing integer values, and the integer value 8,
            test that the my_search method correctly returns the index 6 verifying
            that 8 is in the list.
        """
        linked_list = LinkedList()

        node3 = Node("data3", None)
        node2 = Node("data2", node3)
        node1 = Node("data1", node2)

        linked_list.head = node1

        self.assertEqual(linked_list.to_string(), " data1 -> data2 -> data3 -> None")


if __name__ == '__main__':
    unittest.main()
