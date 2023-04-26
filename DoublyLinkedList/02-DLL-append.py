class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # Implement append for DublyLinkedList
    # We're going to initialize the link list with a node with the value of one and we'll append another node. So the link list will contain one and two.

    def append(self, value):
        # Create a new node with the given value
        new_node = Node(value)

        # Check if the list is empty (head is None)
        if self.head is None:
            # Set head and tail to the new node
            self.head = new_node
            self.tail = new_node

        
        else:
            # Connect the new node to the end of the list
            self.tail.next = new_node
            # Connect the new node to the previous node
            new_node.prev = self.tail
            # Update the tail to point to the new Node
            self.tail = new_node
            # Increment the length of the list
            self.length +=1
        # Return True to indicate success
        return True




my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.print_list()