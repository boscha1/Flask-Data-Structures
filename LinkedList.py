class Node:
    def __init__(self, current_node=None, next_node=None):
        self.current_node = current_node
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def to_string(self):
        ll_string = ""
        node = self.head
        if node is None:
            return None
        while node:
            ll_string += f" {str(node.current_node)} ->"
            node = node.next_node
        ll_string += " None"
        return ll_string

    def insert_head(self, data):
        if self.head is None:
            self.head = Node(data, None)
            self.tail = self.head
            return

        new_node = Node(data, self.head)
        self.head = new_node

    def insert_tail(self, data):
        if self.head is None:
            self.insert_head(data)
            return

        self.tail.next_node = Node(data, None)
        self.tail = self.tail.next_node
