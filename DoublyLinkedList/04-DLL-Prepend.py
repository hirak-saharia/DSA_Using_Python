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

    
# 
    # Define a function called "prepend" with an input called "value"
    def prepend(self, value):
        # Create a new node ith given the value and store it in a variable called "new_node"
        new_node = Node(value)
    
        # Situation 1: when we dont have any items in DLL
        if self.length == 0: # check if the length of the list is zero. If it is :

            # set head and tail poniting to the new node
            self.head = new_node
            self.tail = new_node

        # Situation 2: when we have an items in the DLL or if the if the length of the list is greater than zero:
        else:
            # Set the next (attribute) of the new_node pointer to the current head node that is pointing to:
            new_node.next = self.head
            # Set the previous attribute of the current head node to the new_node:
            self.head.prev = new_node
            # set the head node to the new_node
            self.head = new_node
        
        # Increase the length of the list by 1
        self.length += 1
        return True


my_doubly_linked_list = DoublyLinkedList(2)
my_doubly_linked_list.append(3)

my_doubly_linked_list.prepend(1)

my_doubly_linked_list.print_list()