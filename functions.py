class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        new_data = Node(new_data)
        new_data.next = self.head
        self.head = new_data

    def insert(self, prev, newdata):
        if prev is None:
            print("Not exist")
        newdata = Node(newdata)
        newdata.next = prev.next
        prev.next = newdata

    def append(self, new_data):
        new_data = Node(new_data)
        if self.head is None:
            self.head = new_data
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_data




    def delete(self):
        pass
