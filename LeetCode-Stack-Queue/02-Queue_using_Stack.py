# You are given a class MyQueue which implements a queue using two stacks. Your task is to implement the enqueue method which should add an element to the back of the queue.
        # To achieve this, you can use the two stack "stack1" and "stack2". Initially, all elements are stored in stack1 and stack2 is empty. In order to add an element to the back of the queue, you need to first transfer all the elements from stack1 and stack2 using a loop that pops each elements from stack1 and pushes it onto stack2.

# Once all elements have been transferrd to stack2, push the new element onto stack1. Finally, transfer all elements from stack2 back to stack1 in the same way as before, so that the queue maintains its ordering.

# Note: Your implemetation should satisfy the following constrains:
     #1. The method signature should be def enqueue(self, value).
    #2. The method should add the element value to the back of the queue.


class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, value):
        
        # Transfer all the elemets from stack1 to stack2
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())

        # Add the new element to the bottom of stack1
        self.stack1.append(value)

        # Transfer all element back from stack2 to stack1
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())

    def peek(self):
        return self.stack1[-1]
    
    def is_empty(self):
        return len(self.stack1) == 0
    
# Create a new queue
q = MyQueue()

# Enqueue some values
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Output the front of the queue
print("Front of the queue:", q.peek())

# Check if the queue is empty
print("Is the queue is empty:", q.is_empty())


# How the above code works:::
    # 1. First, code checks if stack1 has any element in it. If stack1 is not empty, the code enters a while loop.
    # 2. Inside the while loop, the code pops elements from stack1 one at time and appends them to stack2. This is done so that we can add the new element to the bottom of stack1.
    # 3. Once all elements have been transferred from the stack1 to stack2, the code appends the new element value to the bottom of stack1.
    # 4. Finally, the code enters another while loop to transfer all the elements from stack2 back to stack1 in their original order. This ensures that the queue is maintained in a First-In-First-Out(FIFO) ordering. 