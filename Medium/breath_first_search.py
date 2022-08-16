# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        # Write your code here.
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            for x in current.children:
                queue.append(x)
            array.append(current.name)
        return array
                
                
        
