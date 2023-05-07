class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        
        # Create a new instance of the Node class using the provided value.
        new_node = Node(value)

        # Set the top and bottom attribute of the Stack class to point to the new node.
        self.top = new_node
        self.bottom = new_node

        # Initialize a height attribute for the Stack class, which represents the current number of nodes in the stack, and set it to 1
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

my_stack = Stack(4)

my_stack.print_stack()