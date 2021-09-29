import unittest
from HashTable import HashTable


class MyTestCase(unittest.TestCase):
    """
        Test cases for HashTable class
    """

    def setUp(self):
        self.hash_table = HashTable(10)
        self.hash_table.add_key_value("title", "This is a title")
        self.hash_table.add_key_value("body", "This is the body of a post")

    def test_get_value(self):
        self.assertEqual(self.hash_table.get_value("title"), "This is a title")
        self.assertEqual(self.hash_table.get_value("body"), "This is the body of a post")
        self.assertNotEqual(self.hash_table.get_value("title"), "This is the body of a post")


if __name__ == '__main__':
    unittest.main()
