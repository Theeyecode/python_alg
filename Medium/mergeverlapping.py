# def mergeOverlappingIntervals(intervals):
#     output = []
#     low = 1
#     high = len(intervals) - 1
#     while low < high:
#         first_array = intervals[low-1]
#         second_array = intervals[low]
#         if first_array[1] > second_array[0]:
#             y = swap(first_array, second_array)
#             output.append(y)
#         else:
#             output.append(second_array)
#         low += 1
#     # handle the last case
#     if intervals[low][1] > intervals[low-1][0]:
#         output.append(intervals[low])
#     else:
#         y = swap(intervals[low], intervals[low-1])
#     return output


# def swap(array1, array2):
#     newarray = [array1[0], array2[1]]
#     return newarray


def mergeOverlappingIntervals(intervals):
    sortedIntervals = sorted(intervals, key=lambda x: x[0])
    mergedIntervals = []
    currentInterval = sortedIntervals[0]
    mergedIntervals.append(currentInterval)

    for nextInterval in sortedIntervals:
        print(nextInterval)
        _, currentIntervalEnd = currentInterval
        nextIntervalstart, nextIntervalEnd = nextInterval

        if currentIntervalEnd >= nextIntervalstart:
            currentInterval[1] = max(currentIntervalEnd, nextIntervalEnd)

        else:
            currentInterval = nextInterval
            mergedIntervals.append(currentInterval)
    return mergedIntervals


intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
y = mergeOverlappingIntervals(intervals)
print(y)
