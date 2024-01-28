# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional 


""" 
    思路 : 
        我的概念是使用分解問題的思路 , 每一次遞迴函數返回的會是以該節點為起始的最大zigzag長度 , 
        在我們取得以left,right child為起始的最大zigzag長度後就可以計算以當前節點為起始的最大zigzag長度 , 
        因為最大zigzag長度的起始不一定會發生在原始的root , 因此我們透過一個外部變數,去追蹤遞迴過程的最大值
"""

""" 
    解法一. 
        上面的思路已經定義了大致的框架  , 不過在我實做的時候想到要去計算自身節點的最長長度 , 
        會需要去考量child的延伸方向 , 對left child來說在計算自身長度時就需要left_child往右延伸的最大長度 ,
        因此更改遞迴函數的定義變成回傳該節點 往左以及往右的最大zigzag長度  
        
        速度普通 , 但也是O(N)級別 , 空間很優
        
"""
class Solution:

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        sol = float("-inf") 
        
        
        # 返回以node為起始 , 往左以及往右的最大zigzag長度
        def longestWithNode(node):
            nonlocal sol
            # zigzag長度定義為拜訪到的節點-1 , 如果為None 則為-1
            if node is None : return -1 , -1 
            
            # 去取得以左右子樹為起點的最長zigzag長度
            
            _ , left_child_R = longestWithNode(node.left)
            right_child_L , _ = longestWithNode(node.right)  
            
            # 計算自身節點的最大zigzag長度 ,
            
            # 從自身出發 , 往左的最大長度為left child往右的最大長度 + 1
            # 從自身出發 , 往右的最大長度為right child往左的最大長度 + 1 
            node_L = left_child_R + 1 
            node_R = right_child_L + 1 
            
            # 在過程中更新sol 
            sol = max(sol , node_L , node_R)  
            
            return node_L , node_R 
        
        longestWithNode(root) 
        
        return sol 
            