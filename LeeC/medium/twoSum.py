class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) -1
        while left<right:
            curSum = numbers[left] + numbers[right]
            if curSum == target:
                return [left+1, right+1]
            elif curSum > target:
                right-=1
            else:
                left+=1
