from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
""" 
    思路 : 
        用inorder就可以得到一個按照順序的值 , 這裡兩種作法 :
        1. 把值保存在list內 , 接著取出第k個就是第k小的值
        2. 初始化一個外部變數k , 並且在每次inorder找到值調整k ,一旦k值等於0就找到了,並且可以跳過後續traverse
"""


""" 
    解法一. 
        存list , 找第k個
        --> 速度略慢 , 空間反而還不錯
    
"""
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.sorted_list = list() 
        
        def traverse(node): 
            if node is None : return 
            
            traverse(node.left)
            self.sorted_list.append(node.val)
            traverse(node.right)
        
        traverse(root) 
        
        return self.sorted_list[k-1]

""" 
    解法二. 
        外部變數k , 透過調整k來解 
        --> 速度也略慢一點點 , 空間更加優
"""

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int: 
        
        self.k = k  
        self.sol = None 
        
        def traverse(node):
            if node is None : return 
            
            traverse(node.left)
            self.k -= 1 
            if self.k == 0 : self.sol = node.val
            traverse(node.right)
            
            
        traverse(root) 
        
        return self.sol
    
""" 
    微調解法二. 提早結束遞迴  ,速度跟空間都優
"""

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int: 
        
        self.k = k  
        self.sol = None 
        
        def traverse(node):
            if node is None : return 
            if not self.sol is None : return 
            traverse(node.left)
            self.k -= 1 
            if self.k == 0 : self.sol = node.val
            traverse(node.right)
            
            
        traverse(root) 
        
        return self.sol