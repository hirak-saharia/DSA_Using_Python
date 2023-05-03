# Run an insert method to insert at the index of one, a node with the value of two............
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
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
        return True
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
               temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
            return temp
        

    def insert(self, index, value):
        if index < 0 or index > self.length: 
            return False
        
        if index == 0: 
            return self.prepend(value) # call prepend function with the input value 
        
        if index == self.length:
            return self.append(value) # call append function with the input value
        
        # Adding the node 2 at somewhere in the middle of the list, to do that, will create a new node:
        new_node = Node(value)
        # Get the node before the specified index and store it in a variable called "before".
        before = self.get(index - 1)
        # Get the next node of "before" and store it in a variable called "afetr".
        after = before.next

        # Update the pointers of the new_node and its neighboring nodes:  
        new_node.prev = before # set the previous attribute of new_node to "before"
        new_node.next = after # set the next attribute of new_node to "after".
        before.next = new_node # set the next attribute of "before" to new_node.
        after.prev = new_node # set the previous attribute of "after" to new_node.
        self.length += 1 # increase the length of the list by one.
        return True





    

my_dll = DoublyLinkedList(1)
my_dll.append(3)

print('DLL before insert():')
my_dll.print_list()

my_dll.insert(1,2)

print('\nDLL after insert(2) in the middle:')
my_dll.print_list()

my_dll.insert(0,0)

print('\nDLL after insert(4) at beginning:')
my_dll.print_list()

my_dll.insert(4,4)

print('\nDD after insert(4) at the end:')
my_dll.print_list()

# my_dll.print_list()
