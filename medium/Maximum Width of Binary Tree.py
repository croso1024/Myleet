
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

""" 
    解法一. 
        使用depth-table去紀錄每層第一次看到的節點index
        後續看到相同層的節點時透過index差值去更新最佳解
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque 
from typing import Optional
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # minIndex in 0 level is root , (index = 0)
        minIndex = {0:0}
        # solution that we need to update 
        solution = float("-inf")

        def traverse(node,index,depth): 
            nonlocal solution 
            if node is None : return  

            if depth in minIndex :   
                solution = max(solution ,  index - minIndex[depth] + 1 ) 
            else : 
                minIndex[depth] = index  
            
            traverse(node.left , index*2 , depth+1)
            traverse(node.right , index*2 + 1 , depth+1) 

            return 

        traverse(root, 0 ,0 ) 
        return solution 

""" 
        解法二 . 
            改為使用BFS , 使用每一層的第一個以及最後一個index來更新最佳解
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque 
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        queue = deque() 
        queue.append((root , 0))
        solution = 0

        while queue : 

            size = len(queue) 
            firstNodeIndex = queue[0][1]
            for _ in range(size): 

                node , index = queue.popleft() 

                solution = max(solution , index - firstNodeIndex + 1 )

                if node.left : 
                    queue.append( (node.left , index*2 ) )
                if node.right : 
                    queue.append( (node.right , index*2 + 1) ) 
            
        return solution
       

