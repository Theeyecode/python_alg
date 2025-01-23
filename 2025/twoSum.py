class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            potential = target - nums[i]
            if potential in hashmap:
                return [hashmap[potential], i]
            else:
                hashmap[nums[i]] = i
        return []






            
