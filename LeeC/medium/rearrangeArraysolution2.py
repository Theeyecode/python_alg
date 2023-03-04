class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # O(n)
        a = nums[0] < nums[1]
        for i in range(len(nums)-1):
            if a and nums[i] < nums[i+1] or (not a and nums[i] > nums[i+1]):
                temp = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = temp

            a = not a
            print(a)

        return nums
