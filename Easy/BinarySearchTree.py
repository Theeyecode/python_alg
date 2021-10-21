class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            new_node = Node(data)
            self.root = new_node
        else:
            self._insert(self.root, data)

    def _insert(self, cur, data):
        if data < cur.value:
            if cur.left == None:
                cur.left = Node(data)
            else:
                self._insert(cur.left, data)
        elif data > cur.value:
            if cur.right == None:
                cur.right = Node(data)
            else:
                self._insert(cur.right, data)
        else:
            print('Value already exist')

    # def print_tree(self):
    #     if self.root != None:
    #         self._print_tree(self.root)

    # def _print_tree(self, cur_node):
    #     if cur_node != None:
    #         self._print_tree(cur_node.left)
    #         print(str(cur_node.value))
    #         self._print_tree(cur_node.right)

    def print_func(self):
        if self.root is not None:
            self._print_func(self.root)

    def _print_func(self, cur_node):
        if cur_node is not None:
            self._print_func(cur_node.left)
            print(cur_node.value)
            self._print_func(cur_node.right)


bst = BST()
bst.insert(5)
bst.insert(7)

bst.print_func()
