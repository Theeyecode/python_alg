class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        i = 0 
        j = 0
        n1,n2 = len(word1), len(word2)
        merged = []

        while i < n1 or j< n2:
            if i<n1:
                merged.append(word1[i])
                i+=1
            if j<n2:
                merged.append(word2[j])
                j+=1
        return ''.join(merged)


        
