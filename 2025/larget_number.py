from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for index, n in enumerate(nums):
            nums[index] = str(n)
        print(nums)
        def compare(n1, n2):
            print(f"Comparing {n1} and {n2} → {n1 + n2} vs {n2 + n1}")
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1
        nums = sorted(nums, key=cmp_to_key(compare))
        return str(int("".join(nums)))
        