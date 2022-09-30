from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        phashMap = {}
        shashMap = {}
        for i in range(len(p)):
            phashMap[p[i]] = 1 + phashMap.get(p[i], 0)
            shashMap[s[i]] = 1 + shashMap.get(s[i], 0)
            
        res = [0] if phashMap == shashMap else []
        l_p = 1
        for r_p in range(len(p), len(s)):
            shashMap[s[r_p]] = 1 + shashMap.get(s[r_p], 0)
            shashMap[s[l_p]] -=1
            
            if shashMap[s[l_p]] == 0:
                shashMap.pop(s[l_p])
            l_p+=1
            if shashMap == phashMap:
                res.append(l_p)
        return res