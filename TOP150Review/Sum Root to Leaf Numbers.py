# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


# 思路: 在遞迴過程中keep當前的"字串累積" , 當走到left_node , 就將值轉回int加在外部變數
# 給定題目至少有一個節點
class Solution:
    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        sol = 0
        
        # 後面走到的節點,他們的數字要加在後方 
        def traverse(node:TreeNode , acc:str): 
            nonlocal sol             
            
            # 如果沒有child(在left , 就將這條path的累計加入) 
            if not node.left and not node.right :  
                sol += int(acc) 

            if node.left : 
                traverse(node.left  , acc+str(node.left.val)  )
            if node.right : 
                traverse(node.right , acc+str(node.right.val) )
        
        traverse( root , str(root.val) ) 
        return sol 
    

# DFS  , 走到left的時候把當前stack的所有值 join 起來
from typing import List 


class Solution:
    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        post_order = []
        stack = [] 
        stack.append(root) 
        
        while stack : 
            
            cur_node = stack[-1]
            
            if not cur_node.left and not cur_node.right : 
                stack.pop() 
                post_order.append(cur_node)
            
            if cur_node.left : stack.append(cur_node.left) 
            if cur_node.right : stack.append(cur_node.right) 
            
            cur_node.left = None 
            cur_node.right = None 
                
                
        print(post_order)
        
        return 