class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            new_node = Node(data)
            self.root = new_node
        else:
            self._insert(self.root, data)

    def returnroot(self):
        return self.root

    def _insert(self, cur, data):
        if data < cur.value:
            if cur.left == None:
                cur.left = Node(data)
                cur.left.parent = cur

            else:
                self._insert(cur.left, data)
        elif data > cur.value:
            if cur.right == None:
                cur.right = Node(data)
                cur.right.parent = cur
            else:
                self._insert(cur.right, data)
        else:
            print('Value already exist')

    def find(self, data):
        if self.root is not None:
            return self._find(self.root, data)
        else:
            return False

    def _find(self, cur, data):
        if data == cur.value:
            return cur.value
        elif data < cur.value and cur.left is not None:
            return self._find(cur.left, data)
        elif data > cur.value and cur.right is not None:
            return self._find(cur.right, data)

    # can only delete a node by its value
    def delete(self, data):

        return self._delete(self.find(data))

    def _delete(self, data):
        def minimum_value(n):
            current = n
            while current.left is not None:
                current = current.left
            return current

        def numberofchildren(n):
            numberofchildren = 0
            if n.left is not None:
                numberofchildren + 1
            if n.right is not None:
                numberofchildren + 1
            return numberofchildren

        node_parent = data.parent
        node_children = numberofchildren(data)

        # case 1: Deleting a leaf node
        if node_children == 0:
            if node_parent is not None:
                node_parent.left = None
            else:
                node_parent.right = None
        else:
            self.root = None

        # case 2:Deleting a node that has one leaf node

        if node_children == 1:
            if node_parent.left is not None:
                child = node_parent.left
            else:
                child = node_parent.right

            # checks if it was the root node
            if node_parent is not None:     # if its not the root node
                if node.parent.left == data:
                    node.parent.left = child
                else:
                    node.parent.right = child
            else:
                self.root = child

            child.parent = node_parent

        # caase3 : Deleting a node with two children

        if node_children == 2:
            successor = min_value_node(node.right_child)
            # get the inorder successor of the deleted node

            # copy the inorder successor's value to the node formerly
            # holding the value we wished to delete
            node.value = successor.value

            # delete the inorder successor now that it's value was
            # copied into the other node
            self._delete(successor)

    def search(self, data):
        if self.root is not None:
            return self._search(self.root, data)
        else:
            return False

    def _search(self, cur, data):
        if data == cur.value:
            print('Gotten')
            return True
        elif data < cur.value and cur.left is not None:
            print('Go to left')
            return self._search(cur.left, data)
        elif data > cur.value and cur.right is not None:
            print('Go to right')
            return self._search(cur.right, data)

        else:
            print('value no exist')
            return False

    def height(self):
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            print('This Tree is empty')
            return 0

    def _height(self, cur, cur_height):
        if cur is None:
            return cur_height
        else:
            left_height = self._height(cur.left, cur_height + 1)
            right_height = self._height(cur.right, cur_height + 1)
            return max(left_height, right_height)

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
bst.insert(3)
bst.insert(8)
bst.delete(8)
print('BST height :', bst.height())
print('BST value found is :', bst.find(9))
print('BST root:', str(bst.returnroot().value))


bst.print_func()
