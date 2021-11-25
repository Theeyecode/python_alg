#This algorithm removes duplicate Node in a linkedlist...
# i didnt test this algorithm if it works or not
class LinkedList:
    def __init__(self, value):
        self.next = None
        self.value = value


def remove_node_duplicate(linkedList):
    currentNode = linkedList
    while currentNode is not None:
        nextNode = currentNode.next
        while nextNode is not None and nextNode.value == currentNode.value:
            nextNode = nextNode.next
        currentNode.next = nextNode
        currentNode = nextNode
    return linkedList

