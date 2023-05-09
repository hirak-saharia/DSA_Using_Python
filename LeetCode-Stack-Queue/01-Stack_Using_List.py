# Implement Stack Using a List of a linked list
  # Create a constructor for class Stack that implement a new stack with an empty list.

class Node:
    def __init__(self, value):
        self.vlaue = value
        self.next = None

class Stack:
    def __init__(self):
        self.stack_list = []


