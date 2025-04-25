from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 1
        N = len(nums)

        for i in range(1, N*2):
            if nums[(i-1)%N] <= nums[i%N]:
                count+=1
            else:
                count = 1
            if count == N:
                return True
        return N==1

