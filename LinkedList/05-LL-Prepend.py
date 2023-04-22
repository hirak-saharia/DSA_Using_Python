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
    
    def pop(self, value):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -=1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value):
        new_node = Node(value) #created a new Node with the given value
        if self.length == 0: #Check if the Linked List is empty

            #Set the head and tail attributes to the new node
            self.head = new_node 
            self.tail = new_node
        else:
            # Set the next attributes to the new Node to the current Node
            new_node.next = self.head
            self.head = new_node # Update the head attribute to the new node
        self.length +=1 # Increment the length attribute of the LinkedList
        return True #Return True to indicate a successfull operation
        




my_linked_list = LinkedList(2)
my_linked_list.append(3)

# my_linked_list.prepend(1)
# my_linked_list.print_list()

print('Before prepend():')
print('---------------')
print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length, '\n')
print('Linked List:')
my_linked_list.print_list()

my_linked_list.prepend(1)

print('\n\nAfter prepend():')
print('---------------')
print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length, '\n')
print('Linked List:')
my_linked_list.print_list()
