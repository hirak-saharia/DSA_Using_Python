class Node:
    def __init__(self, value):
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
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
        return True
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
# This code defines a set_value method for a LinkedList Class.
# The purpose of this method is to update the value of the node at the specified index in the linked list.

    def set_value(self, index, value):

        # Call the "get" method to find the node at the specified index
        temp = self.get(index)

        # Check if a valid node was found at the specified index
        if temp:

            # Update the value of the found node with the given value
            temp.value = value

            # Return True to indicate that the value was updated successfully
            return True
        
        # If no valid node was found, return False to indicate that the value was not updated.
        return False
    

my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)

my_linked_list.set_value(1,4) #lets set the value 4 in the index 1

my_linked_list.print_list()