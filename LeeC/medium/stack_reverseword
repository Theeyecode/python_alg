class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.split()
        stack = []
        res = ""
        for word in word_list:
            stack.append(word)
        while stack:
            res +=" " + stack.pop()
        return res.strip()
        
