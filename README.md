# LinkedList and Stack Implementation in Python
This repository contains a basic implementation of a singly linked list in Python. The linked list supports several common operations including insertion, deletion, and traversal. Moreover, A stack is a Last In, First Out (LIFO) data structure where elements are added and removed from the top of the stack.

# Linked List Classes
## Node
The Node class represents an individual element in the linked list.

# Stack Class
# The Stack class provides the following methods to interact with the stack:

## push(new_data): Adds new_data to the top of the stack.
## pop(): Removes the top element from the stack. Returns a message if the stack is empty.
## is_empty(): Checks if the stack is empty. Returns a boolean value.
## is_full(): Checks if the stack is full. Always returns "Stack is empty" since the stack implementation is dynamic.
## peek(): Returns the data of the top element without removing it. Returns a message if the stack is empty.
## size(): Returns the number of elements in the stack. Returns a message if the stack is empty.

# Attributes:
## data: Stores the value of the node.
## next: Pointer to the next node in the linked list.
# Methods:
__init__(self, data): Initializes the node with the given data and sets the next pointer to None.
# LinkedList
The LinkedList class manages the entire linked list and provides methods to manipulate it.

# Attributes:
## head: Pointer to the first node in the linked list.
# Methods:
## __init__(self): Initializes the linked list with the head set to None.
## print_list(self): Traverses the linked list and prints the data of each node.
## push(self, new_data): Inserts a new node with the given data at the beginning of the linked list.
## insert(self, prev, newdata): Inserts a new node with the given data after the specified previous node.
## append(self, new_data): Appends a new node with the given data at the end of the linked list.
## delete(self, key): Deletes the first occurrence of the node with the given key.

# Notes
## The is_full() method is included but does not serve a practical purpose in this dynamic stack implementation. It always indicates that the stack is empty.
## The pop() method does not return the removed value. It only updates the stack's head. You may want to modify it to return the value of the removed node if needed.
