def firstDuplicateValue(array):

    firstidxfound = len(array)

    for i in range(len(array)):
        value = array[i]
        for j in range(i+1, len(array)):
            comparevalue = array[j]
            if value == comparevalue:
                firstidxfound = min(firstidxfound, j)
    if firstidxfound == len(array):
        return -1

    return array[firstidxfound]


array = [2, 1, 5, 7, 3, 3, 4]
y = firstDuplicateValue(array)
print(y)
