def bubblesort(array):
    isSorted = False
    counter = 0
    while not isSorted:
        isSorted = True
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                isSorted = False
        counter += 1
    return array


array = [8, 5, 2, 9, 5, 6, 3]
y = bubblesort(array)
print(y)
