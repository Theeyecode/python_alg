class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        countT , window = {},{}                        #Initialize the hashmap
        for c in t:                                #add each string in countT
            countT[c] = 1 + countT.get(c,0)
        have, need = 0, len(countT)
        res, resLen = [-1,-1], float("infinity")              #Initialize the result and lenght
        l = 0
        for r in range(len(s)):                                #loop through the string s
            cur = s[r]
            window[cur] = 1 + window.get(cur,0)                          #add each string in the hashMp

            if cur in countT and window[cur] == countT[cur]:            #check if it meets the value in the countT and increment have
                have+=1
            
            while have == need:          #keep
                if (r-l+1) < resLen:  #update your result
                    res = [l,r]
                    resLen = (r-l+1)
                window[s[l]] -=1    #pop from left of your window
                if s[l] in countT and window[s[l]] < countT[s[l]]: #if the index of the string in t are not equal in the hashmap
                    have-=1
                l+=1
        l,r = res
        return s[l:r+1] if resLen != float("infinity") else ""
        
        

  