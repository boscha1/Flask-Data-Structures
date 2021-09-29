class Node:
    def __init__(self, current_node=None, next_node=None):
        self.current_node = current_node
        self.next_node = next_node


class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self, table_size):
        self.table_size = table_size
        self.hash_table = [None] * table_size

    def custom_hash(self, key):
        hash_value = 0
        for i in key:
            hash_value += ord(i)
            hash_value = (hash_value * ord(i)) % self.table_size
        return hash_value

    def add_key_value(self, key, value):
        hashed_key = self.custom_hash(key)
        if self.hash_table[hashed_key] is None:
            self.hash_table[hashed_key] = Node(Data(key, value), None)
        else:
            # if a collision occurs
            node = self.hash_table[hashed_key]
            while node.next_node:
                node = node.next_node

            node.next_node = Node(Data(key, value), None)

    def get_value(self, key):
        hashed_key = self.custom_hash(key)
        if self.hash_table[hashed_key] is not None:
            node = self.hash_table[hashed_key]
            if node.next_node is None:
                return node.current_node.value
            while node.next_node:
                if key == node.current_node.key:
                    return node.current_node.value
                node = node.next_node

            if key == node.current_node.key:
                return node.current_node.value
        return None

    def print_table(self):
        print("{")
        for i, val in enumerate(self.hash_table):
            if val is not None:
                llist_string = ""
                node = val
                if node.next_node:
                    while node.next_node:
                        llist_string += (
                            str(node.current_node.key) + " : " + str(node.current_node.value) + " --> "
                        )
                        node = node.next_node
                    llist_string += (
                        str(node.current_node.key) + " : " + str(node.current_node.value) + " --> None"
                    )
                    print(f"    [{i}] {llist_string}")
                else:
                    print(f"    [{i}] {val.current_node.key} : {val.current_node.value}")
            else:
                print(f"    [{i}] {val}")
        print("}")
