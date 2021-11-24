def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    smallest = float("inf")
    current = float("inf")
    idxOne = 0
    idxTwo = 0
    smallestpair = []

    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        arrayOneNumber = arrayOne[idxOne]
        arrayTwoNumber = arrayTwo[idxTwo]

        if arrayTwoNumber > arrayOneNumber:
            current = arrayTwoNumber - arrayOneNumber
            idxOne += 1
        elif arrayTwoNumber < arrayOneNumber:
            current = arrayOneNumber - arrayTwoNumber
            idxTwo += 1
        else:
            return [arrayOneNumber, arrayTwoNumber]

        if smallest > current:
            smallest = current
            smallestpair = [arrayOneNumber, arrayTwoNumber]

    return smallestpair


arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]
y = smallestDifference(arrayOne, arrayTwo)
print(y)
