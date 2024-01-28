# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

""" 
    思路: 
        給定兩個binary tree , 將兩個tree進行合併 , 
        合併的規則相當於將兩個tree "疊在一起" , 有節點重疊的部份將他們的值相加 , 只有其中一棵樹有節點的部份就沿用
        
        我的想法是分解問題的思路 , 一個指針在第一棵tree上遊走 , 如果兩棵樹都有left/right child才往下遞迴 , 否則直接接上不是None的那一棵就可 
        遞迴函數傳入兩個節點 ,回傳以傳入節點為root合併出來的結果
"""


""" 
    解法一. 就是上述思路 , 速度普通 , 空間不錯  , 程式碼結構本身還可以優化一些
"""
class Solution:
    
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        if root1 is None : return root2 
        elif root2 is None : return root1 
        
        
        def merge(node1 , node2): 
            
            # 如果兩棵樹在該節點都有值 , 建立一個新的合併node作為回傳 
            node = TreeNode(val=node1.val + node2.val) 
            
            # 如果兩個都有left_child 才要遞迴left_child , right_child同理 
            if node1.left and node2.left : 
                merged_left = merge(node1.left , node2.left)   
            else : 
                merged_left = node1.left if node1.left else node2.left   
                
            if node1.right and node2.right : 
                merged_right = merge(node1.right , node2.right) 
            else : 
                merged_right = node1.right if node1.right else node2.right
                
            node.left = merged_left 
            node.right = merged_right 
            
            return node 
            

        return merge(root1 , root2) 
    

""" 
    解法二. 嘗試去稍微優化一下程式碼結構 , 但整體性能與上面的差不多
"""
class Solution:
    
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def merge(node1 , node2): 
            
            if node1 is None : return node2
            elif node2 is None : return node1 
            
            # 如果兩棵樹在該節點都有值 , 建立一個新的合併node作為回傳 
            node = TreeNode(val=node1.val + node2.val) 
            
            # 如果兩個都有left_child 才要遞迴left_child , right_child同理 
            node.left = merge(node1.left , node2.left)   
            node.right = merge(node1.right , node2.right) 
            
            return node 
            

        return merge(root1 , root2) 