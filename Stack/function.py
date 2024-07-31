# Node class to represent each element in the stack
class Node:
    def __init__(self, data):
        self.data = data  # Data held by the node
        self.next = None  # Pointer to the next node in the stack


# Stack class to implement stack operations using linked list
class Stack:
    def __init__(self):
        self.head = None  # Initialize the stack with an empty head

    # Method to push an element onto the stack
    def push(self, new_data):
        new_data = Node(new_data)  # Create a new node with the provided data
        if self.head is None:      # If the stack is empty
            self.head = new_data   # Set the new node as the head
        new_data.next = self.head  # Link the new node to the previous head
        self.head = new_data       # Update the head to the new node

    # Method to pop an element from the stack
    def pop(self):
        if self.head is None:         # If the stack is empty
            return "Stack is empty"   # Return an empty message
        temp = self.head              # Temporarily store the current head
        self.head = self.head.next    # Move the head to the next node
        return temp.data              # Return the data of the popped node

    # Method to check if the stack is empty
    def is_empty(self):
        return True if self.head is None else "Stack is not empty"  # Return True if empty, otherwise return a message

    # Method to check if the stack is full (Note: This method is not typically used in a linked list-based stack)
    def is_full(self, key):
        return True if self.head is not None else "Stack is empty"  # Return True if the stack is not empty, otherwise return a message

    # Method to peek at the top element of the stack without removing it
    def peek(self):
        if self.is_empty():         # If the stack is empty
            return "Stack is empty" # Return an empty message
        return self.head.data       # Return the data at the head of the stack

    # Method to get the size of the stack
    def size(self):
        if self.is_empty():         # If the stack is empty
            return "Stack is empty" # Return an empty message
        temp = self.head            # Temporarily store the current head
        i = 1                       # Initialize size counter
        while temp.next:            # Traverse the stack
            temp = temp.next        # Move to the next node
            i += 1                  # Increment the size counter
        return i                    # Return the size of the stack
