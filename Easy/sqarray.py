# def sortedSquaredArray(array):

#     newArray = [0 for _ in array]

#     for idx in range(len(array)):
#         value = array[idx]
#         newArray[idx] = value * value

#     newArray.sort()

#     return newArray

#     # Write your code here.
#     pass


# optimal solution

def sortedSquaredArray(array):
    sortedSquares = [0 for _ in array]
    smallerValueIdx = 0
    largerValueIdx = len(array) - 1

    for idx in reversed(range(len(array))):
        smallerValue = array[smallerValueIdx]
        largerValue = array[largerValueIdx]

        if abs(smallerValue) > abs(largerValue):

            sortedSquares[idx] = smallerValue * smallerValue
            smallerValueIdx += 1
        else:
            sortedSquares[idx] = largerValue * largerValue
            largerValueIdx -= 1

    return sortedSquares


x = sortedSquaredArray([-9, 1, 2, 3, 4, 5])
print(x)
