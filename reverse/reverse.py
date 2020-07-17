class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, next=None):
        self.next = next
        return self

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        self.head is None or node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True
            print(current.get_value())
            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if prev is not None:
            node.value, prev.value = (prev.value, node.value)
        node is None or node.next is None or self.reverse_list(node.next, node)
