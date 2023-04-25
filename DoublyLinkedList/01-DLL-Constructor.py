class Node:
    def __init__(self, value):

        # Store node value
        self.value = value

        # Reference to next node
        self.next = None

        # Reference to previuos node
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):

        # Create a new node with value
        new_node = Node(value)

        # Set head to the new_node
        self.head = new_node

        # Set tail to the new_node
        self.tail = new_node

        # Set initial length to 1
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_doubly_linked_list = DoublyLinkedList(7)
my_doubly_linked_list.print_list()
