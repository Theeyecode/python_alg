def find_fixed_point(data):
    low = 0
    high = len(data) - 1

    while low < high:
        mid = (low + high)//2
        if mid == data[mid]:
            return data[mid]
        elif mid > A[mid]:
            if mid-1 > 0:
                low = mid+1
            else:
                return False
        else:
            if mid+1 < len(data):
                high = mid-1
            else:
                return False
    return False


A = [-10, -5, 0, 8, 7]
y = find_fixed_point(A)
print(y)
