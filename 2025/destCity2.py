class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        outgoingSet = set()

        for i in range(len(paths)):
            outgoingSet.add(paths[i][0])
        for i in range(len(paths)):
            if paths[i][1] not in outgoingSet:
                return paths[i][1]
        return "" 
