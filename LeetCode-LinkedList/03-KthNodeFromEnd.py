# Implement the find_kth_from_end function, which takes the LinkedList (II) and an integer k as input, and returns the k-th node from the end of the linked list WITHOUT USING LENGTH.

# [Note: If the linked list has fewer than k items, the program should return None]

# The find_kth_from_end function should follow thses requirements.
    
         #1. The function should utilize two pointers, slow and fast, initialized to the head of the linked list.
         #2. The fast pointer should moves k nodes ahead in the list.
         #3. If the fast pointer becomes None before moving k nodes, the function should return None, as the list is shorter than k nodes.
         #4. The slow and fast pointers should then move forward in the list at the same time until the fast pointer reaches the end of the list.
         #5. The function should return the slow pointer, which will be at the k-th position from the end of the list.


# ------------------------------code------------------------

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
    
    
# Let's find_kth_from_end
# taken two arguments for the function, 11 > representing the linked list and k > the position of the node to be found from the end.
# [This is a seperate function that is not a method within the LinkedList class. So, indent all the way to left]
def find_kth_from_end(self, k): 

    # Initialize both slow and fast pointers to head
    slow = fast = self.head

    # Move the fast pointer k nodes ahead
    for _ in range(k):
        if fast is None:
            return None # List is shorter than k
        fast = fast.next # Move fast pointer to the next node

    # Move slow and fast pointer until fast reaches the end
    while fast:
        slow = slow.next
        fast = fast.next

    # Return the slow pointer (k-th node from the end)
    return slow
            

    


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

# my_linked_list.print_list()

k = 3
result = find_kth_from_end(my_linked_list, k)

print(result.value)

