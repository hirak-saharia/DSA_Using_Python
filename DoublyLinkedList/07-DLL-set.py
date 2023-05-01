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
            self.head = None
            self.tail = None

        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.length += 1
            return True
        
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp
    
    # Define a function called "set_value" with inputs "index" and "value"
    def set_value(self,index,value): 

        # Get the node at the specified index and store it in a temporary variable called temp
        temp = self.get(index)

        # Check if "temp" exists (Not None): 
        if temp:

            # If temp exists, set the value attribute of "temp" to the input value. return true.
            temp.value = value

            return True
        
        # If "temp" does not exist, return false
        return False

        

my_doubly_linked_list = DoublyLinkedList(11)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(23)
my_doubly_linked_list.append(7)

my_doubly_linked_list.set_value(1,4)
my_doubly_linked_list.print_list()
