# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional



""" 
    思路:
        這一題要我們驗證兩個binary tree的 "leaf sequence" 是否相同 , 
        基本上就是由左到右的leaf所排出的順序是否相同 , 我最簡單的想法是traverse , 遇到leaf將其加入list 
        這樣就可以得到兩個tree的leaf sequence做比較 
        
        這個解法在速度上不是很優 , 但我認為就是常規上的時間複雜度最佳 , 主要是空間很差 遞迴+存list,
        
        我想空間上還有比較大的優化部份
        
"""
class Solution:

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        # 已知至少有一個node , 這邊不用node is None判斷 
        def traverse(node , res): 
            
            if not node.left and not node.right : 
                res.append(node.val) 
                return res 
            
            if node.left : traverse(node.left , res) 
            if node.right : traverse(node.right , res)   
            
            return res 
        
        return traverse(root1 , [] ) == traverse(root2 , [])
        
        
            
            
        