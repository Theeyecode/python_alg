class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {')' : '(', '}': '{', ']':'['}
        stack = []

        for i in s:
            if i not in hashMap:
                stack.append(i)
                continue
            if not stack or stack[-1] != hashMap[i]:
                return False
            stack.pop()
        return not stack


            
