# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    
    
    # 走節點的過程中 maintain 左右邊界
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        sol = True 
        
        
        # 遞迴去驗證該節點是否合法 , 節點的值必須要 > left_bound , < right_bound
        # 在我們往left child走得時候 , 更新right-bound , 反之亦然
        def valid(node , left_bound , right_bound) : 
            nonlocal sol 
            if node is None : return None 
            
            
            # pre-order位置先進行有效性驗證 , 通過後再來遞迴
            if (not  node.val > left_bound ) or (not node.val < right_bound) : 
                sol = False   
            
            # 如果已經驗證到無效就不用再遞迴了 
            if sol :
                
                valid(node.left  , left_bound , node.val )
                valid(node.right , node.val , right_bound) 
        
        valid(root , float("-inf") , float("inf") )
        
        return sol 
