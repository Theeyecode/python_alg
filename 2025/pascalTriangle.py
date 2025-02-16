from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]

        for i in range(rowIndex):
            new_res = [0] * (len(res)+1)
            for j in range(len(res)):
                new_res[j] += res[j]
                new_res[j+1] += res[j]
            res = new_res
        
        return res



