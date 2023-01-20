class ArvoreBinaria:
    def __init__(self, dado, esq=None, dir=None):
        self.dado = dado
        self.esq = esq
        self.dir = dir

def checkForSimmetry(root):
    if not root:
        return True
    return isMirrorred(root.esq, root.dir)
            
def isMirrorred(leftNode, rightNode):
    if leftNode is None and rightNode is None:
        return True
    if leftNode is not None and rightNode is not None:
        if leftNode.dado == rightNode.dado:
            return (isMirrorred(leftNode.esq, rightNode.dir) and
                    isMirrorred(leftNode.dir, rightNode.esq))
    return False