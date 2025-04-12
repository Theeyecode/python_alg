from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        p1,p2 = 0,0
        res = 0
        g.sort()
        s.sort()

        while p1 < len(g) and p2 < len(s):
            if s[p2] >= g[p1]:
                res+=1
                p1+=1
            p2+=1
        return res

    #    g= 7,8,9,10
    #   s=  5,6,7,8