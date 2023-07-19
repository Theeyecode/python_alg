class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.split()
        l=0
        r = len(word_list) -1
        while r>l:
            word_list[l], word_list[r] = word_list[r],word_list[l]
            r-=1
            l+=1
        return ' '.join(word_list)

        
