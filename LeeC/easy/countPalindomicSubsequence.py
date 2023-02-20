import collections
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left = set()
        res = set()
        right = collections.Counter(s)
        # print(right)

        for i in range(len(s)):
            right[s[i]]-=1
            if right[s[i]] == 0:
                right.pop(s[i])
            
            for j in range(26):
                c = chr(ord("a") +j)
                if c in left and c in right:
                    res.add((s[i], c))
                    # print(res)
            left.add(s[i])
        return len(res)

            
