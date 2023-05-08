# We'll run enqueue to add a second node with a value of 2 and then will print this out and we should get one and two.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # Define a function called "enqueu" with an input called "value"
    def enqueue(self, value):
        # Create a new node with the given value and store it in a variable called "new_node".
        new_node = Node(value)
        
        # Check if the first node is None(list is empty)
        if self.first is None:
            # Set the first and last nodes to the new_node.
            self.first = new_node
            self.last = new_node

        # If the first node is not None(list is not empty)
        else:
            # Set the next attribute of the last node to the new_node.
            self.last.next = new_node
            # Set the last node to the new_node.
            self.last = new_node
        
        # Increase the length of the list by one.
        self.length += 1





my_queue = Queue(1)

my_queue.enqueue(2)

my_queue.print_queue()


