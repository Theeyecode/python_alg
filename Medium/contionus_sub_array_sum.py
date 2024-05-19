class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashMap = {0:-1}
        total = 0
        for i, n in enumerate(nums):
            total = total+n
            r = total % k
            if r not in hashMap:
                hashMap[r] = i
            elif i - hashMap[r] > 1:
                return True
        return False



        

