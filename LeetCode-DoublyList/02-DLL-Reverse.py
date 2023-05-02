# Create a new method called reverse that reverses the order of the nodes in the list, i.e., the first node becomes the last node, the second node becomes the second-to-last node, and so on.

class Node:
    def __init__(self, value):
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


    def reverse(self):
        temp = self.head # create a temp variable and setting it to the head of the list.
        while temp is not None:
            # Swap the prev and next pointers of node points to
            temp.prev, temp.next, = temp.next, temp.prev
            
            # move to the next node
            temp = temp.prev

        # swap the head and tail pointers
        self.head, self.tail = self.tail, self.head





my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)

my_doubly_linked_list.reverse()

my_doubly_linked_list.print_list()



#[Note: Inside the while loop, we swap the prev and next pointers of the current node by using Python's tuple packing and unpacking syntax. We assign the value of temp.next to temp.prev and the value of temp.prev to temp.next, effectively swapping the two pointers.
  # We then update the value of temp to be the previous node (which is now the next node in the original list). We do this by setting temp to temp.prev.
 # We repeat this process until we have traveresd the entire list(i.e., temp to None), at which point we have effectively reversed the list.]