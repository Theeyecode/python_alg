class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        hashSet = set()
        l = 0
        for r in range(len(s)):
            while s[r] in hashSet:
                hashSet.remove(s[l])
                l+=1
            hashSet.add(s[r])
            res = max(res, r-l+1)
        return res





















        # hashMap = {}
        # curSum = 0
        # output = 1
        # for l in range(len(s)):
        #     if s[l] in hashMap :
        #         output = max(output, curSum)
        #         curSum = 0
        #         hashMap = {}
        #     hashMap[s[l]] = 1
        #     curSum+=1
        # return output
