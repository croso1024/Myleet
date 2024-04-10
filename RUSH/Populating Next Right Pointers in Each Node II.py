# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: Node = None, right: Node = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

# BFS 

from collections import deque 

class Solution:

    def connect(self, root) :
    
        if root is None : return None 
        
        queue = deque() 
        queue.append(root) 
        
        while queue:         
            
            size = len(queue) 
            # connect the right pointer 
            for i in range(size-1):
                queue[i].next = queue[i+1]
            
            for _ in range(size): 
                
                node = queue.popleft() 
                
                if node.left : 
                    queue.append(node.left)
                if node.right : 
                    queue.append(node.right) 
                
        return root 