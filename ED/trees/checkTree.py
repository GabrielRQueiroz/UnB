class BynaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def checkForSearchBinaryTree(root):
    if root is None:
        return False
    if root.left is not None and root.left.data > root.data:
        return False
    if root.right is not None and root.right.data < root.data:
        return False
    if not checkForSearchBinaryTree(root.left) or not checkForSearchBinaryTree(root.right):
        return False
    return True
