
""" 
    思路 : 
    
        這一題蠻有趣的 , 給定一個嚴格BST , 我們要把讓樹的每個節點都加上所有大於自身節點值的數字 
        從上面的敘述來看 , 我們也希望拜訪節點的順序由大到小 
        即反過來使用in-order  , RDL 的尋訪 
        尋訪過程maintain目前的累積sum , 用以在每一個節點都用來做++ 
        
        重要時機點大概是這樣 : 
        1. 進入一個節點時是帶著當前的累積值 
        2. 在in-order處將累積值加在自身的節點上 (先保留一個temp紀錄原始值)
        3. 接下來要往左邊child走之前 , 調整acc 
        
        
"""

""" 
    解法一. 
        就是遞迴, 按照上面的規則走RDL去處理 , O(N)時間 O(1)空間
        看結果時間還行 , 空間超優 , 應該是大多數人都用O(N) array去保存
"""

# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # 這個acc 會 keep尋訪過程的總和 , 我們把他定義在外部變數
        acc = 0 
        
        def traverse(node): 
            nonlocal acc 
            if node is None : return 
            
            # 帶著當前的累積值進去 , 注意這一題是RDL順序
            traverse(node.right)  
            
            # 在in-order的位置去將自身的值做個++ 
            temp = node.val 
            node.val  += acc 
            acc += temp 
            traverse(node.left) 
        
        traverse(root)
        return root 