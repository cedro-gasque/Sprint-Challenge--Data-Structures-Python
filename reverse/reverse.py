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

    def set_head(self, node):
        self.head = node

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
            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if node is None:
            self.set_head(prev)
        else:
            next = node.get_next()
            node.set_next(prev)
            self.reverse_list(next, node)
