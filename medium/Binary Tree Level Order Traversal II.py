""" 
    Simplest solution is BFS and reverse the store list to achieve bottom-up traverse

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None : return []

        queue = deque() 
        queue.append(root) 
        solution = []

        while queue : 

            size = len(queue) 
            level_traverse = [] 

            for _ in range(size): 

                node = queue.popleft() 
                level_traverse.append(node.val) 

                if node.left : queue.append(node.left)
                if node.right : queue.append(node.right) 
            

            solution.append(level_traverse)
        
        return solution[::-1]