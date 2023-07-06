class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums)<=1:
            if nums[0] < target:
                return 0
            else:
                return 1
        if sum(nums) < target:
            return 0
        i = 0
        j = 0
        summ = 0
        res = len(nums)
        while j<len(nums):
            summ+=nums[j]
            while summ >= target:
                res = min(res, j-i+1)
                summ-=nums[i]
                i+=1
            j+=1
        return res
            

            


