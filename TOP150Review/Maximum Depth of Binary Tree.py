# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional

# traverse的走法 
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        max_depth = 0
        
        def traverse(node , depth ): 
            nonlocal max_depth  
            if node is None : return None 
            
            max_depth = max(max_depth ,  depth)
            
            traverse(node.left , depth+1) 
            traverse(node.right , depth+1) 
        
        traverse(root , 1) 
        
        return max_depth


# 分解問題的想法 ,  節點的深度等於其左右子樹深度比較大的+1 

class Solution:
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # 返回以node為root的樹最大深度 
        def subTreeDepth(node): 
            # 空節點的深度為0 
            if node is None : return 0
            
            left_depth = subTreeDepth(node.left)
            right_depth = subTreeDepth(node.right)  
            
            # 以node為root的樹, 深度為左或右子樹中深度較大的+1
            return max(left_depth , right_depth) + 1 
        
        return subTreeDepth(root)
    
