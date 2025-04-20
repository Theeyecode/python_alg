from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l<=r:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid  
            #left sorted side
            if nums[mid] >= nums[l]:
                if target > nums[mid] or target<nums[l]: #we only want to move out of left side if any of this is satisfied
                    l = mid+1
                else:
                    r = mid-1
            #we are in the right side
            else:
                if target < nums[mid] or target > nums[r]: #we only want to move out of right side if any of this is satisfied
                    r = mid-1
                else:
                    l = mid+1   
        return -1
         
            

