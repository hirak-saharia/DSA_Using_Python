# Implement the contains method for the BinarySearchTree class that checks if a node with a given value exists in the binary search tree.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

# Insert method
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node

        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right


# Contains method
    def contains(self, value):
        # Start at the root of the teee
        temp = self.root

        # Iterate through the tree until the node is found of the end of the tree is reached
        while temp is not None:
            # if the value is less than the current node's value, go left
            if value < temp.value:
                temp = temp.left

            # If the value is greater than the current node's value, go right
            elif value > temp.value:
                temp = temp.right
            
            # If the value matches the current node's value, return True
            else:
                return True
        
        # If the value is not found in the tree, return false
        return False





my_tree = BinarySearchTree()
# my_tree.insert(2)
# my_tree.insert(1)
# my_tree.insert(3)

# print(my_tree.root.value)
# print(my_tree.root.left.value)
# print(my_tree.root.right.value)

my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print('BST Contains 27:')
print(my_tree.contains(27))


print('BST Contains 17:')
print(my_tree.contains(17))


    