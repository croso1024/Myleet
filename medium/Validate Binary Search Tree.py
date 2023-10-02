from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

""" 
    思路 : 
        一個有效的Binary tree , 其left_child必須是None或著小於自己 ,
        right_child則必須是None或大於自己 , 這一題應該是可以透過traverse以及分解問題兩種方式來解 
        
        - traverse : 前序檢查所有節點是否滿足BST , 並透過一個外部變量 : Valid作為flag 
        - 分解問題 : 在post-order先檢查左右子樹是否是BST , 自己與左右子樹的root是否滿足BST 做回傳
        - Inorder : 一個合理的Binary Search Tree : in-order的結果是一個sorted list 
"""


# 解法一. Traverse . 
# 作者有點出我犯的一個錯誤，就是只比較了左右兩個child ，但忽略了"右子樹的所有節點要大於root"與"左子樹的所有節點要小於root"這件事
# 解決方式是加入額外參數來紀錄這些訊息，但也因為這樣變成要Bottom UP的解，需要用分解問題的思路與post-order

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        self.Valid = True 
        
        def traverse(node): 
            if node is None : return None 
            
            # 前序檢查: 其child是否滿足BST : 
            if node.left and (node.left.val >= node.val) : self.Valid = False 
            if node.right and (node.right.val <= node.val ) : self.Valid = False 
            # 通過檢查 , 依照pre-order繼續尋訪 
            
            traverse(node.left) 
            traverse(node.right) 
            
        traverse(root) 
        
        return self.Valid    

""" 
    改良解法一. 
        透過傳入參數的Traverse來走, traverse接受三個參數,節點 , min_bound , max_bound , 
        我自己寫的時候思路幾乎都是"在一個節點上檢查其child" , 但東哥的思路寫起來比較類似"進入該節點的當下去判斷該節點是否在兩個bound"內 
        我想差別在於我的作法需要同時在同樣的一組bound下去檢查left,right ,比較複雜 ,
        而東哥版本只需要專住在當下進入的node是否滿足bound.
        
    關鍵想法在於,BST往下成長的過程中  ,bound是逐漸收縮的 , 
        因此當我們往左child找 , 右邊的bound變為當前節點 
        當我們往右child去找 , 左邊的bound變為當前節點 . 
"""
class Solution: 

    def isValidBST(self,root): 
        
        self.valid = True 


                
        def traverse(node, min_bound , max_bound): 
            
            if node is None : return
            
            # 進入了節點後檢查該節點是否滿足Bound    
            if not min_bound is None: 
                if not node.val > min_bound : self.valid = False 
            
            if not max_bound is None: 
                if not node.val < max_bound : self.valid = False
                
            # 往左child走 , 更新max bound ,即左子樹不能超過的值 
            traverse(node.left  ,min_bound , node.val  )
            # 往右child走 , 更新min bound ,即右子樹必須大於的值
            traverse(node.right , node.val , max_bound)
        
        traverse(root , None , None)

        return self.valid


""" 
    我自己想到的 解法二. Inorder檢查 , 但會需要用到sort , 而且我最後使用轉集合比較長度來檢查是否有重複元素，因此這個解法速度與空間都很差 
    
    --> 仔細想根本不需要sort , 透過in-order以O(n)的時間複雜度走完所有節點後 , 一個linear check確認所有list滿足遞增的性質即可
    
"""

class Solution:
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # phrase.1  in-order traverse and collect all node in list 
        self.sorted_nodes = list()
        def traverse(node):  
            
            if node is None : return 
            traverse(node.left)
            self.sorted_nodes.append(node.val)
            traverse(node.right)
            
        traverse(root)
        
        # phrase.2 check the ordinary ascending 
        if len(self.sorted_nodes) == 1 : return True 
        prev = self.sorted_nodes[0] 

        for i in self.sorted_nodes[1:] :  
            if i > prev : prev = i 
            else : return False 
        return True 
            
        
""" 
    在討論版上看到的版本 , 也是in-order , 但不需要O(n)空間 , 因為我們只需要記得inorder順序的前一個值
    -> 但是實際跑LeetCode的結果也沒有比上面好多少?? 也可能是這一次跑得比較差
"""

class Solution:
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        self.temp = float("-inf")        
        self.valid = True 
        
        def traverse(node):  
            if node is None : return 
            traverse(node.left)
            if not node.val  > self.temp : self.valid = False
            self.temp = node.val
            traverse(node.right)
            
        traverse(root)
        
        return self.valid