# 0(n) TS
def bitonic_sequence_iterative(data):
    highest = data[0]
    for i in range(len(data)):
        if data[i] > highest:
            highest = data[i]
    return highest


def bitonic_sequence(data):
    low = 0
    high = len(data) - 1
    highest = 0

    if len(data) < 3:
        return None

    while low <= high:
        mid = (low + high) // 2
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
