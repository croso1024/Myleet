# Definition for a binary tree node.
from typing import Optional 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
""" 
    思路:  
        traverse一遍,去找到每一個子樹的高度( leaf高度為1 )來回傳。 
        接著post-order讓sub-root比較左右兩個節點高度 , 如果高度差異>1即為unbalanced tree
        
        --> 結果論來說這個作法時間與空間都很優異
"""

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.balanced = True 
        
        def nodeHeight(node):  
            # 空節點高度為0,leaf高度為1
            if node is None : return 0 
            
            
            left_height = nodeHeight(node.left)
            right_height = nodeHeight(node.right)  
            
            if abs(left_height-right_height) > 1 : self.balanced = False 
            
            # 一個節點的高度為左右子樹中較高的高度值 + 1 
            return max(left_height , right_height) + 1 
        
        nodeHeight(root) 
        
        return self.balanced
            
            
