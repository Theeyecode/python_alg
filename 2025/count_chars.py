from collections import defaultdict
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        hashMap = defaultdict(int)
        for c in chars:
            hashMap[c] +=1
        ans = 0
        for word in words:
            word_count = defaultdict(int)
            good = True
            for w in word:
                word_count[w] +=1
                if w not in hashMap or word_count[w] > hashMap[w]:
                    good = False
                    break

            # for key, val in word_count.items():
            #     if hashMap[key] < val:
            #         good = False
            #         break
            if good:
                ans += len(word)
        return ans
                
