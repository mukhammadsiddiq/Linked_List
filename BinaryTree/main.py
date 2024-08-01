from function import *

tree = Treenode(10)
tree.insert(5)
tree.insert(4)
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(22)
tree.insert(11)
tree.insert(22)
tree.preorder()
print(tree.find(11))
print(tree.find(43))