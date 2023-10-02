from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    


""" 
    Solution1  O(1) Space complexity , 但速度慢
"""
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        # 要更換的第一個 , 第二個目標 , 以及inorder的sorted-array的前一個元素
        self.target1 = None
        self.target2 = None
        self.prev = None 
        
        def in_order(node): 
            
            if not node : return 
            
            in_order(node.left) 
            # In-order traversal 
            
            if not self.prev : 
                self.prev = node  
            elif self.prev.val <= node.val : 
                self.prev = node 
            else :  
                
                if self.target1 == None : 
                
                    self.target1 = self.prev 
                    self.target2 = node 
                    self.prev = node 
                
                else : 
                    
                    self.target2 = node 
                    # self.prev = node 

            
            in_order(node.right)
        
        in_order(root) 
        
        # swap : 
        
        self.target1.val , self.target2.val = self.target2.val , self.target1.val
        
        
            

""" 
    Solution2  簡單解法,不考慮space complexity
"""
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.val_list = [] 
        self.node_list = [] 
        
        
        def in_order(node): 
            
            if not node : return 
            in_order(node.left)
            self.node_list.append(node)
            self.val_list.append(node.val) 
            in_order(node.right) 
        
        in_order(root)
        
        l,r = 0 , len(self.node_list) - 1 
        
        # 從左到右 ，找違反遞增規則的節點 
        while l <= len(self.node_list) - 2  : 
            if self.val_list[l] <= self.val_list[l+1] : 
                l += 1   
            else : 
                break 
        
        # 從右到左 , 找違反遞減 
        while r >= 1 : 
            if self.val_list[r]  >= self.val_list[r-1]:
                r -= 1 
            else :
                break 
        # print(self.val_list)
        # print(l,r)
        self.node_list[l].val , self.node_list[r].val = self.node_list[r].val , self.node_list[l].val 
            
            
            
        
        
        