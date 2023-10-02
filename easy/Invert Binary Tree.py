from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
""" 
    我的想法 :
    透過post-order由下而上去進行對調 , 並返回對調完成的自己 ,讓上面一層的節點再做對調
"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        def traverse(node): 
            
            if node is None : return
            
            left_subTree = traverse(node.left)
            right_subTree = traverse(node.right) 
            
            # post-order swap the tree 
            node.left = right_subTree 
            node.right = left_subTree
            
            return node 
            
        return traverse(root)        

""" 
    更快一點，使用原函數自己遞迴, 比前一個作法在空間與速度上都略有優勢。
"""

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]: 
        
        if root is None : return root 
        
        left_subTree = self.invertTree(root.left)
        right_subTree = self.invertTree(root.right) 
        
        root.left = right_subTree 
        root.right = left_subTree 
        
        return root  
    
    
""" 
    書本的解法有兩種，一種是如同前兩個，透過分解問題的方式來求解，
    而這一題也可以透過traverse的思維來做 , "即每當我們到達某個節點,就交換他的兩個child"
    
    實做起來雖然速度較另外兩個慢一點，但空間效率最好。
"""


class Solution: 
    def invertTree(self,root) : 
        
        
        # 在pre-order的位置操作 , 每次進入一個節點就做交換,走完整棵樹就做完了
        def traverse(node):  
            
            if node is None : return  
            # swap child 
            tmp = node.left 
            node.left = node.right 
            node.right = tmp 
            
            traverse(node.left)
            traverse(node.right)
        
        traverse(root)
        
        return root 