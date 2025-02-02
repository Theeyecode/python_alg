from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-2  # Start from the second last element
        while i>=0 and nums[i+1] <= nums[i]: # Find the first element that is smaller than the element to its right
            i-=1 # Decrement i
        if i > 0: # If i is greater than 0
            j = len(nums)-1 # Start from the last element
            while nums[j] <= nums[i]: # Find the first element that is greater than the element at index i
                j-=1 # Decrement j
            self.swap(nums,i,j) # Swap the two elements
        self.reverse(nums,i+1) # Reverse the elements from i+1 to the end of the list
    
    def reverse(self, nums, start):  # Reverse the elements from start to the end of the list
        i,j = start, len(nums)-1 # Start from the start index and the last index
        while i < j: # While i is less than j
            self.swap(nums,i,j) # Swap the two elements
            i+=1 # Increment i
            j-=1 # Decrement
        
    
    def swap(self, nums, i, j): # Swap the elements at index i and j
        temp = nums[i] # Store the element at index i in a temporary variable
        nums[i] = nums[j] # Replace the element at index i with the element at index
        nums[j] = temp # Replace the element at index j with the element stored in the temporary variable

        