from typing import Optional  , List 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
""" 
    我的思路 :  
    一個dict去保存每一個深度的list 
    pre-order , 進入節點前調整深度 , 之後可以在前序位置新增節點在對應深度的list
    在post-order離開的時候調整深度即可。
"""        

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        self.table = dict() 
        depth = 0 
        
        def traverse(node): 
            nonlocal depth 
            if node is None : return  
            
            ## pre-order , 調整深度 ,並將節點加入對應深度的list 
            depth += 1  
            
            if depth in self.table : 
                self.table[depth].append(node.val) 
            else : 
                self.table[depth] = [node.val]
            
            traverse(node.left)
            traverse(node.right) 
            ## post-order , 離開節點前要調整深度 
            depth -= 1 
            

        traverse(root)
        
        return [ i for  i in self.table.values() ]
""" 
        這一題可以應用BFS的樹階層尋訪框架 , 透過while迴圈探訪每個深度 , 
        在相同深度內使用for迴圈尋訪所有節點。  
"""
from collections import deque
class Solution:
    
    # 廣度優先搜索, 基於一個queue把所有尋訪到的節點產生的未拜訪節點加入queue
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        solution = [] 
        if not root : return []
        
        unvisited = deque()
        unvisited.append(root)
        
        while unvisited : 
            # 此size代表了"相同深度內有多少個節點"
            size = len(unvisited) 
            same_level = [] 
            
            for i in range(size) :  
                
                node = unvisited.popleft()  

                same_level.append(node.val)

                # 我們先檢查了child的存在才加入queue , 因此拿出來的時候不必檢查其存在性了                
                if node.left : unvisited.append(node.left) 
                if node.right : unvisited.append(node.right)
                    
            solution.append(same_level) 
        
        return solution
            
                
            

        
