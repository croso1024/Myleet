""" 
    思路 : 
        這一題要計算tree中 "Good Node"的數量 , Good node的定義是從root到該node的整條路徑上沒有其他節點大過他 
        直觀想法是traverse整顆tree , 在尋訪的過程中去keep目前位置的最大值就好
"""

""" 
    解法一. 走traverse的思路走完整棵樹 , 在進入與離開操作目前路徑的最大值就可以了
    這個解法的時間是O(N) ,  空間等於遞迴的堆疊數量 , 但看起來實際結果空間與時間都不太優 , 
    針對初始path_max可以做一個修正
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        good_nodes = 0 
        
        # path_max 是目前尋訪到此的最大數值 
        # 這一題更新是否為good node數量這件事在 pre-order / in-order / post-order都可  
        # 我就在pre-order處做這件事
        def traverse(node , path_max): 
            nonlocal good_nodes 
            if node is None : return 
            
            if path_max is None : 
                path_max = node.val 
                good_nodes += 1 
            
            elif node.val >= path_max : 
                good_nodes += 1 
            
            traverse(node.left , max(path_max , node.val)) 
            traverse(node.right , max(path_max , node.val)) 
            
        
        traverse(root, None) 
        return good_nodes

""" 
    解法二. 
        針對初始path-max 做一個簡單修正來嘗試加速 
        -> 速度有略為提昇 , 反而空間提昇不少
"""

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        good_nodes = 0 
        
        # path_max 是目前尋訪到此的最大數值 
        # 這一題更新是否為good node數量這件事在 pre-order / in-order / post-order都可  
        # 我就在pre-order處做這件事
        def traverse(node , path_max): 
            nonlocal good_nodes 
            if node is None : return 
            
            if node.val >= path_max : 
                good_nodes += 1 
            
            traverse(node.left , max(path_max , node.val)) 
            traverse(node.right , max(path_max , node.val)) 
            
        
        traverse(root, float('-inf')) 
        return good_nodes
