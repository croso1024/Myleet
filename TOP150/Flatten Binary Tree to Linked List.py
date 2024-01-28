# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import Optional
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def flatTree(node) : 
            if node is None : return None , None 
            elif not node.left and not node.right : return node , node 
            
            left_head , left_tail = flatTree(node.left) 
            right_head , right_tail = flatTree(node.right) 
            
            if left_head and right_head :  
                left_tail.right = right_head 
                node.left = None 
                node.right = left_head 
                return node , right_tail 
            
            elif left_head : 
                node.left = None 
                node.right = left_head 
                return node , left_tail
            
            elif right_head : 
                return node , right_tail
        flatTree(root)    