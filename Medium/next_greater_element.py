from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Idx = {n:i for i , n in enumerate(nums1)}
        print(nums1Idx)
        res = [-1] * len(nums1)
        stack = []
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                value = stack.pop()
                idx = nums1Idx[value] 
                res[idx] = cur
                print('result',res)
            if cur in nums1Idx:
                stack.append(cur)
            print(stack)
        return res

x = Solution()
y = x.nextGreaterElement([1,3,5,2,4],
[6,5,4,3,2,1,7])
print(y)
