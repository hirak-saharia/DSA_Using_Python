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
    
    def pop(self):
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
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1
        return True
    
    def pop_first(self):
        #Check if the list is empty
        if self.length == 0:
            return None
        
        #save a reference to the current head node
        temp = self.head

        #Update the head to the second node in the list
        self.head = self.head.next

        #Disconnect the removed node from the list
        temp.next = None

        #Decrease the length of the list by 1
        self.length -=1

        #Check if the list is now empty
        if self.length == 0:
            #set the tail to None if the list is empty
            self.tail = None

        # Return the removed node
        return temp

    



my_linked_list = LinkedList(2)
my_linked_list.append(1)

# print(my_linked_list.head.value)
# print(my_linked_list.tail.value)


# (2) Items - Returns 2 Node
print(my_linked_list.pop_first().value)

# (1) Item - Returns 1 Node
print(my_linked_list.pop_first().value)

# (0) Items - Returns None
print(my_linked_list.pop_first())

