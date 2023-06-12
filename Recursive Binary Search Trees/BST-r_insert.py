# Implement a recursive method called r_insert to insert a value into a binary search tree. The method should maintain the BST properly, where the left subtree contains only nodes with the values less than the parent node's value, and the right contains only nodes with the values greater than the parent node's value. No duplicate values are allowed in the BST.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None


    
    def __r_insert(self, current_node, value):

        # If current_node is None, we have reached a leaf node and insert a new node with the given value
        if current_node == None:
            return Node(value)
        
        # If the value is less than the value of the current_node, we insert the value into the left subtree
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)

        # If the value is greater than the value of the current_node, we insert the value into the right subtree
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)

        # Return the modified current_node after inserting the value
        return current_node
    


    def r_insert(self, value):
        # If the tree is empty, create a new node and make it the root node.
        if self.root == None:
            self.root = Node(value)

        # Call the private helper method __r_insert with the root node and the value to be inserted
        self.__r_insert(self.root, value)







my_tree = BinarySearchTree()

my_tree.r_insert(2)
my_tree.r_insert(1)
my_tree.r_insert(3)

print('Root:', my_tree.root.value)
print('Root -> Left:', my_tree.root.left.value) 
print('Root -> Right:', my_tree.root.right.value) 


# Explanation of the provided code:

    # The r_insert method and its helper method __r_insert are used to insert values into a BST using recursive approach.

        # 1. __r_insert method: This is private method for the r_insert method. It takes two arguments - the current node and the value to be inserted. The method is recursive and works as follows:

            # a. If the current node is None, it means the value can be inserted at this position. A new node with the given value is created and returned.
            # b. If the value is less than the current node's value, the method is called recursively on the left child of the current node.
            # c. If the value is greater than the current node's value, the method is called recursively on the right child of the current node.
            # d. Finally, the current node is returned

        # 2. r_insert method: This is the public method to insert a value  into the BST. 
            # a. If the root is None, it creates a new node with the given value and sets it as the root.
            # b. Then  it calls the __r_insert helper method with the root and the value as arguments