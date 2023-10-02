from typing import Optional 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

""" 
    思路 :  
        這一題要找到最短長度 , 可以抽象為"找到root到leaf的最短距離" 。 
        
        可以透過兩種作法來處理 : 
        1. traverse並以外部變數紀錄深度 , 一旦到達一個leaf , 就更新目前找到的最短距離 , 此法相當於DFS
        2. 透過BFS框架,作到階層尋訪 ,如此一來第一個發現的leaf時就必然是離root最短的leaf

        這一題使用DFS或BFS各有優缺, 實際上這優缺也與DFS,BFS的本質有關        

        DFS透過遞迴一次只處理一個分支 , 因此要找到最短路徑會需要探訪整棵tree ,時間複雜度為O(N), 
        但相應的需要的空間複雜度頂多就是儲存recursion stack的O(h) 
        
        BFS齊頭並進尺李所有分支 , 因此不用走完整棵樹就能找到答案 ( 雖然最壞情況一樣要走O(N)  , 但大多時候效率更好 )
        然後BFS的空間複雜度較差 , 因為最多會需要保存到與答案那一層所在節點數相同的空間

"""
        
""" 
    解法一. DFS
"""        

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if root is None : return 0 

        # 只要有root , 起碼深度是1, 因為題目定義depth為 root到leaf經過的節點數
        self.depth = float("inf")
        depth = 1
        
        def traverse(node): 
            nonlocal depth
            if node is None : return None
            
            if node.left is None and node.right is None : 
                self.depth = min(self.depth , depth) 
            
            depth += 1 
            traverse(node.left)
            traverse(node.right) 
            depth-=1     
                
        traverse(root)
        
        return self.depth 
    

""" 
    解法二. BFS 
"""

from collections import deque

class Solution:
    
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if root is None : return 0
        
        queue = deque() 
        queue.append(root) 

        # 只有root的基本深度為1
        depth = 1 
        
        # 當queue還有內容時繼續 , 用for-loop對同一階層的節點進行尋訪 
        # 將該層節點的child加入queue以進行下一波尋訪 , 同時檢查每一個節點是否是我們要找的leaf 
        # 因為BFS的特性,我們所找到的第一個leaf深度就是解 , 就可以馬上return了 
        while queue :  

            # size代表了這個階層還有多少的節點要逐一尋訪             
            size = len(queue) 
            for item in range(size): 
                
                node = queue.popleft()
                
                if not node.left and not node.right : 
                    return depth 
                
                # 當這個節點還有child , 就將他們append到queue中 
                if node.left : queue.append(node.left)
                if node.right : queue.append(node.right) 
                
            depth += 1
        
        