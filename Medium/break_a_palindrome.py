class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        palindromelist = list(palindrome)
        mid = len(palindromelist)//2
        
        for i in range(mid):
            if palindromelist[i] != 'a':
                palindromelist[i] = 'a'
                return ''.join(palindromelist)
        palindromelist[-1] = 'b'
        return ''.join(palindromelist)
