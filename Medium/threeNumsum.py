def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    output = []
    for i in range(len(array) - 2):
        leftidx = i+1
        rightidx = len(array) - 1
        while leftidx < rightidx:
            potentialSum = array[i] + array[leftidx] + array[rightidx]
            if potentialSum == targetSum:
                output.append([array[i], array[leftidx], array[rightidx]])
                leftidx += 1
                rightidx -= 1
            elif potentialSum < targetSum:
                leftidx += 1
            else:
                rightidx -= 1
    return output


array = [12, 3, 1, 2, -6, 5, -8, 6]
y = threeNumberSum(array, 0)
print(y)
