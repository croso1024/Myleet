# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

from typing import List , Optional
from collections import deque
class Solution:

    # BFS 
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None : return []
        queue = deque() 
        queue.append(root) 
        sol = [] 
        
        LTR = True
        
        while queue : 
            
            size = len(queue) 
            temp = [] 
            for i in range(size): 
            
                cur_node = queue.popleft() 
                temp.append(cur_node.val)
                
                if cur_node.left : queue.append(cur_node.left)
                if cur_node.right : queue.append(cur_node.right) 
            
            if LTR : 
                sol.append(temp)  
            else : 
                sol.append(temp[::-1])
            LTR = False if LTR else True 
        
        return sol 