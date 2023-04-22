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
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1

    def pop(self): 
        if self.length ==0: # Check if the list is empty
            return None
        # Initialize temp and pre to the head
        temp = self.head
        pre = self.head
        # Iterate until the last node
        while(temp.next):
            pre = temp
            temp = temp.next
        # Set the new tail to the previous node
        self.tail = pre
        self.tail.next = None # Remove link to the remove node
        self.length -=1 # Decrement list length by 1
        if self.length == 0: # Again check if the list is now empty
            # Set head and tail to Node
            self.head = None
            self.tail = None
        return temp #return the node that we just removed.
        #return temp.value

my_linked_list = LinkedList(1)
my_linked_list.append(2)

#my_linked_list.print_list()

# (2) Items - Returns 2 Node
print(my_linked_list.pop().value)

# (1) Item - Returns 1 Node
print(my_linked_list.pop().value)

# (0) Items - Returns None
print(my_linked_list.pop())




# there are two self.length == 0; >> which the one on top is if we started with zero. > self.length +=1
# And the other one we just added is when we started with one item > self.length -=1