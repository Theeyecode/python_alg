class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
       char_count = {} 

       for i in s:
           if i in char_count:
            char_count[i] +=1
           else:
                char_count[i] = 1
       all_vals = char_count.values()
       return len(set(all_vals)) == 1
        
        
