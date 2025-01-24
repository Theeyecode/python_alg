class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if len(target) != len(arr):
            return False
        hashMap = {}

        for i in range(len(target)):
            hashMap[target[i]] = hashMap.get(target[i], 0) + 1
            hashMap[arr[i]] = hashMap.get(arr[i], 0) - 1
        x = hashMap.values()

        return len(set(x)) == 1 # timeComplexity is 0(n) space compexity is also 0(n)
