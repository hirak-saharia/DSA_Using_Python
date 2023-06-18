# Implement a method called min_value that finds and returns the minimum value in a binary search tree starting a given node.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while(True):
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

    def min_value(self, current_node):
        # Iterate until no left child is found
        while current_node.left is not None:
            # Move to the left child of current node
            current_node = current_node.left
        
        # Return the value of the leftmost node
        return current_node.value


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.min_value(my_tree.root))
print(my_tree.min_value(my_tree.root.right))


# The method works as follows:
    # 1. It starts with a while loop that continues as long as current_node.left is not None. This means that the loop continues as long as there is a left child for the current node.

    # 2. Inside the loop, the method updates the current_node to its left child(current_node.left). It means that the method keeps traversing the left subtree of the BST to find the leftmost node.

    # 3. Once the loop ends, it means that the current_node has no left child, which implies that the current node is the leftmost node in the tree, and thus contains the minimum value.

    # 4. Finally, the method returns the value of the current node, which is the minimum value in the BST starting from the given node.