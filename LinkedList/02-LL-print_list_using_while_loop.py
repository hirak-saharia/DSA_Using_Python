def print_list(self):
    # Set a temporary pointer(temp) to the head of the list to start traversal
    temp = self.head

    # Iterate through the list until the end (temp is None)
    while temp is not None:

        # Print the value of the current node(temp)
        print(temp.value)

        # Move the temporary pointer (temp) to the next node in the list
        temp = temp.next