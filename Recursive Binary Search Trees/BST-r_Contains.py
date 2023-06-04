# Implement the r_contains method of the BinarySearchTree class. This method should recursively search the binar search tree for a given value, starting from the root node, and return True if the value is found, and False otherwise.

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
                temp.left = new_node
                return True
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right


    # The r_contains method takes a value as input and it calls the private method __r_contains with the root node(current_node) of the tree and the value as arguments.
    def __r_contains(self, current_node, value):

        # If current_node is None, we have reached a leaf node and the value is not present in the tree.
        if current_node == None:

            return False
    
        # If the value matches the value of the current_node, we have found the value and return True
        if value == current_node.value:

            return True
    
        # If the value is less than the value of the current_node, we recurse on the left subtree.
        if value < current_node.value:

            return self.__r_contains(current_node.left, value)
    
        # If the value is greater than the value of the current_node, we recurse on the right subtree.
        if value > current_node.value:

            return self.__r_contains(current_node.right, value)
    

    # The r_contains method returns the output of the __r_contains method
    def r_contains(self, value):
         
         # The r_contains method calls the private helper method __r_contains
         # With the root node of the tree and the value to search for.
         # It returns the output of __r_contains.
         return self.__r_contains(self.root, value)



my_tree = BinarySearchTree()

my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print('BST Contains 27:')
print(my_tree.r_contains(27))

print('\nBST Contains 17:')
print(my_tree.r_contains(17))


# For normal Binary Search Tree
# print('Root:', my_tree.root.value)
# print('Root->Left:', my_tree.root.left.value)
# print('Root->Right:', my_tree.root.right.value)