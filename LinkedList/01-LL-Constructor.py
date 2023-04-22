# Define the node class for a singly linked list
class Node:
    # Constructor for the Node class
    def __init__(self,value):
        # Set the value attribute for the node
        self.value = value
        # Initialize the next attribute to None
        self.next = None 

# Define the LInkedList class
class LinkedList:
    # Constructor for the LinkedList class
    def __init__(self,value):
        new_node = Node(value) # Create a new Node with the given value
        self.head = new_node # Set the head attribute to the new Node
        self.tail = new_node # Set the tail attribute to the new Node
        self.length = 1 # Initialized the lenght attribute to 1

my_linked_list = LinkedList(4)

print("head:", my_linked_list.head.value)
print("tail:", my_linked_list.head.value)
print("length:", my_linked_list.head.value)