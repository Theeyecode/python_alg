# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hashTable = {}
        if not head:
            return None
        cur = head 
        count = 0
        mid = 0
        while cur:
            count+=1
            hashTable[count] = cur
            cur = cur.next
        
        if count%2 == 0:
            mid = (count //2) +1
        else:
            mid = (count+1) //2
        
        return hashTable[mid]
            
        