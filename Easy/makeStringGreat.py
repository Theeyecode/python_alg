class Solution:
    def makeGood(self, s: str) -> str:
        stack =[s[0]]
        
        for i in range(1, len(s)):
            cur = s[i]
            
            f = stack and stack[-1] == cur.lower() and cur.isupper()
            b = stack and stack[-1] == cur.upper() and cur.islower()
            
            if f or b:
                stack.pop()
            else:
                stack.append(cur)
        return ''.join(stack)
        