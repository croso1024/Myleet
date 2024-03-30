# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List , Optional

class Solution:
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        
        def build(preorder:list , inorder:list):  
            
            if len(preorder) == 0 : return None  
            
            rootIndex = inorder.index(  preorder[0]  )
            
            root = TreeNode(val = inorder[rootIndex]) 
            left_sub_tree = build( preorder[1:rootIndex+1]   , inorder[:rootIndex]   )
            right_sub_tree = build(  preorder[rootIndex+1:] , inorder[rootIndex+1:]  )
            
            root.left = left_sub_tree 
            root.right = right_sub_tree 
            
            return root 

        return build(preorder , inorder)