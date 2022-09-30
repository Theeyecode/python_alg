from ast import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)      
        for word in strs:
            count = [0] * 26       
            for letters in word:
                count[ord(letters) - ord('a')] +=1
            res[tuple(count)].append(word)
        return res.values()
        
        