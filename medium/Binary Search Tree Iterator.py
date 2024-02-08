# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = list() 
        self.probe = root 

        while self.probe.left : 
            self.stack.append(self.probe)
            self.probe = self.probe.left  

    def next(self) -> int:
        
        returnNode = self.probe 

        # Fallback , check out the node in stack top , 
        if self.probe.right : 
            
            self.probe = self.probe.right 

            while self.probe.left : 
                self.stack.append(self.probe) 
                self.probe = self.probe.left 

        # no any more left child 
        else : 
            
            if self.stack :  
                self.probe = self.stack.pop() 
            
            else : 
                self.probe = None 
        
        return returnNode.val

    def hasNext(self) -> bool:
        return not self.probe is None


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()