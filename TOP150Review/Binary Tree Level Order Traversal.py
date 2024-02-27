# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional , List 

from collections import deque
class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None : return []
        queue = deque() 
        queue.append(root) 
        sol = [] 
        
        while queue : 
            
            size = len(queue) 
            # maintain一個這一層的節點的array
            temp = [] 
            for i in range(size): 
                
                cur_node = queue.popleft() 

                temp.append(cur_node.val)
                
                if cur_node.left : queue.append(cur_node.left)
                if cur_node.right : queue.append(cur_node.right)
                
            sol.append(temp)
        
        return sol 



# level hashmap  , 我們一邊遞迴走訪這一棵樹 , 同時將相應深度的節點加入對應深度的array
class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        table = dict() 
        
        def traverse(node , depth): 
            if node is None : return None 
            
            # 在pre-order位置去將節點加入depth table
            if depth in table : 
                table[depth] .append(node.val)  
            else : 
                table[depth] = [node.val]

            traverse(node.left , depth+1)
            traverse(node.right , depth+1)
            
        traverse(root,1)
        
        # 依據python dict , 我們走訪時建構深度的性質 , 直接return table.values()就可 
        
        if table : 
            return table.values() 
        else : 
            return  []
        