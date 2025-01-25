class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        hashMap = Counter(words[0])
        for w in words:
            cur_hashMap = Counter(w)
            for c in hashMap:
                hashMap[c] = min(hashMap[c], cur_hashMap[c])
        res = []

        for k,v in hashMap.items():
            for i in range(v):
                res.append(k)
        return res
