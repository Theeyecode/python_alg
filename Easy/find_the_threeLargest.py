# def findThreeLargestNumbers(array):
#     # Write your code here.
#     threeLargestNum = [None, None, None]
#     for num in array:
#         compareAndUpdateLargestNumber(threeLargestNum, num)
#     return threeLargestNum


# def compareAndUpdateLargestNumber(threeLargestNum, num):
#     if threeLargestNum[2] is None or num > threeLargestNum[2]:
#         shiftAndUpdate(threeLargestNum, num, 2)
#     elif threeLargestNum[1] is None or num > threeLargestNum[1]:
#         shiftAndUpdate(threeLargestNum, num, 1)
#     elif threeLargestNum[0] is None or num > threeLargestNum[0]:
#         shiftAndUpdate(threeLargestNum, num, 0)

# # this helper method helps to shift the numbers to the left if there is bigger number

#                 # [2,5,9], 6 ,  1
# def shiftAndUpdate(array, num, idx):
#     for i in range(idx + 1):
#         if i == idx:
#             array[i] = num
#         else:
#             array[i] = array[i + 1]


def findThreeLargestNumbers(array):
    currentidx = 0

    while currentidx < len(array) - 1:
        if currentidx == 3:
            return array[3::-1]

        largestNum = currentidx
        for i in range(largestNum + 1, len(array)):
            if array[largestNum] < array[i]:
                largestNum = i
        array[largestNum], array[currentidx] = array[currentidx], array[largestNum]
        currentidx += 1
    return array[2::-1]


array = [141, 1, 17, 7, -17, -27, 18, 541, 8, 19, 7]
y = findThreeLargestNumbers(array)
print(y)
