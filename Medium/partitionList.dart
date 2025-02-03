// # Definition for singly-linked list.
// # class ListNode:
// #     def __init__(self, val=0, next=None):
// #         self.val = val
// #         self.next = next
// class Solution:
//     def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
//         d1 = c1 = ListNode(0)
//         d2 = c2 = ListNode(0)

//         while head:
//             if head.val<x:
//                 c1.next = head
//                 c1 = c1.next

//             else:
//                 c2.next =head
//                 c2=c2.next

//             head = head.next
        
//         c2.next = None
//         c1.next = d2.next
//         return d1.next
