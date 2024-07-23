class Node:
    def __init__(self, data):
        self.data = data  # Initialize the node with data
        self.next = None  # Set the next pointer to None


class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the linked list as None

    def print_list(self):
        # Print all nodes in the linked list
        temp = self.head  # Start from the head
        while temp:  # Traverse until the end of the list
            print(temp.data)  # Print the data of each node
            temp = temp.next  # Move to the next node

    def push(self, new_data):
        # Insert a new node at the beginning of the linked list
        new_data = Node(new_data)  # Create a new node with the given data
        new_data.next = self.head  # Point the new node's next to the current head
        self.head = new_data  # Update the head to the new node

    def insert(self, prev, newdata):
        # Insert a new node after the given previous node
        if prev is None:
            print("Not exist")  # If the previous node doesn't exist, print an error message
            return  # Exit the function
        new_node = Node(newdata)  # Create a new node with the given data
        new_node.next = prev.next  # Point the new node's next to the previous node's next
        prev.next = new_node  # Update the previous node's next to the new node

    def append(self, new_data):
        # Append a new node at the end of the linked list
        new_data = Node(new_data)  # Create a new node with the given data
        if self.head is None:
            self.head = new_data  # If the list is empty, set the new node as the head
            return
        last = self.head  # Start from the head
        while last.next:  # Traverse to the last node
            last = last.next  # Move to the next node
        last.next = new_data  # Point the last node's next to the new node

    def delete(self, key):
        # Delete the first occurrence of the node with the given key
        temp = self.head  # Start from the head
        if temp is None:
            return  # If the list is empty, exit the function
        if temp and temp.data == key:
            self.head = temp.next  # If the head node is the one to be deleted, update the head
            temp = None  # Free the old head node
            return
        prev = None  # Initialize the previous node as None
        while temp and temp.data != key:
            prev = temp  # Keep track of the previous node
            temp = temp.next  # Move to the next node
        if temp is None:
            return  # If the key is not found, exit the function
        prev.next = temp.next  # Update the previous node's next to skip the deleted node
        temp = None  # Free the node to be deleted
