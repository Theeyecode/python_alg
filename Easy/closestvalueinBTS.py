def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, tree.value)


def findClosestValueInBstHelper(tree, target, closest):
    currentNode = tree

    while currentNode is not None:
        if abs(target-closest) > abs(currentNode.value):
            closest = currentNode.value

        if target > currentNode.value:
            currentNode = currentNode.right
        elif target < currentNode.value:
            currentNode = currentNode.left
        else:
            break
    return closest


    #time complexity is 0(logn), space complexity is 0(i)
