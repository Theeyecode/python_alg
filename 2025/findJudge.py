class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        k = n+1
        if len(trust) < n-1:
            return -1 
        trust_given = [0] * k
        trust_gotten = [0] * k

        for a,b in trust:
            trust_given[a] +=1
            trust_gotten[b] +=1
        
        for i in range(1,k):
            if trust_given[i] == 0 and trust_gotten[i] == n-1:
                return i
        return -1
