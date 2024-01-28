""" 
    思路 : 
        題目告知所有的node.value都是unique , 但這一題的tree不是binary search tree , 因此無法直接用 logN 定位到目標 
        比較直觀的方法可能是traverse整個樹 , 並keep他們一路上的軌跡 (不能遇到target就return , maybe 另外一個目標在第一個目標之下)

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


""" 
    解法一. 
        Traverse這棵樹 , 並給一個track代表軌跡 , 在進出節點的位置操作  , 這個解法在速度與性能上都不太好
        
"""
class Solution:
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # trajectory 用來保存兩個目標點的軌跡
        trajectory = {p.val :None , q.val:None}

        # track用來紀錄走到目前節點node , 他一路走來的軌跡
        def traverse(node, track):  
            
            if node is None : return 
            
            # 找到目標一 OR 目標二  , 將目前為止的軌跡加入 
            elif node.val == p.val or node.val == q.val:

                trajectory[node.val]  = list(track) + [node]
            
            # pre-order處 : 把自身節點加入track再往下走
            track.append(node) 
            traverse(node.left , track) 
            traverse(node.right, track) 
            # post-order處 , 要pop掉自己再返回
            track.pop() 
            
        # traverse完成後 , 兩個目標節點的軌跡就被拿到了 
        traverse(root , [])
        
        
        # 有了兩個目標節點的軌跡就可以算LCA , LCA就是從頭開始 , 兩個軌跡一同前進 , 遇到了不同的結果or其中一個為空的情況
        
        # trajectory最短的情況就是在root , 因此至少len(trajectory) >= 1 
        probe1 = 0 
        probe2 = 0 
        
        track1 = trajectory[p.val]
        track2 = trajectory[q.val]
        
        while probe1+1 < len(track1) and probe2+1 < len(track2) : 
            
            if track1[probe1+1] == track2[probe2+1] : 
                
                probe1 += 1 
                probe2 += 1 
            
            else : 
                # 這個節點至少會是root 
                return track1[probe1]
        
        
        # 當其中一個走完了 , 另外一個還有,則代表走完那個array的最後一個值就是LCA 
        if probe1+1 < len(track1) : 
            return track2[len(track2)-1]
        else : 
            return track1[len(track1)-1]
             
            
            
        