class Node:
    # Constructor with the value of the node as the argument
    def __init__(self, value):
        # Set the value of node
        self.value = value
        # Set the left child to None
        self.left = None
        # Set the right child to None
        self.right = None

class BinarySearchTree:
    # Constructor for the binary search tree
    def __init__(self):
        # Set the root of the tree to None, indicating that the tree is initially empty.
        self.root = None


my_tree = BinarySearchTree()

print(my_tree.root)