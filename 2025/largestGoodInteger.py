class Solution:
    def largestGoodInteger(self, num: str) -> str:
        # largest = '\0'
        # for index in range(len(num)-2):
        #     if num[index] == num[index+1] == num[index+2]:
        #         largest  = max(largest,num[index])
        #         print(type(num[index]))
        #         print(largest)
        
        # return '' if largest == '\0' else largest * 3
        output = ''
        i = 0
        while i < (len(num)-2):
            if num[i:i+3] == num[i] *3:
                output = max(output, num[i:i+3])
                i+=3
            else:
                i+=1
        return output

        