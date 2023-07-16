# You are asked with writing a method called is_valid_bst in the BinarySearchTree class that checks whether a bst is a valid bst.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree():
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
    
    def dfs_in_order(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)

            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results
    
    # The is_valid_bst method is a method of the BinarySearchTree class that checks whether the binary search tree is a valid binary search tree.
    def is_valid_bst(self):
        # Get node values of the binary search tree in ascending order
        node_values = self.dfs_in_order()

        # Iterate through the node values using a for loop
        for i in range(1, len(node_values)):
            # Check if each node value is greater than the previous node value
            if node_values[i] <= node_values[i-1]:

                # If node values are not sorted in ascending order, the binary
                # search tree is not valid, so return Fasle
                return False
            
            # IF all node values are sorted in ASC order, the binary search tree
            # is a valid binary search tree, so return True
            return True





my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print("BST is valid")
print(my_tree.is_valid_bst())

# Note: Implementation of is_valid_bst assumes that the node values in the binary search tree are unique.
        # If the binary search tree contains duplicate node values, the is_valid_bst method may return incorrect results.