from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        

""" 
    思路 : 
        要把一個Binary Tree展開成Linked list 並且按照pre-order的順序 , 並且要求in-place
        
        最naive的想法當然是直接pre-order一次把節點存入list 
        再O(n)建立linked list , 這麼做會是O(N)時間與O(N)空間 , 就算是in-place也可以這樣做 
        
        follow up要求使用O(1)的空間來做
"""        


""" 
    解法一. 就先做最直覺的pre-order traverse後建立linked list 
"""
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.preOrderList = list() 

        def traverse(node): 
            if node is None : return 
            self.preOrderList.append(node) 
            traverse(node.left)
            traverse(node.right) 

        traverse(root)             
        if len(self.preOrderList) <= 1 : return root
        
        for idx in range(0 ,len(self.preOrderList)-1) : 
            
            self.preOrderList[idx].left = None 
            self.preOrderList[idx].right = self.preOrderList[idx+1]
        
        self.preOrderList[-1].left=None
        
        return self.preOrderList[0] 

""" 
    解法二 . 依據東哥的思路,這一題也可以使用分解問題的想法來做， 
            即使用一個post-order的遞迴函數 , 其功能是拉平一個二元樹(拉成和題目要求一樣的) 
            
            其中的關鍵在於要怎樣定義這個遞迴函數
            假設一個最簡單總共三個節點的二元樹 ,要把他拉平成題目要的模式(按照pre-order順序拉平) ,則 : 
            
            將右child接在左child的右邊 , 在把左child接在原節點的右邊
            ( 仔細想一下應該要一個tmep 先保存左child的右邊整條 , 不然會導致遞迴中途已經形成一條的左child斷掉 )

            如此一來post-order遞迴的把所有子樹拉成平的 , bottom-up的構成了完全平的Tree(Linked List)
"""

class Solution:
    
    def flatten(self, root: Optional[TreeNode]) -> None:
        
        if root is None : return root 
        
        left_child = self.flatten(root.left) 
        right_child = self.flatten(root.right)  
        
        # 交換的順序是比較關鍵的問題 , 用一個temp保存右方linked-list的head
        # 接下來將左邊linked-list接在原節點右邊 , 然後往下走到端點把temp接回去 
        temp = right_child 
        
        root.right = left_child 
        # 記得要把left切掉
        root.left = None
        # temp2的while迴圈結束後 , 他就來到了最後一個節點上,可以去接temp
        temp2 = root
        while temp2.right :  
            temp2 = temp2.right 
        temp2.right = temp 
        
        return root 
        
        
        
        