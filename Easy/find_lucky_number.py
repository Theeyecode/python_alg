class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # Using set
        maxi = -1
        for i in set(arr):
            if i == arr.count(i) and maxi < i:
                maxi = i
        return maxi
    def findLucky2(self, arr):
        dc = {}
        for i in range(len(arr)):
            if arr[i] not in dc:
                dc[arr[i]] = 1
            else:
                dc[arr[i]] = dc[arr[i]] +  1
        freq = -1
        for key, value in dc.items():
            if key == value:
                freq = max(key, freq)

        return freq
            
            
        