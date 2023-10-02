# Definition for a binary tree node.

from typing import List , Optional 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
""" 
    思路 : 
        遞迴的進行樹的建構 , 即根節點+左右兩顆子樹  ,使用post-order 
        先建構好左右兩棵子樹後(post-order)和root接起來 , 而root是傳入子陣列的中位數 
        
        
    
"""        

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        # 先走一個O(n) ，把數字轉換橙節點集 
        node_set = [ TreeNode(val=i) for i in nums ]
        
        # 給定一個節點集，建立一個以中間節點為root的tree返回
        def buildTree(nodes : List[int] ) :  
            
            # 如果已經沒有節點就返回None 
            if not nodes : return None 
            elif len(nodes)==1: return nodes[0]
            # 如果不到兩個節點
            elif len(nodes) == 2 : 
                if nodes[0].val > nodes[1].val : 
                    nodes[0].left = nodes[1]
                    return nodes[0]
                else : 
                    nodes[1].left = nodes[0]
                    return nodes[1]
            
            mid = (len(nodes)-1) // 2  
            root = nodes[mid]
            
            left_child = buildTree( nodes[:mid] ) 
            right_child = buildTree( nodes[ mid+1 : ])
            
            # post-order , 將兩個節點和root接合
            root.left = left_child 
            root.right = right_child 
            
            return root
            
        
        return buildTree(node_set) 
    
nums = [-10,-3,0,5,9] 
C = Solution()
print(C.sortedArrayToBST(nums))