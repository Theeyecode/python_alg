from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]    
        output = [[1]]
        for i in range(rowIndex):
            temp = [0] + output[-1] + [0]
            res = []
            for j in range(0, len(temp) -1):
                res.append(temp[j] + temp[j+1])
            output.append(res)
        return output[-1]