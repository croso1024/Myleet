# Definition for a binary tree node.

from typing import Optional 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


""" 
    思路 : 
        這一題所說的 "diameter" 指的就是左子樹最大深度+右子樹的最大深度和 ,
        並且不一定要穿過root  
        
        所以應該是用post-order , 取得每個節點左右子樹的深度後加總更新外部變數 , 
        這個問題使用traverse的作法 
        
        -> 確實這樣做時間空間就很不錯了
"""        
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        
        self.diameter = float("-inf") 
        
        # traverse函數返回以該節點為root的樹的高度(最大深度)
        # 我們定義leaf節點高度為1  
        # 在post-order位置取的左右sub-tree的高度來更新diameter並回傳 
        def traverse(node) : 
            
            if node is None : return 0
            
            left_height = traverse(node.left)
            right_height = traverse(node.right) 
            
            self.diameter = max(self.diameter ,  left_height+right_height  )
            
            return max(left_height , right_height) + 1 
        
        traverse(root) 
        
        return self.diameter
            