from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        changed = False
        for i in range(len(nums)-1):
            if nums[i] <= nums[i+1]:
                continue
            if changed:
                return False
            if i == 0 or nums[i+1] >= nums[i-1]: #  == 0 Helps not to go out of bound [1,4,2,3]...[3,4,2,3] case
                nums[i] = nums[i+1]
            else:
                nums[i+1] = nums[i]
            changed = True
        return True
        