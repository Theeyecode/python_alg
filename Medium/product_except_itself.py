from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:  
        postfix = 1
        prefix = 1 
        output = [prefix]
        for i in range(1,len(nums)):
            prefix = prefix * nums[i-1]
            output.append(prefix) 
        for i in reversed(range(len(nums))):
            output[i] = output[i] * postfix
            postfix = postfix * nums[i]
        return output
            
        