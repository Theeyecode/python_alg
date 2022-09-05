from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        def dfs(i,j):
            if i < 0 or j < 0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] == 0:
                return 1
            if (i,j) in visited:
                return 0
            visited.add((i,j))
            perim = dfs(i, j-1)
            perim += dfs(i-1, j)
            perim += dfs(i+1, j)
            perim += dfs(i, j+1)
            return perim
    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return dfs(i,j)

        
        
        
        