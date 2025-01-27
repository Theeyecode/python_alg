class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

       # Move along the input array starting from the end of the array.

#Set all the nines at the end of the array to zero.

#If we meet a not-nine digit, we would increase it by one. The job is done - return digits.
        n = len(digits)

        for i in range(n):
            idx = n-1 - i

            if digits[idx] == 9:
                digits[idx] = 0
            
            else:
                digits[idx] +=1
                return digits
        return [1] + digits 
