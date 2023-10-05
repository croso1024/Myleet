from typing import Optional ,List 
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

""" 
    這一題蠻有趣的 , 想像我們站在Binary tree的右邊 , 要求右邊看過去可以看到的所有節點 , 
    看起來就是要求 "每一層的最後一個節點" 
    
    直覺上第一個想法是做階層尋訪 , BFS或dict , 用dict只存每一層最後一個看起來比較簡單 
"""

""" 
    解法一. 
        使用dict的階層巡訪 , 求得每一個階層最後一個節點 , 
        基本上無論用前中後序來看節點 , ,同一階層都會由左往右 , 但這一題有特別說 ,
        我們給結果的順序要從上到下 , 因此使用pre-order才能確保深度表"建立的過程"由淺到深 
        (否則就要按照深度表的深淺順序來建立解)
"""
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        self.depthTable = dict() 
        self.depth = 0 
        
        
        #我們在前序,後序位置調整深度 , 更新depthTable的部份在此題必須要在前序位置
        # 基本上無論用前中後序來看節點 , ,同一階層都會由左往右  
        # ""
        def traverse(node) : 
            
            if node is None : return None 
            
            
            # pre-order : 調整depth 
            self.depth += 1 

            # 在對應深度更新當前的節點            
            self.depthTable[self.depth] = node 
            
            traverse(node.left)
            traverse(node.right) 
            
            # post-order : 
            self.depth -= 1 
            
        traverse(root) 
        
        #當我們traverse完成 , depthTable就保存了所有深度最靠外的節點 
        
        
        return [node.val for node in self.depthTable.values()]