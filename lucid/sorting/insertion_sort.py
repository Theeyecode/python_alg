def insertion(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1
    return array


array = [8, 5, 2, 9, 5, 6, 3]
y = insertion(array)
print(y)

#   In insertion sort we say the first elemnt is sorted , then we sort through the rest towards the sorted elemnt <---
