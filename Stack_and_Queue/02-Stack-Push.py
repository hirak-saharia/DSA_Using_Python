class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        # self.bottom = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

# Implement the push method for the Stack class that adds a new node with a given value to the top of the stack.

    def push(self, value):
        new_node = Node(value)

        # Check if the height of the stack is zero:
        if self.height == 0:
            # If it is : set the top node to the new_node
            self.top = new_node
        
        # If the height of the stack is not zero
        else:
            # Set the next attribute of the new_node to the current to the current top node.
            new_node.next = self.top

            # Set the top node to the new_node.
            self.top = new_node

            # Increase the height of the stack by one.
            self.height += 1
            


my_stack = Stack(2)
my_stack.push(1)

my_stack.print_stack()