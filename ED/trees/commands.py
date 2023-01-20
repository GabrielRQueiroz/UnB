class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(val, self.root)

    def _insert(self, val, node):
        if val < node.val:
            if node.left is None:
                node.left = Node(val)
            else:
                self._insert(val, node.left)
        else:
            if node.right is None:
                node.right = Node(val)
            else:
                self._insert(val, node.right)

    def inorder(self):
        if self.root:
            return self._inorder(self.root)

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.val, end=" ")
            self._inorder(node.right)

    def preorder(self):
        if self.root:
            return self._preorder(self.root)

    def _preorder(self, node):
        if node:
            print(node.val, end=" ")
            self._preorder(node.left)
            self._preorder(node.right)

    def postorder(self):
        if self.root:
            return self._postorder(self.root)

    def _postorder(self, node):
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.val, end=" ")


bin_tree = BinarySearchTree()

while True:
    command = input()

    if command == "quack":
        break

    elif command == "pre":
        if bin_tree.root:
            bin_tree.preorder()
        print()

    elif command == "in":
        if bin_tree.root:
            bin_tree.inorder()
        print()

    elif command == "pos":
        if bin_tree.root:
            bin_tree.postorder()
        print()

    elif command.isnumeric():
        bin_tree.insert(int(command))
