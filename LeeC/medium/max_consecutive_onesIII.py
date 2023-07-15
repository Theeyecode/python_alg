class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = float("-inf")
        count = 0
        l=0
        for r in range(len(nums)):
            if nums[r] == 0:
                count+=1
            if (count <= k):
                res = max((r-l+1), res)
            elif(count>k):
                if nums[l] == 0:
                    count-=1
                l+=1
        return res if res!=float("-inf") else 0



            

