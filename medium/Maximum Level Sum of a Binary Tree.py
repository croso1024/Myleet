# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

""" 
    思路: 
        給定Tree , 其中root節點代表第一層 , 要求 有著最大總和值的層中最低層的層數 , 
        看題目的例子, 就是返回同一層節點值最大的那一層 , 如果有兩層次一樣 , 返回較低的層
        
        這題就BFS或著depth-table都能解 , 我這邊用BFS
"""



""" 
    解法一. BFS , 速度就很不錯,空間稍微差一些
"""
from collections import deque

class Solution:

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        queue = deque() 
        queue.append(root) 

        best_sum = float("-inf")
        best_level = 0 
        
        cur_level = 0 
        
        while queue : 
            
            size = len(queue) 

            cur_level += 1

            # 紀錄當前這一層的sum
            level_sum = 0             
            
            for _ in range(size): 
                
                cur_node = queue.popleft() 
                level_sum += cur_node.val
                
                if cur_node.left : queue.append(cur_node.left) 
                if cur_node.right : queue.append(cur_node.right) 
        
            if level_sum > best_sum : 
                best_sum = level_sum 
                best_level = cur_level 
                
        
        return best_level
