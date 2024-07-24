class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_data = Node(new_data)
        if self.head is None:
            self.head = new_data
        new_data.next = self.head
        self.head = new_data

    def pop(self):
        if self.head is None:
            return f"Stack is empty"
        temp = self.head
        self.head = self.head.next
        temp = None

    def is_empty(self):
        return True if self.head is None else f"Stack is not empty"

    def is_full(self, key):
        return True if self.head is not None else f"Stack is empty"

    def peek(self):
        if self.head is None:
            return f"Stack is empty"
        return self.head.data

    def size(self):
        if self.head is None:
            return f"Stack is empty"
        temp = self.head
        i = 1
        while temp.next:
            temp = temp.next
            i += 1
        return i

