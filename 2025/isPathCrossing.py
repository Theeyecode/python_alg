# 1496. Path Crossing

# Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

# Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.
# Input: path = "NES"
# Output: false 
# Explanation: Notice that the path doesn't cross any point more than once.



class Solution:
    def isPathCrossing(self, path: str) -> bool:
        direction = {
            "N" : [0,1],
            "S" : [0,-1],
            "E" : [1,0],
            "W" : [-1,0]
        }
        visited = set()
        x=y = 0

        for p in path:
            visited.add((x,y))
            dx,dy = direction[p]
            x,y = x +dx , y+dy
            if (x,y) in visited:
                return True
        return False


        
