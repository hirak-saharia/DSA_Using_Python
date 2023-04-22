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
    
    # Removing an item in index 2 from the LinkedList : 11 3 23 7
    def remove(self, index):
        # Check if index is out of bounds
        if index < 0 or index >= self.length:
            return None

        # Remove and return the first Node
        if index == 0:
            return self.pop_first()

        # Remove and return the last Node
        if index == self.length-1:
            return self.pop()

        # Get the previous Node
        prev = self.get(index-1)

        # Set the temp to the node to be removed
        temp = prev.next

        # Update prev.next to skip the removed node
        prev.next = temp.next

        # Disconnect the list length
        self.length -=1

        # Return the remove node
        return temp
        # return temp.value
           




my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)


print(my_linked_list.remove(2), '\n')


my_linked_list.print_list()




# Keep in mind the following requirements
   
    #1. The method should handle edge cases, such as removing a node at the begining or end of the list
    #2. The method should utilize the pop_first() and pop() methods for handling these edge cases
    #3. The method should use the get() method to find the node previous to the one to be removed.
    #4. The method should update the next attribute of the previous node to point to the node after the removed one.
    #5. The method should decrement the length attribute of the LinkedList class.
    #6. The method should return the removed node if the removal is successful.
    #7. If the index is out of bounds, the method should return None.