LinkedList Implementation in Python
This repository contains a basic implementation of a singly linked list in Python. The linked list supports several common operations including insertion, deletion, and traversal.

Classes
Node
The Node class represents an individual element in the linked list.

Attributes:
data: Stores the value of the node.
next: Pointer to the next node in the linked list.
Methods:
__init__(self, data): Initializes the node with the given data and sets the next pointer to None.
LinkedList
The LinkedList class manages the entire linked list and provides methods to manipulate it.

Attributes:
head: Pointer to the first node in the linked list.
Methods:
__init__(self): Initializes the linked list with the head set to None.
print_list(self): Traverses the linked list and prints the data of each node.
push(self, new_data): Inserts a new node with the given data at the beginning of the linked list.
insert(self, prev, newdata): Inserts a new node with the given data after the specified previous node.
append(self, new_data): Appends a new node with the given data at the end of the linked list.
delete(self, key): Deletes the first occurrence of the node with the given key.
