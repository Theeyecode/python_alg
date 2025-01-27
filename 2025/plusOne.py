class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string_numbers = list(map(str,digits))
        toString = ''.join(string_numbers)
        number = int(toString) + 1
        res = []
        while number > 0:
            res.insert(0, number%10) #append the remainder
            number //=10 #gets the other part leaving the fractional remainder
        return res

        
