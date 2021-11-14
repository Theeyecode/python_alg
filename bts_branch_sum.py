class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    sums = []
    calculateBranchSum(root, 0, sums)
    return sums
    # Write your code here.


def calculateBranchSum(node, runningSum, sums):
    if node is None:
        return

    newRunningSum = runningSum + node.value
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        return

    calculateBranchSum(node.left, newRunningSum, sums)
    calculateBranchSum(node.right, newRunningSum, sums)
