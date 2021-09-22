class Node:
    def __init__(self, current_node=None, next_node=None):
        self.current_node = current_node
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

