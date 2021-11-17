def find_closest_num(data, target):
    min_diff = float("inf")
    low = 0
    high = len(data) - 1
    closest_num = None

    # check if the list is empty or contains ony one element
    if len(data) == 0:
        return False
    if len(data) == 1:
        return data[0]

    while low < high:
        mid = (low + high) // 2
        if mid + 1 <= len(data):  # trying not to read beyound the list
            min_diff_right = abs(data[mid+1] - target)
        if mid > 0:
            min_diff_left = abs(data[mid-1] - target)

        # check if the abs value are smaller than any seen prior
        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_num = data[mid-1]
        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_num = data[mid+1]

        # move the mid-point accoridingly as its done in a binary search
        if A[mid] < target:  # if the midpoint is less than the target then you move your left pointer to midpoint+1
            low = mid+1
        elif A[mid] > target:  # if the midpoint is greater than the target then you move your right pointer to midpoint-1
            high = mid - 1
        else:  # the midpoint is == target the return the midpoint
            return data[mid]
    return closest_num


A = [2, 5, 7, 9, 11, 13, 33]
A1 = [1, 2, 4, 5, 6, 8, 9]
target = 3
y = find_closest_num(A1, target)
print(y)
