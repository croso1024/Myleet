# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


# traverse整個tree,並在過程中檢查是否有節點違反BST性質 ,
# 為了做到檢查,在traverse的過程中要maintain左右bound 
# 當我們往左節點找 , 左節點必須小於當前節點 , 因此rightBound要進行更新 
class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        sol = True 


        def valid(node , leftBound , rightBound) : 
            nonlocal sol 
            if node is None : return None 
            if not sol : return 
            
            if leftBound < node.val < rightBound : 
                pass 
            else : 
                sol = False 
                
            # 往左節點走,更新rightBound
            valid(node.left  , leftBound , node.val)
            valid(node.right , node.val , rightBound) 

        valid(root , float('-inf') ,float('inf'))
        
        return sol 
                
            