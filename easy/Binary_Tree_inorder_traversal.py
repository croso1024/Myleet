# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root) :
        self.result = [] 
        self._inorderTraversal(root)
        return self.result 
    
    def _inorderTraversal(self,node) :
        if not node is None : 
            self._inorderTraversal(node.left) 
            self.result.append(node.val)
            self._inorderTraversal(node.right)
        else: 
            return None 
        return None