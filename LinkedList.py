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
