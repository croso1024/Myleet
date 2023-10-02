# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.ans = float("-inf")
        
        self.oneSideMax(root) 
        
        return self.ans
        
    
    def oneSideMax(self,node) : 
        # base case 
        if not node : return 0 
        
        left_max = max(0 , self.oneSideMax(  node.left ) )
        right_max = max(0, self.oneSideMax( node.right ) )
        
        self.ans = max(self.ans , left_max+right_max + node.val)   
        
        return  max(left_max , right_max ) + node.val 
        
    
            