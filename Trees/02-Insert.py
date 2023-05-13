# Implement the insert method for the BinarySearchTree class that insert a node with a given value into the binary search tree.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        # Create a new node with the given value
        new_node = Node(value)
        # If the tree is empty, set the new node as the root
        if self.root is None:
            self.root = new_node
            return True
    
        # Set a temporary node to the root of the tree
        temp = self.root
        while (True):
            # If the value already exists in the tree, return false
            if new_node.value == temp.value:
                return False
            # If the value is less than the temporary node's value, go left
            if new_node.value < temp.value:
                # If there's no left child, insert the new node as the left child
                if temp.left is None:
                    temp.left = new_node
                    return True
                # Otherwise, continue iterating through the left subtree
                temp = temp.left
        
            # If the value is greater than the temporary node's value, go right 

            else:
                # if there's no right child, insert the new node as the right

                if temp.right is None:
                    temp.right = new_node
                    return True
            
                # Otherwise, contneu iterating through the right subtree
                temp = temp.right



my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)


print('Root:', my_tree.root.value)
print('Root->Left:', my_tree.root.left.value)
print('Root->Right:', my_tree.root.right.value)


# Result: 
# Root: 2
# Root->Left: 1
# Root->Right: 3



# The method should perform the following tasks:

    # 1. Create a new instance of the if the Node class using the provided value.

    # 2. If the binary search tree is empty(i.e., self.root is None), set the root attribute of the BinarySearchTree class to poin to the new node and return True.

    # 3. If the binary search tree is not empty, initialize a temporary variable temp to point to the root node, and then perform the following steps in a loop until the new node is inserted:

            # a. If the value of the new node is equal to the value of the current node(stored in temp), return False, indicating that duplicate values are not allowed in the tree.
            

            # b. If the value if the new node is less than the value of the current node, check if the left child of the current node is None:
                    # i - If it is, set the left child of the current node to the new node and return True.
                    # ii - If it is not, update temp to point to the left child and continue the loop.


            # c. If the value of the new node is greater than the value of the current node, check if the right child of the current node is None:
                    # i - If it is, set the right child of the current node to the new node and return True.
                    # ii - If it is not, update temp to point to the right child and continue the loop.


         