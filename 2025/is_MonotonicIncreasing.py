from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if nums[-1] - nums[0] < 0:
            nums.reverse()
            #check first and last if its decreasing if it is .. we reverse and do a one way loop
        
        for i in range(len(nums)-1):
            if not (nums[i] <= nums[i+1]):
                return False
        return True
        
        # increasing,decreasing = True, True
        # for i in range(len(nums)-1):
        #     if not(nums[i] <= nums[i+1]):
        #         increasing = False
        #     if not(nums[i] >= nums[i+1]):
        #         decreasing = False
        # return increasing or decreasing