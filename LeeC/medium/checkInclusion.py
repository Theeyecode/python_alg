class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        checks1 = [0] * 26
        checks2 = [0] * 26

        for i in range(len(s1)):
            checks1[ord(s1[i]) - ord('a')] +=1
            checks2[ord(s2[i]) - ord('a')] +=1
        
        matches = 0
        for i in range(26):
            if checks1[i] == checks2[i]:
                matches+=1
            else:
                matches+=0
        l = 0
        for i in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[i]) - ord('a')
            checks2[index] +=1

            if checks1[index] == checks2[index]:
                matches+=1
            elif checks1[index] +1 == checks2[index]:
                matches -=1
            
            index = ord(s2[l]) - ord('a')
            checks2[index] -=1

            if checks1[index] == checks2[index]:
                matches+=1
            elif checks1[index] -1 == checks2[index]:
                matches -=1   
            l+=1
        return matches == 26



        

        # if len(s1)>len(s2):
        #     return False
        # hashs1 = {}
        # for s in s1:
        #     hashs1[s] = 1+ hashs1.get(s, 0)
        # l = 0
        # r = len(s1)-1
        # print(hashs1)
        # while r < len(s2):
        #     hashs2 = {}
        #     while l<=r:
        #         hashs2[s2[l]] = 1+ hashs2.get(s2[l], 0)
        #         l+=1
        #     if hashs1 == hashs2:
        #         return True
        #     r+=1
        #     l= r - len(s1) +1 
        #     #hashs2[s2[l-1]] = -1 + hashs2.get(s2[l-1], 0)
        # return False
                
        


            



