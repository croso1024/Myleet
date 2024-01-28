
""" 
    思路 :  
        給定一個binary tree , 要求在最底層的最左邊節點 (先找最底層 , 再找最底層中最左邊的)

        這一題就是走一個traverse的思路 , 去maintain變數depth , node ,
        一旦走到一個新的深度 , 就去更新第一個到達該深度的node , 之後走正常LDR , traverse結束
        
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional




class Solution:

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        depth = -1 
        sol = None 
        
        def traverse(node,cur_depth) : 
            nonlocal depth , sol 
            
            if node is None : return 
            
            if cur_depth > depth : 
                depth = cur_depth
                sol = node 
            
            traverse(node.left , cur_depth+1) 
            traverse(node.right, cur_depth+1) 

        
        traverse(root , 0)
        
        return sol.val 