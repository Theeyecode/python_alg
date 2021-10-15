def sumOfTwoNumbers(array, targetSum):
    nums = {}

    for n in array:
        potentialNum = targetSum - n
        if potentialNum in nums:
            return [potentialNum, n]
        else:
            nums[n] = True

    return []


x = sumOfTwoNumbers([3, 5, -4, 8, 11, 1, -1, 6], 10)
print(x)
