class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for idx,value in enumerate(nums):
            if value == target:
                return idx
            elif value > target:
                return idx
            else:
                continue
        return idx+1
            
        
        