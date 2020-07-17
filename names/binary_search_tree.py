"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.hash = self.__hash__(value)
        self.left = self.right = None

    def __hash__(self, s):
        return sum([ord(c) for c in s])
    # Insert the given value into the tree
    def insert(self, value):
        hash = self.__hash__(value)
        return self._insert_(hash, value)

    def _insert_(self, hash, value):
        side = "left" if hash < self.hash else "right"
        node = getattr(self, side)
        return node is None and not setattr(self, side, BSTNode(value)) or node._insert_(hash, value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        hash = self.__hash__(target)
        return self._contains_(hash, target)

    def _contains_(self, hash, target):
        side = "left" if hash < self.hash else "right"
        node = getattr(self, side)
        return self.value == target or (
        node is not None and (node.value == target or node._contains_(hash, target)))
