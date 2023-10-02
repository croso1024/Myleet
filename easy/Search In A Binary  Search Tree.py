from typing import Optional
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
""" 
    這一題就做一般的Binary Search , 但只需要往下探索 , 不需要考慮尋訪整個Tree ,
    因此往下走的過程遇到None就是沒有找到了。 

"""        
class Solution:

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        
        def traverse(node) : 
            
            # 如果遇到None代表找不到了 , 否則至少有找到節點
            if node is None : return None 
            
            
            # 找到了目標 
            if node.val == val : return node 
            else : 
                # 要往左子樹去找 
                if node.val > val : 
                    return traverse(node.left)
                # 要往右子樹去找 
                else : 
                    return traverse(node.right)
                
        return traverse(root)
        
        
            