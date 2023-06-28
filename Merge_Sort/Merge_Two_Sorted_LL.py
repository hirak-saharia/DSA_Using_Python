# Merge two Sorted LL

# THe merge method takes an another LinkedList as an input and merges it with the current LinkedList.
# The element in both lists are assumed to be in ascending order, but the input lists themselves do not need to be sorted.

# Parameters - other_list (LinkedList): the other LinkedList to merge with the current list

# Return Value: The method does not return a value, but it modifies the current LinkedList to contain the merged list.

# Example:
        
        # l1 = LinkeList(1)
        # l1.append(3)
        # l1.append(5)
        # l1.append(7)

        # l2 = LinkedList(2)
        # l2.append(4)
        # l2.append(6)
        # l2.append(8)

        # l1.merge(12)

        # The current list (l1) now contains merged list [1,2,3,4,5,6,7,8]


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

# This code defines a method called merged that can be used on a LinkedList object to merge it with another LinkedList object(other_list).

    # Method to merge a linked list with another linked list
    def merge(self, other_list):

        # get the head node of the other linked list
        other_head = other_list.head

        # create a dummy node to hold the merged list
        dummy = Node(0)

        # set the current node to the dummy node
        current = dummy


        # loop while both list still have nodes
        while self.head is not None and other_head is not None:

            # compare the value of the first nodes in each list
            if self.head.value < other_head.value:
                # if the value in the first list is smaller,
                # add it to the current node and move to the next node in the first list

                current.next = self.head
                self.head = self.head.next

            else:
                # otherwise, add the value from the second list
                # and move to the next node in the second list
                current.next = other_head
                other_head = other_head.next

            # move the current node to the next position
            current = current.next


        # If the first list still has nodes left, add them to the current node
        if self.head is not None:
            current.next = self.head

        else:
            # If the second list still has nodes left, add them to the current node
            current.next = other_head
            # update the tail of the merged list to be the tail of the second list
            self.tail = other_list.tail


        # Set the head of merged list to the next node after the dummu node
        self.head = dummy.next

        # Update the length of the merged list
        self.length += other_list.length





l1 = LinkedList(1)
l1.append(3)
l1.append(5)
l1.append(7)

l2 = LinkedList(2)
l2.append(4)
l2.append(6)
l2.append(8)

l1.merge(l2)

l1.print_list()
# l2.print_list()


    