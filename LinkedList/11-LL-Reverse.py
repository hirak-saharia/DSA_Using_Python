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


    def reverse(self):

        # Swap the head and tail pointers
        temp = self.head # Created a temp variable to swap
        self.head = self.tail
        self.tail = temp

        # Initialize variables : after and before for the next & previous nodes
        after = temp.next
        before = None

        # Iterate through the list to reverse the next pointers.
        for _ in range(self.length):
            # Store the next node in the list
            after = temp.next
            # Update the current nodes next pointer to the previous node
            temp.next = before
            # Move the previous node to the current nodes.
            before = temp
            # Move the current node to the next node in the list
            temp = after








my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

my_linked_list.reverse()

my_linked_list.print_list()


# Why Reverse method is import?

    # The reverse method should reverse the the order of the nodes in the linked list so that the head becomes the tail and the tail becomes the head.

    # The method should not create any new noded or modify the values of the nodes.

    # The method should only update the next attribute of each node to point to the previous node in the list.

# Consider the following requirements while implementing the method:
  
   # 1. The method should handle edge cases, such as an empty list or a list with a single node.
   # 2. The method should utilize a temporary variable to swap the head and tail attributes of the LinkedList class.
   # 3. THe method should use a loop to interate through the nodes in the list and update the next attribute of each node.
   # 4. The method should not modify the length of the LinkedList class.