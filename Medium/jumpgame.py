from typing import List
class Solution:
    def canJump( nums: List[int]) -> bool:
        goal = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False

x = Solution
y = x.canJump([3,2,1,0,4])
print(y)