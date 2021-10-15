def sumOfTwoNumbers(array, targetSum):
    nums = {}

    for n in array:
        potentialNum = targetSum - n
        if potentialNum in nums:
            return [potentialNum, n]
        else:
            nums[n] = True

    return []


x = sumOfTwoNumbers([4, 6, -3, 9, 12, 2, 1, 6], 13)
print(x)
