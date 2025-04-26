class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        word_s1 = s1.split()
        word_s2 = s2.split()
        hashmap_word_s1 = {}
        for word in word_s1:
            hashmap_word_s1[word] = hashmap_word_s1.get(word, 0) +1
        hashmap_word_s2 = {}
        for word in word_s2:
            hashmap_word_s2[word] = hashmap_word_s2.get(word,0) +1
        res = []
        for word,count in hashmap_word_s1.items():  #word is key, count is value
            if word not in hashmap_word_s2 and count == 1:
                res.append(word)
        for word, count in hashmap_word_s2.items():
            if word not in hashmap_word_s1 and count ==1:
                res.append(word)
        
        return res
        




        