# Implement the dequeue method for the Queue class that removes the first node from the queue and returns it.

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

    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        
        else:
            self.last.next = new_node
            self.last = new_node
            self.length += 1

    def dequeue(self):
        # If the queue is empty(i.e., the length is 0)
        if self.length == 0:
            return None
        
        # Store a reference to the current first node in a temporary variable, temp
        temp = self.first
        # If the queue has only one node(i.e., the length is 1)
        if self.length == 1:
            # Set both the first and last attribute of the Queue class to None.
            self.first = None
            self.last = None
        
        # If the Queue has more than one node, peroform the following steps:
        else:
            # Set the first node to the next node of the current first node.
            self.first = self.first.next
            # Set the next attribute of the removed node (stored in a temporary variable>temp) to None.
            temp.next = None

        # Decrement the length attribute of the Queue class by 1
        self.length -= 1
        # Return the removed node(stored in the temporary variable)
        return temp.value




my_queue = Queue(1)

my_queue.enqueue(2)

# my_queue.print_queue()

# (2) Items - Return 2 Node
print(my_queue.dequeue())

# (1) Item - Return 1 Node
print(my_queue.dequeue())

# (0) Item - Return None
print(my_queue.dequeue())