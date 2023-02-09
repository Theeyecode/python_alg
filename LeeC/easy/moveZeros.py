class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        j = 0
        while i < len(nums):
            if nums[i] !=0:
                nums[i], nums[j] = nums[j], nums[i]
                j+=1
            i+=1
