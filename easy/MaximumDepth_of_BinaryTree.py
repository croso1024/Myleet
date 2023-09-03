from typing import Optional 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root :  return 0 

        self.maximum_depth = 0  
        def recursion(sub_root , depth) : 
            # base case : leaf 
            self.maximum_depth = max(self.maximum_depth , depth)

            if not sub_root.left and not sub_root.right : 
                return depth
            elif sub_root.left and not sub_root.right : 
                recursion(sub_root.left , depth+1)
            elif sub_root.right and not sub_root.left : 
                recursion(sub_root.right , depth+1)
            else :
                recursion(sub_root.left , depth+1)
                recursion(sub_root.right , depth+1)
        
        recursion(root , 1)
        return self.maximum_depth