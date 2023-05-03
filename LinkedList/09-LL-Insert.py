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
    

    def insert(self, index, value):

        # Check if index is out of bounds
        if index < 0 or index > self.length:
            return False
    
        # If index is 0, prepend the value
        if index == 0:
            return self.prepend(value)
    
        # If index is at the end, Append the value
        if index == self.length:
            return self.append(value)
    
        # Create a new node with the value
        new_node = Node(value)

        # Get the node just before the insertion point
        temp = self.get(index-1)

        # Set new_node's next to temp's next
        new_node.next = temp.next

        # Update temp's next to temp's new_node
        temp.next = new_node

        # Increament the length of the list
        self.length +=1

        # Return True as node inderted successfully
        return True
    
my_linked_list = LinkedList(0)
my_linked_list.append(2)

my_linked_list.insert(2,1)

my_linked_list.print_list()
