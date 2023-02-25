class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left<right:
            if s[left] == s[right]:
                left+=1
                right-=1
            else:
                return self.helper(s,left+1, right) or self.helper(s, left, right-1)
        return True

    def helper(self, s, left, right):
        while left<right:
            if s[left] == s[right]:
                left+=1
                right-=1
            else:
                return False
        return True
