class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashMap = {}
        for string in s:
            hashMap[string] = 1 + hashMap.get(string,0)
        for k in hashMap:
            if hashMap[k] == 1:
                return s.index(k)
        return -1
