# Write a function called BFS that performs a Breadth-First Search Traversal on a Binary Tree.
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

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while(temp):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    

    def BFS(self):
        # Set the current_node to the root of the tree
        current_node = self.root

        # Create an empty queue to store nodes to visit
        results = []

        # Create an emply list to store the values of visited nodes
        queue = []

        # Add the root node to the queue
        queue.append(current_node)

        # A loop to continue untile all nodes have been visited
        while len(queue) > 0:
            # remove the first node from the queue
            current_node = queue.pop(0)

            # add the value of the visited node to the results list
            results.append(current_node.value)

            # if the visited node has a left child, add it to the queue
            if current_node.left is not None:
                queue.append(current_node.left)

            # if the visited node has a right child, add it to the queue
            if current_node.right is not None:
                queue.append(current_node.right)

        # return the list of visited node values
        return results
    

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.BFS())


# The Breadth First Search Algorithm traverses the tree level-by-level, visiting all nodes at a particular level before moving on to the next level. The BFS method in this implementation achievs this by using a queue to keep track of nodes that have been visited, but not processed, in the order they are visited.