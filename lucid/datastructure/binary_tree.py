class Node(object):
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
        
        
class BinaryTree(object):
    def __init__(self, root) -> None:
        self.root = Node(root)


tree = BinaryTree(44)
tree.root.left = 40
tree.root.right = 43
        
    