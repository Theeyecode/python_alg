class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        for i in range(len(paths)):
            cur = paths[i][1]
            good = True

            for j in range(len(paths)):
                if paths[j][0] == cur:
                    good = False
            if good:
                return cur
        return ''

        # timeComplexity = O(n2)
        # space complexity =O(1)
