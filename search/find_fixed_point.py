# time complexity is 0(logn)
def find_fixed_point(data):
    low = 0
    high = len(data) - 1

    while low <= high:
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

# brute approach


def find_fixed_point_linear(data):
    for i in range(len(data)):
        if i == data[i]:
            return data[i]
    return False


A = [-10, -5, 0, 3, 7]
y = find_fixed_point(A)
x = find_fixed_point_linear(A)
print(y)
print(x)
