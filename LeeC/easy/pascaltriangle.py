from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = [[1]] 
        for i in range(numRows -1):
            temp = [0] + arr[-1] + [0]
            res = []
            for j in range(0,len(temp) -1):
                res.append(temp[j] + temp[j+1])
            arr.append(res)
        return arr

