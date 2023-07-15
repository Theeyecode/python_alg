# Definition for a binary tree node.
from ast import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        list1 = []
        def preOrder(start, list1):
            if not start:
                return
            list1.append(start.val)
            preOrder(start.left, list1)
            preOrder(start.right, list1)
        preOrder(root, list1)
        return list1


       
        
        
