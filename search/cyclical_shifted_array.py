# this program returns the smallest number in this array
def cyclical_shifted_array(data):
    low = 0
    high = len(data) - 1

    while low < high:
        mid = (low + high) // 2
        if data[mid] > data[high]:
            low = mid + 1
        elif data[mid] <= data[high]:
            high = mid

    return data[low]


A = [1, 2, 3, 4, 5, 6, 7]
# A = [3, 4, 5, 6, 7, 1, 2]
y = cyclical_shifted_array(A)
print(y)
