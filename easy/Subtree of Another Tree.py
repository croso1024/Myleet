# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

""" 
    思路:
    
        給定兩個tree , 分別為root 和 subroot , 需要去確認說subroot是否是root所根的tree中的子樹 , 
        換句話說除了要在root中找到subroot這個節點,也要進一步確認他們是否形成一樣的tree  . 
        
        解這一題的工作我認為大概有兩個部份 , 但不曉得為啥這一題在easy , --
        以tree代表主要的樹,subtree代表題目給定,我們要找的tree ,
        第一個部份是要找到tree中和subtree的root相同值的節點 
        第二個部份是傳入兩個tree , 比較其結構是否完全相同的函數 
        但這樣做很可能讓時間複雜度爆掉到O(N^2) 
        
        
        另一個作法可能是可以透過in-order , 如果兩個節點的結構相同 , 則inorder也應該有片段相同
        --> 這個概念是錯的 , 一個有著 left/right child的root和相同值的subroot但只有其中一個child也會有一樣的inorder , 但不是sub tree 
        
"""


""" 
    解法一. 這邊實做第一種解法 , 先找到tree中值和subroot一樣的 , 再透過令一個function進行比較
    
    這個作法可行 , 但就是worse case要O(N^2) , 因此時間不佳 , 另外空間也不佳 , 
    但看提交區似乎這一題就是O(N^2) ( 準確說是 O( mainTree + subTree   ) )
"""

class Solution:

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        
        # 傳入兩個node , 比較以他們形成的子樹是否相同
        def sameTree(node1,node2): 
            
            if node1 is None and node2 is None : return True 
            elif node1 is None  or node2 is None  : return False   
            
            if node1.val != node2.val : return False 
            
            # 值一樣的話就要比較他們左右的tree是否也一樣 
            same_left = sameTree(node1.left , node2.left) 
            same_right = sameTree(node1.right , node2.right)
            
            
            #如果左右都一樣才能回傳True 
            if same_left and same_right : return True 
            else : return False 
            
        # traverse主要的tree , 遇到值與subroot一樣就call sameTree 
        sol = False 

        def traverse(node): 
            nonlocal sol 
            if node  is None : return None 
            elif sol : return None 
            
            
            if node.val == subRoot.val : 
                sol = sameTree(node , subRoot) 
            
            traverse(node.left)
            traverse(node.right)
        
        traverse(root) 
        
        return sol 
                
            
            
            
            
            
            