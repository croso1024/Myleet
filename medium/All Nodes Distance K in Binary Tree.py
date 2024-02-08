# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
    解法一.
        Traverse一次Tree紀錄各個節點的parent , 待會要將這個tree當作Graph使用
        同時在上面traverse的途中去找尋目標節點 ,
        最後從目標節點開始展開BFS
"""
from collections import deque
from typing import List 
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = dict() 
        targetNode = None 
        def traverse(node):
            nonlocal targetNode
            if node.val == target.val : targetNode = node
            if node.left : 
                parent[node.left] = node 
                traverse(node.left) 
            if node.right : 
                parent[node.right] = node 
                traverse(node.right) 
        # complete covert the tree to graph 
        traverse(root) 
        
        # BFS From target node 
        queue = deque()
        queue.append(targetNode)
        visited = set()
        visited.add(targetNode)
        distance = 0
        while queue: 
            size = len(queue) 
            if distance == k :
                return [node.val for node in queue]

            for _ in range(size): 
                node = queue.popleft() 

                if node.left and not node.left in visited : 
                    visited.add(node.left)
                    queue.append(node.left)
                if node.right and not node.right in visited:
                    visited.add(node.right)
                    queue.append(node.right)
                if node in parent and not parent[node] in visited: 
                    visited.add(parent[node])
                    queue.append(parent[node])

            distance += 1 
        # if leave the while loop and not yet return , it's represent no any node satisfy the condition

        return [] 
        