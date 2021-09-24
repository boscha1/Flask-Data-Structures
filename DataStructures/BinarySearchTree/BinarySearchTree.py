class Node:
    def __init__(self, current_node=None):
        self.current_node = current_node
        self.left_node = None
        self.right_node = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
