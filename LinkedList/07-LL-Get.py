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
    





    def get(self, index):
        if index < 0 or index >= self.length: # Check if the given index is out of bounds
            return None
        temp = self.head # initialize a temporary variable to the head of the lsit
        for _ in range(index): # Traverse the lsit index times
         temp = temp.next # Move the temporary variable to the next node in the list
        return temp.value
    
my_linked_list = LinkedList(0)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

print(my_linked_list.get(3))
















