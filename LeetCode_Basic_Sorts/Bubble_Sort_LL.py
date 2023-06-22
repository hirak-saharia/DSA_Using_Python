# Write a bubble_sort() method in the LinkedList class that will sort the elements of a linked list in ascending order using the bubble sort algorithm. 
#The method should update the head and tail pointers of the linked list to reflect the new order of the nodes in the list. 
#You can assume that the input linked list will contain only integers. 
#You should not use any additional data structure to sort the linked list.

# Input: The LinkList object containig a linked list with unsorted elements(self).
# Output: The method sorts the linked list in place.

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
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def bubble_sort(self):
        # check if the list has less than 2 elements
        if self.length < 2:
            return # returns without doing anything - if the list is already sorted
        
        # If the length of the LL is >= 2, initialize a variable called sorted_until to None.
        sorted_until = None

        # Continue sorting until sorted_until reaches the second node
        while sorted_until != self.head.next:
            # Initialize current pointer to head of the list
            current = self.head

            # Itereate through unsorted portion of the list until sorted_until
            while current.next != sorted_until:
                # Initialize a variable called next_node to the node after current.
                next_node = current.next

                # Swap current and next_node values if current is greater the next_node
                if current.value > next_node.value:
                    current.value, next_node.value = next_node.value, current.value
                
                # Move current pointer to next noce
                current = current.next
            
            # Update sorted_until pointer to the last node processed
            sorted_until = current





my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.bubble_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()