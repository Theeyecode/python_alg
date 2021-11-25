def bubblesort(array):
    isSorted = False   
    counter = 0  #optimize the loop not to read the last elemnet
    while not isSorted:
        isSorted = True   #
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i+1]:   #checks 
                array[i], array[i+1] = array[i+1], array[i]   #swaps
                isSorted = False      # if the loop enters the if statement
        counter += 1 #since after each loop the largest elemnet is always moved to the last position
    return array


array = [8, 5, 2, 9, 5, 6, 3]
y = bubblesort(array)
print(y)
