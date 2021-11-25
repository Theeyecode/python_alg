def isMonotonic(array):
    if len(array) <= 2:
        return True
    isNonIncreasing = True
    isNondecreasing = True

    for i in range(1, len(array)):
        if array[i] < array[i-1]:
            isNondecreasing = False
        if array[i] > array[i-1]:
            isNonIncreasing = False
    return isNondecreasing or isNonIncreasing


array = [-1, -5, -10, -1100, -1100, -1101, -2102, -9001]
y = isMonotonic(array)
print(y)
