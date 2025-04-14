from collections import deque


class Solution:
    def pushDominos(self, dominoes:str) -> str:
        domList = list(dominoes)
        q = deque()

        for index, value in enumerate(domList):
            if value!=".":
                q.append((index,value))
        
        while q:
            index,value = q.popleft()
            if value == "L":
                if index > 0 and domList[index -1] == ".":
                   q.append((index-1,"L"))
                   domList[index -1] = "L"
            elif value == "R":
                if index+1 < len(domList) and domList[index+1] == ".":
                    if index+2 < len(domList) and domList[index+2] == "L":
                        q.popleft()
                    else:
                        q.append(index+1, "R")
                        domList[index+1] = "R"
        return ''.join(domList)
        





        