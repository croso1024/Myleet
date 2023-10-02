# Definition for a binary tree node.

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

""" 
    我的原始想法: 透過檢查pre-order , post-order , in-order是否都相同 , 
    由於可能會有樹內的值都相同，但結構不同，所以特別加上一個 "structure" list來保存結構特性
"""
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        
        def structure_of_Tree(root): 
        
            pre_order = list() 
            in_order = list() 
            post_order = list() 
            structure = list()
        
            def traverse(node): 
                if node == None :
                    structure.append(0) 
                    return
                else : 
                    structure.append(1)
                
                pre_order.append(node.val) 
                traverse(node.left) 
                in_order.append(node.val)
                traverse(node.right) 
                post_order.append(node.val)       
        
            traverse(root)

            return [ pre_order , in_order , post_order,structure ]
        
        tree_1 = structure_of_Tree(p)
        tree_2 = structure_of_Tree(q) 
        
        return True if tree_1 == tree_2 else False 
    

""" 
    書上作者的想法，利用"拆解問題"的思路來處理,兩個Tree相同的話代表他們root相同,左右節點也都相同
"""
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # 一次Traverse 兩棵樹
        def sameTree(node1,node2) : 
            
            # 兩邊都走到空節點
            if node1 == None and node2 == None : 
                return True 
            # 兩個非空，且數值相同，繼續拆，使用post-order , 因為要結合左右子樹的結果來得到最終結果
            elif ( node1 and node2 ) and (node1.val == node2.val):
                return sameTree(node1.left , node2.left) and sameTree(node1.right , node2.right) 
            # 其他情況就一定是不同子樹
            else : 
                return False 
            
                
        return sameTree(p,q)         
        