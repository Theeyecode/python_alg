class Solution:
    def maxScore(self, s: str) -> int:
        if len(s) == 2:
            left = self.getZeros(s[0])
            right = self.getOnes(s[1])
            return left+right
        res = float('-inf')
      
        for i in range(1,len(s)):
            left = self.getZeros(s[:i])
            right = self.getOnes(s[i:])
            print(s[:i])
            print(s[i:])

            cur = left+right
            res = max(res,cur)

        return res

    
    def getZeros(self,string):
        res = 0
        for s in string:
            if s == '0':
                res+=1
        return res
    def getOnes(self,string):
        res = 0
        for s in string:
            if s == '1':
                res+=1
        return res
        
        #timeComplexity is 0(n2) space complexity is 0(1)