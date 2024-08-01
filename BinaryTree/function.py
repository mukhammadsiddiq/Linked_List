class Treenode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, new):
        if new < self.value:
            if self.left is None:
                self.left = Treenode(new)
            else:
                self.left.insert(new)
        else:
            if self.right is None:
                self.right = Treenode(new)
            else:
                self.right.insert(new)

    def inorder_traversal(self):
        if self.value is None:
            print(f"Tree is empty")
        if self.left:
            self.left.inorder_traversal()
        print(self.value)
        if self.right:
            self.right.inorder_traversal()

    def preorder(self):
        if self.value is None:
            print(f"Tree is empty")
        print(self.value)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def find(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                self.right.find(value)
        else:
            return True


