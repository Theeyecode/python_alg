class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = float("-inf")
        hashMap = {}
        l ,r = 0,0
        while r < len(s):
            hashMap[s[r]] = 1 + hashMap.get(s[r], 0)
            x = max(hashMap, key = hashMap.get)           
            y = hashMap[x]
            length = r-l+1
            while length - y > k:
                hashMap[s[l]] = -1 + hashMap.get(s[l], 0)
                l+=1
                length = r -l+1
            res = max(res,length)
            r+=1               
        return res
