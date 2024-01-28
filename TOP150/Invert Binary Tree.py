# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
from typing import Optional
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # post-order位置 , 反轉兩個child-tree 
        
        def Invert(node): 
            if node is None : return None
            
            left_child = Invert(node.left)
            right_child = Invert(node.right) 
            
            node.left = right_child 
            node.right = left_child 
            
            return node  

        return Invert(root)
    

from typing import Optional

class Solution:
    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root is None : return None 
        
        left_child = self.invertTree(root.left) 
        right_child = self.invertTree(root.right) 
        
        root.left = right_child 
        root.right = left_child 
        
        return root 