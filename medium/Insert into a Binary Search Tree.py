# Definition for a binary tree node.


"""  
    思路 :  
        給定一個BST以及一個新值 , 將新節點插入在BST中 , 並遣確保插完後 , 
        仍然維持BST. 注意這個插入值可以有很多種實現方式 , 只要確保完成的樹是包含新的值 , 然後仍是BST 
        
        我看一下 , 感覺根本不必要維持balanced , 所以直接插就好
"""

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        new_node =  TreeNode(val=val) 
        if root is None : return new_node
        
        # 找位置
        probe = root  
        prev = None 
        while probe : 
            
            # 題目有說明不會有任何節點的值等於val
            if probe.val > val : 
                prev = probe 
                probe = probe.left  
            else : 
                prev = probe 
                probe = probe.right
        
        # 一旦跳到出來 , 那就代表這個位置就是要插入的
        # 因為我們已經避開root為None的情況 , 這邊就是檢查prev.val 和val的大小 , 再將新節點插入
        if prev.val > val :  
            prev.left = new_node 
        else : 
            prev.right = new_node 

        return root 
        