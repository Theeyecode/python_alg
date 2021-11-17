"""
Define a bitonic sequence as a sequence of integers such that:
    x_1 < ... < x_k > ... > x_n-1 for some k, 0 <= k < n.
For example:
    1, 2, 3, 4, 5, 4, 3, 2, 1
is a bitonic sequence. Write a program to find the largest element in such a
sequence. In the example above, the program should return "5".
We assume that such a "peak" element exists.
"""


# 0(n) TS
def bitonic_sequence_iterative(data):
    highest = data[0]
    for i in range(len(data)):
        if data[i] > highest:
            highest = data[i]
    return highest

# 0(logn)


def bitonic_sequence(data):
    low = 0
    high = len(data) - 1

    if len(data) < 3:
        return None

    while low <= high:
        mid = (low + high) // 2
        print(data[mid])
        mid_left = data[mid-1] if mid-1 > 0 else float("-inf")
        mid_right = data[mid+1] if mid+1 < len(data) else float("inf")

        if mid_left < data[mid] and mid_right > data[mid]:
            low = mid+1

        elif mid_left > data[mid] and mid_right < data[mid]:
            high = mid-1

        else:
            # mid_left < data[mid] and mid_right < data[mid:
            return data[mid]


A = [1, 2, 3, 4, 5, 4, 3, 2]
y = bitonic_sequence_iterative(A)
x = bitonic_sequence(A)
print(x)
print(y)
