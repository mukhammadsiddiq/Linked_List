from functions import Node, LinkedList

llist = LinkedList()
llist.head = Node("Monday")
tuesday = Node("Tuesday")
wednesday = Node("Wednesday")
llist.head.next = tuesday
llist.head.next.next = wednesday
llist.push("Sunday")
llist.append("Thursday")
llist.insert(llist.head.next.next, "Tuesday Evening")
print(llist.print_list())
llist.delete("Thursday")
print(llist.print_list())