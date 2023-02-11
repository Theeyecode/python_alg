class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0
        for n in numsSet:
            if (n-1) not in numsSet:
                length = 0
                while (n+length) in numsSet:
                    length+=1
                longest = max(length, longest)
        return longest
        # if len(nums) == 0:
        #     return 0
        # nums.sort()
        # maximum = 1
        # longest = 1
        # for i in range(1, len(nums)):
        #     if nums[i] - nums[i-1] == 1:
        #         longest+=1
        #     else:
        #         longest = 1
        #     maximum = max(maximum, longest)
        # return maximum
