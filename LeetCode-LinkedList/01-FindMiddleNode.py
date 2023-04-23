# Implement the find_middle_node method for the LinkedList class.
# The find_middle_node method should return the middle node in the linked list without using the length attribute.
# If the linked list has an even number of nodes, retuen the first node of second half of the list.

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        # self.length = 1

    # def print_list(self):
    #     temp = self.hea
    #     while temp is not None:
    #         print(temp.value)
    #         temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
        
        # else:
        #     self.tail.next = new_node
        #     self.tail = new_node
        #     self.length +=1

    def find_middle_node(self):
        # Initialize two pointers to the head of the list
        slow = self.head
        fast = self.head
        
        # Traverse the list with the fast pointer moving twice
        # as fast as the slow pointer
        while fast is not None and fast.next is not None:
            slow = slow.next # Move slow pointer one step
            fast = fast.next.next # Move fast pointer two steps

        # When the fast pointer reaches the end, the slow pointer will be at the middle node   
        return slow
    



my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print(my_linked_list.find_middle_node().value )


# my_linked_list.print_list()


# Keep in mind the following requirements:
    #1. The method should use a two-pointer approach, where one pointer (slow) moves one node at a time and the pointer (fast) moves two nodes at a time.
    #2. When the fast pointer reaches the end of the list or has no next node, the slow pointer should be at the middle node of the list.
    #3. The method should return the middle node or the fist node of the second half of the list of the list has an even number of noded.