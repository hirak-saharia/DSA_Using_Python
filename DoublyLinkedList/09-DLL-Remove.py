class Node:
    def __init__(self,value):
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
            self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.head == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length -1, index, -1):
                temp = temp.prev
        return temp
    

    def remove(self, index):
        # If the given index is out of bounds
        if index < 0 or index >= self.length:
            return None
        # Remove first item from the list - call the pop_first method and return its results.
        if index == 0:
            return self.pop_first()
        
        # Remove an item from the end of the list 
        if index == self.length - 1:
            return self.pop()
        
        # Remove the item 2 of the the index 1 - call the get method with the given index to retrieve the node to be removed, and store the result in a temporary variable call - temp.
        temp = self.get(index)

        # Update the prev attribute of the temp.next node and the next attribute of the temp.prev node to remove node temp from the list.
        temp.next.prev = temp.prev
        temp.prev.next = temp.next

        # Set the next and prev attribute of the temp node to temp node to None
        temp.next = None
        temp.prev = None

        # Decrement the length attribute of the list by 1
        self.length -= 1
        # Return the removed node (i.e., the temp variable)
        return temp.value




my_dll = DoublyLinkedList(0)
my_dll.append(1)
my_dll.append(2)

print(my_dll.remove(1), '\n')

my_dll.print_list()