# Swap the values of the firsr and last node
#[Note: The pointers to the nodes themselves are not swapped - only their values are excahnged]

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
    
    def swap_first_last(self):

        # Check if the list is empty or has only one node
        if self.head is None or self.head == self.tail:

            return # If either of these conditions is true, then the method returns without doing anything.
        # if the linked list has at least two nodes, then the method swaps the values of the first and last nodes using tuple assignment.

        # Swap the values of the head and tail nodes [Note: The tuple > (self.tail.value, self.head.value) represents the values of the last and first node, respectively. The values are swaped by setting the tuple to(self.head.value, self.tail.value)]
        self.head.value, self.tail.value = self.tail.value, self.head.value

        # After the values are swaped, the method exits. 
        








my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)

print('DLL before swap_first_last():')
my_doubly_linked_list.print_list()

my_doubly_linked_list.swap_first_last()

print('\nDLL after swap_first_last():')
my_doubly_linked_list.print_list()

# my_doubly_linked_list.print_list()