class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []
        # n is col, m is row.. you build col first then build row next
        # result = [[0] * n for _ in range(m)]
        result = [[0 for _ in range(n)] for _ in range(m)]
        print(result)
        index = 0

        for i in range(m):
            for j in range(n):
                result[i][j] = original[index]
                index +=1
        return result


        

 
        


        
