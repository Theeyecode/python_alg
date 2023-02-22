class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        hashMap = {}
        res = 0
        for a,b in rectangles:
            hashMap[(b/a)] = 1 + hashMap.get((b/a), 0)
        for val in hashMap.values():
            res += (val*(val-1)) //2
        return res
                

