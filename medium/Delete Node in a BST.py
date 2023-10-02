# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        # 協助用來砍node , 在我們找到要砍的node後 ,用這個函數返回砍完遞補的子樹
        # 如果該node有left child , 找出以該left child為root的子樹中的最大節點來替換 
        # 如果該node有right child , 找出以該right child為root的子樹中的最小節點來替換 
        def delete(node): 

            if node.left : 

                prev = None 
                temp = node.left 
                while temp.right : 
                    prev = temp 
                    temp = temp.right 
                # temp 為left child為root的子樹中的最大節點 ,且必然沒有right child了 

                # 如果prev為None , 就代表原先左子樹本來就沒有right child,這樣就單純上提
                if prev is None : 
                    temp.right = node.right 
                # 如果prev不是None , 那就把temp的left child接在prev的right , 把temp上提
                else : 
                    prev.right = temp.left 
                    temp.left = node.left 
                    temp.right = node.right 
                return temp   

            elif node.right : 

                prev = None 
                temp = node.right 
                while temp.left : 
                    prev = temp 
                    temp = temp.left 

                if prev is None :
                    temp.left = node.left   
                else : 
                    prev.left = temp.right 
                    temp.right = node.right 
                    temp.left = node.left  
                return temp 
            
            else : None 


        # Step.1 find the target node 
        if root is None : return root 

        node = root 
        prev = None # 保存一個prev用來砍節點

        while node : 
            # 要往left child找 , 如果沒有left那就是找不到了,直接return原始的樹
            if node.val > key :
                if node.left : 
                    prev = node 
                    node = node.left 
                else : return root                   
            elif node.val < key : 
                if node.right : 
                    prev = node 
                    node = node.right 
                else : return root 
            
            # 找到目標節點 ,
            # Case.1 目標節點就是root , 則prev=None , 如果沒有child的話就直接返回None ,有child就隨便拉一個
            else:
                # root就是目標 , 直接return砍掉後的子樹
                if prev == None : 
                    return  delete(node)    
                # 目標是某個樹中的節點, 要把他和prev相連 
                else : 
                    subTree = delete(node) 
                    # prev.val > key代表後來是走到left後發現目標 
                    if prev.val > key : prev.left = subTree 
                    else : prev.right = subTree 
                    return root                       