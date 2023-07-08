class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = []
        prev = []
        for word in words:
            count = [0] *26
            for letter in word:
                count[ord(letter) - ord("a")] +=1  
            if count != prev:
                res.append(word)
                prev = count
        return res


            

