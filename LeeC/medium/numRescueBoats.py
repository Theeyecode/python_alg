class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people)-1
        res = 0
        while r >= l:
            remaining = limit - people[r]
            r-=1
            res+=1
            if r>=l and remaining >= people[l]:
                l+=1
        return res

           
        
        
  
