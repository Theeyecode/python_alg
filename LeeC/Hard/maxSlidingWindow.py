from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        r=0
        output = []
        q = deque()
        while r < len(nums):        #since we are alwasy adding the leftmost elemnt to the output....
            if q and q[0] <= r - k: #we need to know if the index in the leftmost is still part of the window size
                q.popleft()

            while q and nums[r] > nums[q[-1]]: #while the current element is greater than the elements we keep popping
                q.pop()

            q.append(r) #add to the que the index

            if r >= k-1: #when to start adding to the que is when r has reached atleast where the window is....k = 3 which is the 2nd index
                output.append(nums[q[0]])
            r+=1
        return output
