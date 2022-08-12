class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2): 
        if not len(nums1):
            return helper(self,nums2)
        if not len(nums2):
            return helper(self,nums1)
        n1 = len(nums1)
        n2 = len(nums2)
        new_array = [None] * (n1+n2)
        i=0
        j=0
        k=0
    
        while i<n1 and j<n2:
            if nums1[i] < nums2[j]:
                new_array[k] = nums1[i]
                k+=1
                i+=1
            else:
                new_array[k] = nums2[j]
                k+=1
                j+=1
        while i < n1:
            new_array[k] = nums1[i]
            i+=1
            k+=1
        while j < n2:
            new_array[k] = nums2[j]
            j+=1
            k+=1
        return helper(self,new_array)
def helper(self, array):
    if len(array) % 2 == 0:    
        mid = ((len(array)-1)//2)
        output = (array[mid] + array[mid+1])/2.0
        return output
    return array[len(array)//2]
    
       
        