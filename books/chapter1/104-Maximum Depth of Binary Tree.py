""" 
    此題為Binary Tree概念基本題 , 由Binary Tree可以引導出
    回溯法和DP兩種方式，同時也都能用在這一題。
"""
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
""" 
    解法一 . 採用回溯法,透過global variable紀錄數值,當我們走完整顆樹就可以得到答案
"""
class Solution1:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        solution = 0        
        depth = 0
        
        def traverse(node): 
            nonlocal depth , solution 
            if node is None : return 
            
            # 前序位置，準備往下進到新節點 
            # 因為要下探，所以當前深度+1 
            depth += 1 
            traverse(node.left) 
            traverse(node.right)
            # 後序位置，探索完該節點準備往上離開 
            
            # 對於最大深度的更新，可以放在depth增減中間的任何位置。
            if not node.left and not node.right  :
                solution = max(solution , depth)
            
            
            depth -= 1  
        
        traverse(root)  
        
        return solution 


""" 
    解法二 . 採用分治法，透過子問題的解來組合原始問題 ，即樹的深度等於左樹或右樹中較大的再+1
"""

class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def subTreeDepth(node , depth) :  
            
            if node is None : return depth 
            
            left_depth = subTreeDepth( node.left , depth )
            right_depth = subTreeDepth( node.right , depth )
            
            return max(left_depth , right_depth ) + 1 
    
        return subTreeDepth(root , 0 )            
            