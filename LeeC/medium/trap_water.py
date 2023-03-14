class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l,r = 0 ,len(height)-1
        maxLeft = height[l]
        maxRight = height[r]
        while l < r:
            if maxLeft <= maxRight:
                l+=1
                maxLeft = max(maxLeft, height[l])
                c = maxLeft - height[l]
                if c > 0:
                    res+=c
            else:
                r-=1  
                maxRight = max(maxRight, height[r])
                c = maxRight- height[r]
                if c > 0:
                    res+=c
     
        return res

        # maxLeft = []
        # maxRight = []
        # res = 0
        # for i in range(len(height)):
        #     heightRight = 0
        #     if i+1:
        #         for j in range(i+1, len(height)):
        #             heightRight = max(heightRight, height[j])
        #     maxRight.append(heightRight)
        # for i in range(len(height)):
        #     heightLeft = 0
        #     if i-1>=0:
        #         for j in range(i-1, -1 ,-1):
        #             heightLeft = max(heightLeft, height[j])
        #     maxLeft.append(heightLeft)
        # print(maxLeft)
        # print(maxRight)
        
        # for i in range(len(height)):
        #     a = maxLeft[i]
        #     b = maxRight[i]
        #     c = min(a,b) - height[i]
        #     if c > 0:
        #         res = res + c
        # return res

        # [4,2,0,3,2,5]




        
