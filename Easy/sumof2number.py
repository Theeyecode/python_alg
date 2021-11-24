

def sumOfTwoNumbers(array, targetSum):
    nums = {}

    for n in array:
        potentialNum = targetSum - n
        print(potentialNum)
        if potentialNum in nums:  # this alogorithm runs in 0(n) times
            return [potentialNum, n]

        else:
            nums[n] = True

    return []

# def sumOfTwoNumbers(array, targetSum):
#     array.sort()                                    # runs in 0(nlogn) times, because of the sorting algorithn
#     left = 0
#     right = len(array) - 1

#     while left < right:
#         currentsum = array[left] + array[right]

#         if currentsum == targetSum:
#             return[array[left], array[right]]
#         elif currentsum < targetSum:
#             left += 1
#         elif currentsum > targetSum:
#             right -= 1
#     return []


x = sumOfTwoNumbers([3, 5, -4, 8, 11, 1, -1, 6], 10)
print(x)
