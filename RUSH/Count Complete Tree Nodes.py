# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

# 用低於O(N)的時間複雜度去計算complete tree的節點數量 , 
# complete binary tree除了最後一層以外每一層的節點數都等於 2^n , 
# 所以計算的方式,假設最後一層為n , 則總節點數 = 2 + 2^1 + 2^2 + ... 2^(n-1) + 最後一層節點數

class Solution:

    def countNodes(self, root: Optional[TreeNode]) -> int:
    

        def count(node) : 
            
            if node is None : return 0 
            
            return 1 + count(node.left) + count(node.right) 
        
        return count(root)
            