class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    
class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True


    def pop(self):

        # If the stack is empty
        if self.height == 0:
            return None

        # Store a reference to the current top node in a temporary variable, "temp"
        temp = self.top

        # Update the top attribute of the Stack class to point to the next node in the stack.
        self.top = self.top.next

        # Set the next attribute of the removed node(stored in the temporary variable to None)
        temp.next = None

        # Decrement the height attribute of the Stack class by 1
        self.height -= 1

        # Return the removed node(stored in the temporary variable)
        return temp
    

    
my_stack = Stack(7)
my_stack.push(23)
my_stack.push(3)
my_stack.push(11)

# print(my_stack.pop(11), '\n')

# my_stack.print_stack()


print('Stack before pop():')
my_stack.print_stack()

print('\nPopped node:')
print(my_stack.pop().value)

print('\nStack after pop():')
my_stack.print_stack()