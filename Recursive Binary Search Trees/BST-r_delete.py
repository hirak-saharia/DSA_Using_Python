# Write two Python Functions for the BinarySearchTree class: delete_node and __delete_node
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree():
    def __init__(self):
        self.root = None

    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node
    
    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root, value)
    
    def min_value(self, current_node):
        while (current_node.left is not None):
            current_node = current_node.left
        return current_node.value
    

    def __delete_node(self, current_node, value):

        # Return None if the current node is None
        if current_node == None:
            return None
        
        # Traverse the left subtree if value is smaller
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)

        # Traverse the right subtree if value is larger
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)

        # If value is found, delete the node
        else:

            # Case 1: No children, return None to delete
            if current_node.left == None and current_node.right == None:
                return None
            
            # Case 2: No left child, return right child
            elif current_node.left == None:
                current_node = current_node.right

            # Case 3: No right child, return left child
            elif current_node.right == None:
                current_node = current_node.left

            # Case 4: Two children, find min in right subtree
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)

        # Return the current node after deletion
        return current_node
     
    def delete_node(self, value):
        # Call the helper method to delete the node
        # You may see other implementations that write it this way:
        #self.__delete_node(self.root, value)
        # but that way will not work when removing the root node
        self.root = self.__delete_node(self.root, value)





my_tree = BinarySearchTree()

my_tree.r_insert(2)
my_tree.r_insert(1)
my_tree.r_insert(3)

print('Root:', my_tree.root.value)
print('Root -> Left:', my_tree.root.left.value) 
print('Root -> Right:', my_tree.root.right.value) 


my_tree.delete_node(2)

print("\nroot:", my_tree.root.value)
print("root.left =", my_tree.root.left.value)
print("root.right =", my_tree.root.right)


# Note:
    # This case implements a binary search tree, which is a bst data structure where each node has at most two child nodes, arranged in a way that the value of the node to the left is less than or equal to the parent node, and the value of the node to the right is greater than or equal to the parent node.

    # The delete_node method is a public method to delete a node with a given value from the BST.

    # The actual deletion logic is implemented in the private method __delete_node.

    # The logic of the __delete_node method is as follows:
        # 1. If the current node is empty(None), it means the node with the given vlaue is not found, so return None.

        # 2. If the value to delete is less than the current node's value, search in the left subtree.

        # 3. If the value to delete is greater than the current node's value, search in the right subtree.

        # 4. If the value to delete is to the current node's value, we found the node to delete. There are three cases:

            # a. If the node has no children, remove the node by returning None.

            # b. If the node has only a left child or only a right children, remove the node by returning the existing child.

            # c. If the node has both childen, find the minimum value in the right subtree, replace the current node'd value with that minimum value, and then delete the minimum value node in the right subtree.



# The reason we use self.root = self.__delete_node(self.root, value) instead of sel.__delete_node(self.root, value) is to update the tree's root node after deletion.

# This is necessary if the root node is the one being deleted or if its value is replaced with the minimum value from its right subtree.

# By assigning the result of self.__delete_node(self.root, value) to self.root, we ensure that the root node is updated accordingly, maintaining the integrity of the tree structure.