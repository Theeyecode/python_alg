from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 1:
            return [-1,-1]
        length = len(nums)-1
        l,r = 0,length

        while l<=r:
            m = (l+r) // 2
            if nums[m] > target:
                r = m-1
            elif nums[m] < target:
                l=m+1
            else:
                i,j=m,m
                while i-1 >=0 and nums[i] == target and nums[i-1] == target and i>= 0:
                    i-=1
                while j+1 <=length and nums[j] == target and nums[j+1] == target and j<= length:
                    j+=1
                return [i,j]
        return [-1,-1]



            
        