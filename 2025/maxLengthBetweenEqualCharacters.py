class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        hashMap = {}
        res = -1
        for i in range(len(s)):
            if s[i] in hashMap:
                res = max(res, i - hashMap[s[i]] -1)
            else:
                hashMap[s[i]] = i
        return res