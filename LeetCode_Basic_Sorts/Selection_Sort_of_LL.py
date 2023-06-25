# Write a selection_sort() method in the LinkedList class that will sort the elements of a linked list in ascending order using the selection sort algorithm. 
# The method should update the head and tail pointers of the linked list to reflect the new order of the nodes in the list.
# You can assume that the input linked list contain only integers.
# You should not use any additional data structures to sort the linked list.

# Input: The LinkedList object containing a linked list with unsorted elements(self).

# Output: None. The method sorts the linked list in place.

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
        
        self.length +=1

    
    def selection_sort(self):

        if self.length < 2:
            return
        
        # If the len of the LL >= 2, the method initializes a variable called current to the head of the list
        # Or start with first node as the current node
        current = self.head

        # Enters a while loop that continues until current reaches the second to the least node in the list.
        # Becoz, on each pass through the loop, the smallest unsorted element is selected and moved to the begnining of the unsorted portion of the list, so we dont need to compare it again on the next pass.
        while current.next is not None:
            # Assume the curret node has the smallest value so far
            smallest = current
            # Start with the next node as the inner current node(initializes)
            inner_current = current.next


            # Find the node with the smallest value among the remaining nodes
            # So, enters an inner while loop that contains until inner_current is None. 
            while inner_current is not None:
                # checks if the value of inner_current is smaller than the value of smallest
                if inner_current.value < smallest.value:
                    # If so, the method updates the smallest to point to inner_current
                    smallest = inner_current
                inner_current = inner_current.next
            

            # If the node with the smallest value is not current nodes
            if smallest != current:
                # If so, swaps their values using Python's tuple unpacking syntax
                current.value, smallest.value = smallest.value, current.value

            # Finally, the methods moves the current pointer to the next node in the list
            current = current.next

        # Once the while loop finished, set the tail of the linked list to the last node processed
        self.tail = current





my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.selection_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()