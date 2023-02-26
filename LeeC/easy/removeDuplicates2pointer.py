class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        k = 0

        while i < len(nums):
            value = nums[i]
            while i+1 < len(nums) and nums[i+1] == value:
                nums.remove(value)
            k=k+1
            i=k
        return len(nums)
