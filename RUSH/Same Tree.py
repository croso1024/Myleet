# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        
        def traverseBoth( node1 , node2 ):
            if (node1 is None and node2 is None): return True 
            elif (node1 is None or node2 is None): return False 
            elif (node1.val != node2.val):return False 
            
            
            return traverseBoth(node1.left , node2.left) and traverseBoth(node1.right , node2.right)
    
        return traverseBoth(p,q) 
    
                
                
                
        