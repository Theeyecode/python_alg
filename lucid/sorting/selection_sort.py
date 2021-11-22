def selection(array):
    count = 0
    while count < (len(array) - 1):
        smallestidx = count
        for i in range(count + 1, len(array)):
            if array[smallestidx] > array[i]:
                smallestidx = i
        array[count], array[smallestidx] = array[smallestidx], array[count]
        count += 1
    return array


array = [8, 5, 2, 9, 5, 6, 3]
y = selection(array)
print(y)
