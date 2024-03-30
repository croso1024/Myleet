# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional  , List 

class Solution:

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
    
        # store structure : depth:[amount of nodes in this depth , totalvalue]
        depthTable = dict() 
    
        def traverse(node ,depth):

            if node is None : return 
            
            if depth in depthTable : 
                depthTable[depth][0] += 1 
                depthTable[depth][1] += node.val 
            else:
                depthTable[depth] = [1 , node.val] 

            traverse(node.left , depth+1)
            traverse(node.right , depth+1) 

        traverse(root , 0)
        level = 0 
        answer = []
        while (level in depthTable):
            
            answer.append( depthTable[level][1] / depthTable[level][0] ) 
            level += 1 
        
        return answer 