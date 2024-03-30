# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
from typing import Optional
from collections import deque

class Solution:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        queue = deque() 
        queue.append(root) 
        
        def checkSymmetric(q): 
            
            left = 0 
            right = len(q) - 1 
            while (left < right):
                
                if q[left] is None and q[right] is None : 
                    left += 1 
                    right -= 1

                elif q[left] is None or q[right] is None : return False 

                elif  q[left].val == q[right].val : 
                    left += 1 
                    right -= 1
                else : 
                    return False 
            return True 
        
        while (queue): 
            
            if (not checkSymmetric(queue) ): return False 
                
            size = len(queue)
            
            for _ in range(size): 
                
                node = queue.popleft() 
                if node : 
                    queue.append(node.left)
                    queue.append(node.right) 
        
        return True             


class Solution:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def mirror(node1,node2): 
            if node1 is None and node2 is None : return True 
            elif node1 is None or node2 is None : return False 
            
            if (node1.val == node2.val): 
                
                return mirror(node1.left , node2.right) and mirror(node1.right , node2.left)   
            
            else : 
                return False 
        
        return mirror(root , root) 