from ast import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = float('-inf')
        currentMax = 0
        
        for i in range(len(nums)):
            currentMax += nums[i]
            maxSub = max(maxSub, currentMax)
            if currentMax < 0:
                currentMax = 0
        return maxSub
            
        