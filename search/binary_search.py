data = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
target = 2


def binary_search_iterative(data, target):
    low = 0
    high = len(data) - 1

    while low < high:
        mid = (low + high) // 2
        if data[mid] == target:
            return target
        elif target > data[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return False


def binary_search_recursive(data, target):
    low = 0
    high = len(data) - 1
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return target
        elif target > data[mid]:
            return binary_search_recursive(data[mid+1:], target)
        elif target < data[mid]:
            return binary_search_recursive(data[:mid-1], target)
        else:
            return False


print(binary_search_iterative(data, target))
# print(binary_search_recursive(data, target))
