class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        countGap = {0:0}

        for row in wall:
            total = 0
            for brick in row[:-1]:
                total+=brick
                countGap[total] = 1 + countGap.get(total, 0)
        return len(wall) - max(countGap.values())
