def find_first_entry(data, target):
    low = 0
    high = len(data) - 1

    if len(data) == 0:
        return None

    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target and data[mid-1] != target:
            print('left is right oo')
            print(mid)
            return data[mid]
        elif data[mid] == target and data[mid-1] == target:
            high = mid - 1

        elif data[mid] > target:
            high = mid - 1
            print('gothere')

        else:
            low = mid + 1
            print('atall')

    return data[mid]


# A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
A = [1, 1, 1, 1, 2, 1, 1, 1, 1, 1]
y = find_first_entry(A, 1)
print(y)
