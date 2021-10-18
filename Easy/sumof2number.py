# def sumOfTwoNumbers(array, targetSum):
#     nums = {}

#     for n in array:
#         potentialNum = targetSum - n
#         if potentialNum in nums:
#             return [potentialNum, n]

#         else:
#             nums[n] = True

#     return []

def sumOfTwoNumbers(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1

    while left < right:
        currentsum = array[left] + array[right]

        if currentsum == targetSum:
            return[array[left], array[right]]
        elif currentsum < targetSum:
            left += 1
        elif currentsum > targetSum:
            right -= 1
    return []


x = sumOfTwoNumbers([6, -3, 9, 1, 22, 1, 6, 12], 13)
print(x)
