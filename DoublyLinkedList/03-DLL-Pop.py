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
        self.length +=1
        return True
        
        return True
    
    # Implementing POP method for node One and Two

    def pop(self):
        if self.length == 0: # Situation 1: When we have zero item in the list.
            return None
        temp = self.tail # Since we're going to return it, we need to have a variable pointing to it will call temp.
        if self.length == 1: # Situation 2: When we have 1 item in the list
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev # When we have two or more items in the list.
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp





my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)

# my_doubly_linked_list.print_list()

# (2) Items - Returns 2 Node
print(my_doubly_linked_list.pop().value)

# (1) Item - Returns 1 Node
print(my_doubly_linked_list.pop().value)

# (0) Item - Return None
print(my_doubly_linked_list.pop())


# The method Pop() should perform the following tasks:
  
     #1. If the list is empty (i.e., the length is 0), return None.
     #2. Store a reference to the current tail node in a temporary variable.
     #3. If the list has only one node(i.e., the length is 1), set both the head and tail of the list to None.

     #4. If the list has more than one node, perform the following steps:
          
           #a. Update the tail of the list to be the previous node of the current tail.
           #b. Set the next attribute of the new tail node to None.
           #c. Set the prev attribute of the removed node(stored in the temporary variable) to None.

    #5. Decrement the length attribute of the list by 1.
    #6. Return the removed node (stored in the temporary variable).
         