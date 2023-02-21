class Solution:
    def minSwaps(self, s: str) -> int:

        maximum_closing = 0
        count = 0
        closing = ']'
        open = '['

        for i in range(len(s)):
            if s[i] == "]":
                count+=1
                maximum_closing = max(maximum_closing, count)
            else:
                count-=1
        return (maximum_closing +1)//2
