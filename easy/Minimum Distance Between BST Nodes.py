""" 
    思路 : 
        透過in-order順序traverse整顆樹 , 透過in-order順序尋訪 , 計算相鄰兩個節點的值

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        sol = float("inf") 
        lastNode = None 
        
        def traverse(node): 
            nonlocal lastNode , sol 
            if node is None : return node 
            traverse(node.left) 
            
            if lastNode : 
                sol =  min( sol , abs( lastNode.val - node.val ) )
                lastNode = node 
            else : 
                lastNode = node 
            
            traverse(node.right) 
        
        traverse(root) 
        
        return sol 