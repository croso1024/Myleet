""" 
    題意 : 
        透過preorder binary tree去建構一個數字帶有括號的數字字串 , 看example就是
        root(left_subtree)(right_subtree) 這個形式 
    
    思路 :
    
        這一題我認為有兩種解法 , traverse與recursion
        traverse作法的根本在於發現到 , 每次往child走 ,就要加一個'(' , 每次離開child就要加')'
        
        recursion的根本在於上面看到的 root(left_subtree)(right_subtree) 這個形式
        
        
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional

""" 
    解法一. traverse作法 , 在進入節點的時候加上 "(" , 離開時加上 ")"
"""
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        sol = "" 
        
        # 把檢查node是否存在放在進child的時候 ,方便對應這一題的邏輯
        def traverse(node): 
            nonlocal sol 
            
            sol += str(node.val)
            
            # 要離開節點了 , 補上 ")" 
            # 這一題前序後續的操作放在這裡 , 純粹是因為root沒有要被包住 , 寫在這裡讓從root開始call是正常運作
            if node.left : 
                sol += "("
                traverse(node.left) 
                sol += ")"
            if node.right : 
                # 加上這一行 , 因為這一題如果沒有left child但有right child的時候要為left保留一組括號
                if not node.left : sol += "()"
                sol += "(" 
                traverse(node.right) 
                sol += ")"
            
            return 
        
        traverse(root) 
        return sol 
        

""" 
    解法二. recursion , 答案形式為 root(left)(right)
"""
class Solution:

    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        
        # 遞迴產生形式為 root(left)(right) , 如果left child沒有但有right_child , 則要保留一個空位
        # 為了讓traverse()產生的能直接作為解 , 我們讓traverse(node)是產生 node(node_left)(node_right) 
        # 因此在括號是在手動內部加 , 而不是在return sol時候加        
        def traverse(node):
            if node is None : return node 
            
            sol = str(node.val)
            
            left_child = traverse(node.left) 
            right_child = traverse(node.right) 
            
            
            if left_child : 
                sol += "(" + left_child + ")" 
            
            if right_child : 
                
                if not left_child : 
                    sol += "()" + "(" + right_child + ")"
                
                else : 
                    sol += "(" + right_child + ")" 
            
            return sol 

    
        return traverse(root)
            
            
                
        
        