from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        result = nums[0] + nums[1] + nums[2]
        nums.sort()
        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            while l<r:
                cur_sum = (nums[i] + nums[l] + nums[r])
                cur_diff = abs(target - cur_sum)

                if cur_sum == target:
                    return cur_sum
                if cur_sum > target:
                    r-=1
                else:
                    l+=1
                if cur_diff < diff:
                    diff = cur_diff
                    result = cur_sum
        return result
            
                
