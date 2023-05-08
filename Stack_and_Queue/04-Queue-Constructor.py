# Create a Queue class that represents a first-in, first-out(FIFO) data structure using a linked list implementation.

class Node:
    # __init__method that initializes the following attributes:
    def __init__(self, value):
        self.value = value # value: The value of the node.
        self.next = None # next: A reference to the next node in the list, intialized to None.

class Queue:

    # __init__ method that initialize the queue with a single node, using a given value. And it perform the below tasks:
    def __init__(self, value):
        # Create a new instance of the Node class using the provided value.
        new_node = Node(value)
        # Set first attribute of the Queue class to point to the new node.
        self.first = new_node
        # Set last attribute of the Queue class to point to the node.
        self.last = new_node
        # Initalize a length attribute for the Queue class, which represents the current of nodes in the queue, and set it to 1.
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_queue = Queue(4)

my_queue.print_queue()