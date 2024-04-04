# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional , List 

# BFS solution 
from collections import deque 
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None : return [] 
        queue = deque() 
        queue.append(root) 
        sol = list() 
        
        while queue : 
            
            size = len(queue) 
            # store the nodes in same level temporarily
            temp = [] 
            
            for _ in range(size) : 
                
                node = queue.popleft() 
                temp.append(node.val) 
                
                if node.left : queue.append(node.left) 
                if node.right : queue.append(node.right) 
            
            sol.append(temp)
            temp = [] 
        
        return sol 
                