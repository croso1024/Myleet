# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import Optional , List

# BFS 解 , level order traverse 
from collections import deque
class Solution:
    
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        queue = deque() 
        queue.append(root) 
        sol = [] 
        
        while queue : 
            
            size = len(queue)  
            # level_sum : 這一層tree的總和
            level_sum = 0 
            
            for i in range(size): 
                
                cur_node = queue.popleft() 
                level_sum += cur_node.val
                
                if cur_node.left : queue.append(cur_node.left)
                if cur_node.right : queue.append(cur_node.right) 
            
            # 加入這一層的平均值 
            sol.append( level_sum/size  )
        
        return sol 