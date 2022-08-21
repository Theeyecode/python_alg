class Solution(object):
    def plusOne(self, digits): 
        num = ''
        for i in digits:
            num+= str(i)
        num = int(num) +1
        digits = list(map(int, str(num)))
        return digits