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

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    

    
    def pop_first(self):
        if self.length == 0: # If the list is empty (i.e., the length is 0)
            return None
        temp = self.head # Store a reference to the current head node in a temporary variable

        # If the list has only one node(i.e., the length is 1)
        if self.head == 1: 

            # Set head and tail of the list to None
            self.head = None
            self.tail = None
        
        # If the list has more than one node
        else:
            # Update the head of the list to be next node of the current head
            self.head = self.head.next
            # Set the prev attribute of the new head node to None
            self.head.prev = None
            # Set the next attribute of the removed node(stored in the temporary variable) to None.
            temp.next = None
        
        # Decrement the length attribute of the list by 1
        self.length -= 1
        # Returned the removed node(stored in the temporary variable)
        return temp

        




my_doubly_linked_list = DoublyLinkedList(2)
my_doubly_linked_list.append(1)

# # (2) Items - Returns 2 or more Nodes
print(my_doubly_linked_list.pop_first().value)

# # (1) Item - Returns 1 Nodes
print(my_doubly_linked_list.pop_first().value)

# # (0) Item - Return None
print(my_doubly_linked_list.pop_first())

# my_doubly_linked_list.print_list()
