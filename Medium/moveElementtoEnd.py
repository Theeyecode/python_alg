def moveElementToEnd(array, toMove):
    low = 0
    high = len(array) - 1

    while low < high:
        if array[low] == toMove and array[high] == toMove:
            print('First')
            high -= 1
        elif array[low] == toMove and array[high] != toMove:
            array[low], array[high] = array[high], array[low]
            print('second')
            low += 1
            high -= 1
        elif array[low] != toMove and array[high] == toMove:
            print('third')
            high -= 1
        elif array[low] != toMove and array[high] != toMove:
            print('fourth')
            low += 1

    return array




array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2
y = moveElementToEnd(array, toMove)
print(y)
