
from typing import Optional , List 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
        
""" 
    思路 :
        這一題要求計算Binary Tree裡面各個階層的平均值 , 我的直觀想法是階層探尋 , 但此題為easy似乎有更直接的作法
"""

""" 
    解法一. BFS , 直接尋訪同一層級並且將該層級的平均值加入結果陣列
"""

from collections import deque

class Solution:

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        queue = deque()         
        result = [] 
        queue.append(root) 
        
        while queue : 
            
            average  = 0 
            size = len(queue) 
            # for迴圈使用size , 確保這個for-loop拿出來的都是同一個階層的節點
            # 我們針對該層初始化節點數與總和值用以計算加總
            for i in range(size): 
                
                node = queue.popleft() 
                average+=node.val
                if node.left : queue.append(node.left)
                if node.right : queue.append(node.right) 
                 
            # 當完成一層節點的traverse , 計算該層的和 
            result.append( average/size )
        
        return result    

""" 
    解法二. 仰賴dict的階層尋訪 , 為了要滿足排序 , 在pre-order位置操作
"""

class Solution:

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        # table: 
        # key : depth 
        # value : (node_num , sum)
        table = dict() 
        depth = 0 
        
        def traverse(node): 
            nonlocal depth , table 
            if node is None : return None 

            if depth in table : 
                table[depth][0] += 1 
                table[depth][1] += node.val 
            else : 
                table[depth] = [1 , node.val]
            depth += 1 
            traverse(node.left) 
            traverse(node.right) 
            depth -= 1 
        
        traverse(root)
        result = [] 
        # 透過pre-order 我們建立的table順序也會是由淺到深
        for value in table.values() : 
            
            result.append( value[1] / value[0]  )
            
        return result 