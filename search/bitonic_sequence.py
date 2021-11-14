def bitonic_sequence_iterative(data):
    highest = data[0]
    for i in range(len(data)):
        if data[i] > highest:
            highest = data[i]
    return highest


A = [1, 2, 3, 4, 5, 4, 3, 2]
y = bitonic_sequence_iterative(A)
print(y)
