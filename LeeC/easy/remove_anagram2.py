class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res=[words[0]]
        for i in range(1, len(words)):
            prev = sorted(words[i-1])
            cur = sorted(words[i])
            if prev!=cur:
               res.append(words[i])
        return res
