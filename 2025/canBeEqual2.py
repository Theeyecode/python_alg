class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if len(target) != len(arr):
            return False
        
        return sorted(target) == sorted(arr) timeComplextit is nlogn, space  = 0(1)
