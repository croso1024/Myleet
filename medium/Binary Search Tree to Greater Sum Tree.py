""" 
    思路 : 
        這一題很妙 , 和Covert BST to Greater Tree一模一樣 , 
        連code都不用改 , 走反向的中序並且maintain一個外部變數
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
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