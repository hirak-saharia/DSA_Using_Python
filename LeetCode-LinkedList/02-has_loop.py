# Write a method called has_loop that is part of the linked list class.
# The method should be able to detect if there is a cycle or loop present in the linked list.
# The method shold utilize Floyd's cycle-finding alogorithm, also known as the "tortoise and here" algorithm, to determine the presence of a loop efficently.

# The method should follow these guidelines:

   #1. Create two pointers, slow and fast, both initially pointing to the head of the linked list.
   #2. Traverse the with the slow pointer moving one step at a time, while the fast pointer moves two step at a time.
   #3. If there is a loop in the list, the fast pointer will evantually meet the slow pointer. If this occurs, the method should return True.
   #4. If the fast pointer reaches the end of the list or encounters a None value, it means there is no loop in the list. In this case, the method should return False.



# ---------------------//------------------------

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
    
    # Using has_loop
    def has_loop(self):
        # Initilaize slow and fast pointer to head
        slow = self.head
        fast = self.head
        
        # Iterate while fast and fast.next are not None
        while fast is not None and fast.next is not None:
            # Move slow pointer one step forward
            slow = slow.next
            # Move fast pointer two step forward
            fast = fast.next.next

            # Check if slow and fast pointer are equal # Or if any point, slow and fast pointers become equal, that means there is a cycle in the linked list. In this case, the method returns True.
            if slow == fast:
                return True # loop found

        # If the loop ends without finding a cycle(i.e., the fast pointer reaches the end of the list), the method return False, indicating that the linked list does not have a loop.    
        return False # loop not found
    

my_linked_list_1= LinkedList(1)
my_linked_list_1.append(2)
my_linked_list_1.append(3)
my_linked_list_1.append(4)
my_linked_list_1.tail.next = my_linked_list_1.head
print(my_linked_list_1.has_loop()) # Return True

# my_linked_list_1.print_list()


my_linked_list_2= LinkedList(1)
my_linked_list_2.append(2)
my_linked_list_2.append(3)
my_linked_list_2.append(4)
print(my_linked_list_2.has_loop())  # Return False