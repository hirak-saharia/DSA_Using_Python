# Append a value of 2 with 1

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
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
        new_node = Node(value) # Created a new node with the given value
        if self.length == 0: # Check to if the linked list empty

            # Point both haed and tail at the new node
            self.head = new_node
            self.tail = new_node
        else:
            # Point the next pointer of the last node of the new node
            self.tail.next = new_node
            self.tail = new_node
        # Increment the length of the linked list by 1
        self.length +=1


my_linked_list = LinkedList(1)
# print("Head:", my_linked_list.head.value)
# print("Tail:", my_linked_list.head.value)
# print("Length:", my_linked_list.head.value)

my_linked_list.append(2)

my_linked_list.print_list()