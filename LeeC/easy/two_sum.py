from ast import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            potential = target - nums[i]
            if potential in hashMap:
                return [hashMap[potential], i]
            hashMap[nums[i]] = i
        print(hashMap)
        return []






            