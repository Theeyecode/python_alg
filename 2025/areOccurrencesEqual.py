class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
       checker = {}

       for i in s:
           if i in checker:
            checker[i] +=1
           else:
                checker[i] = 1
       all_vals = checker.values()
       return len(set(all_vals)) == 1
        
        
