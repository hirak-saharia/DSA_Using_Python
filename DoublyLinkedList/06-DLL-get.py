class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

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


    
    # Implementing get() method for the the node 0,1,2,3 at the index of one, which will return the value of one. And again we'll run at the index of two, which should retunr the value of two. This is going to test to make sure that our code is working. That goes backward through our Dobuly Linked List.

    # Define a function called "get" with input "index".
    def get(self, index):

        # Check if the index is less than zero or greater than or equal to the length of the list, If it is return None
        if index < 0 or index >= self.length:
            return None
        # Set a temporary variable "temp" to the head node.
        temp = self.head
        
        # Check if the index is less than half the length of the list:a, If it is, iterate from the head node to the desired index using a for loop.
        if index < self.length/2:
            for _ in range(index):
                # Update the "temp" to the next node in each iteration
                temp = temp.next
        
        # If the index is greater than or equal to half of the length of the list:
        else:
            #a. Set "temp" to the tail node.
            temp = self.tail
            
            #b. Iterate from the tail node to the desired index using a for loop with a reverse range.
            for _ in range(self.length - 1, index, -1):
                # Update "temp" to the previous node in each iteration
                temp = temp.prev
        return temp
    





my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)

# my_doubly_linked_list.print_list()

# Get node from first half of DLL(the index of 1)
print(my_doubly_linked_list.get(1).value)

# Get node from second half of DLL(index of 2)
# print(my_doubly_linked_list.get(2))