# Definition for a binary tree node.

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        


""" 
    思路一. :
        透過inorder尋訪,得到一個list代表"壓平後"的節點群 , 之後做list的對稱性比較
        --> 會遇到節點內相同，但結構不同，此時會出現錯誤
"""

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        self.node_set = list() 
        def traverse(node): 
            
            if node is None : return  
            
            
            traverse(node.left) 
            self.node_set.append(node.val) 
            traverse(node.right)
        
        
        traverse(root)
        
        # 只有一個節點必定對稱            
        if len(self.node_set) == 1 : return True 
        # 如果節點數是偶數個-> 必定不對稱 
        elif len(self.node_set) % 2  == 0 : return False 
        
        mid = (len(self.node_set)-1)//2
            
        
        return (  self.node_set[:mid] == self.node_set[mid+1:][::-1]  ) 
    
    
""" 
    思路二. 先做Tree的翻轉,在比較兩顆Tree是否一樣 -> 結合inverse tree & same tree兩題的結果
"""

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        # 把樹翻轉的部份,透過在post-order的位置去調換left/right child接在node上來完成
        def inverseTree(node): 
            if node is None : return None 
            left_child = inverseTree(node.left) 
            right_child = inverseTree(node.right) 
            node.left = right_child 
            node.right = left_child 
            return node 
        
        # 檢查兩棵樹是否相同，一次遞迴兩個樹來完成,在post-order拿到兩組child是否相同後的結果來計算
        def sameTree(node1,node2): 
            if node1 == node2 == None : return True 
            elif ( node1 and not node2 ) or ( not node1 and node2 ) : return False 
            elif not node1.val == node2.val : return False 
            
            left_same = sameTree(node1.left , node2.left) 
            right_same = sameTree(node1.right , node2.right) 
            return left_same and right_same 
        
        # 檢查一下,如果本就只有一個節點就是True 
        if root.left is None and root.right is None  : return True  
        if not root.left or not root.right : return False 
        
        
        
            