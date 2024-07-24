from function import Node, Stack

stack = Stack()
stack.head = Node('Yanvar')
stack.push('Fevral')
stack.push('Mart')
stack.pop()
result = stack.pop()
stack.pop()
stack.pop()
stack.pop()
print(stack.is_empty())

