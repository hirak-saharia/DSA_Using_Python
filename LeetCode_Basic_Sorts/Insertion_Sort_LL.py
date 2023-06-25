# Write an insertion_sort() method in the LinkedList class that will sort the elements of a linked list in ascending order using the insertion sort algorithm.

    # The method should update the head and tail pointers of the linked list to reflect the new order of the nodes in the list.

        # You can assume that the input list will contain only integers. You should not use any additional data structures to sort the linked list.

# Input: The LinkedList object containing a linked list with unsorted elements(self)

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
        self.length += 1

   
    
    def insertion_sort(self):
        # check if the length of the list less than 2, if it is, then the list is already sorted, and the function returns.
        if self.length < 2:
            return
       
       # set the pointer to the first element of the sorted_list, 
        sorted_list_head = self.head
        # set the pointer to the second element of the unsorted_list to pointing to next node after the head
        unsorted_list_head = self.head.next
        # sorted_list_head pointer is then disconnected from the rest of the list by setting its next attribute to None.
        sorted_list_head.next = None
       

       # The function enters a while loop where it iterates through each remaining node in the unsorted part of the list. For each node:
        while unsorted_list_head is not None:
            # save the current element
            current = unsorted_list_head

            # move the pointer to the next element in the unsorted list
            unsorted_list_head = unsorted_list_head.next
           
           # Insert the current element into the sorted list
            if current.value < sorted_list_head.value:
                # if the current element is smaller than the first element
                # in the sorted list, it becomes the new first element
                current.next = sorted_list_head
                sorted_list_head = current
            
            else:
                # otherwise, search for the appropriate position to insert the current element
                # the function searches through the sorted part of the list to find the correct position to insert the current node.
                # The search is done using the search_pointer variable, which initially points to the sorted_list_head node.
                # The search_pointer variable is moved along the sorted part of list until it reaches the last node that is smaller than the current node, 
                # or until it reached the end of the sorted part of the list.
                # Once the correct position is found, the current node is inserted into the sorted part of the list.
                search_pointer = sorted_list_head
                while search_pointer.next is not None and current.value > search_pointer.next.value:
                    search_pointer = search_pointer.next
                current.next = search_pointer.next
                search_pointer.next = current
       
       # update the head and tail of the list
        self.head = sorted_list_head
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        self.tail = temp
       



my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.insertion_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()