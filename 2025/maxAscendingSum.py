
from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = 0
        curSubarraySum = nums[0]

        for i in range(1,len(nums)):
            if nums[i] <= nums[i-1]:
                res = max(res,curSubarraySum)
                curSubarraySum = 0
            curSubarraySum+=nums[i]
        
        return max(res, curSubarraySum)
            
        

        