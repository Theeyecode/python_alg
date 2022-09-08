# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur = head
        prev = None
        while cur:
            if cur.val == val:
                if prev:
                    prev.next = cur.next
                    cur=cur.next 
                else:
                    head = cur.next
                    cur = cur.next    
            else:
                prev = cur
                cur = cur.next
        
        
        return head
        

                
            
            
        
                
            
                    
        