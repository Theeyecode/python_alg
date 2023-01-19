from ast import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) -1
        result = float('inf')
        while l<=r:
            mid = (l+r)//2
            result = min(result, nums[mid])
            if nums[mid] < nums[r] or nums[l] < nums[r]:
                r = mid-1
            else:
                l = mid+1
        return result