class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List , Optional

class Solution:

    
    # 透過pre-order來找尋當前tree的root , 由in-order的資訊來判斷該root的左右子樹範圍
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        
        def build( preorder:list , inorder:list): 
            
            if len(preorder) == 0 : return None 
            # elif len(preorder) == 1 : return TreeNode(val=preorder[0])
            
            root = preorder[0]  
            index = inorder.index(root) 
            
            left_subtree = build(  preorder[1:index+1] , inorder[:index]      )
            right_subtree = build(  preorder[index+1 :]  , inorder[index+1 : ]   )
            
            node = TreeNode(val = root )
            
            node.left = left_subtree 
            node.right = right_subtree 
            
            return node 
        
        return build(preorder , inorder)
    

class Solution:

    
    # 透過pre-order來找尋當前tree的root , 由in-order的資訊來判斷該root的左右子樹範圍
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if len(preorder) == 0 : return None 
        
        root = preorder[0] 
        index = inorder.index(root) 
        
        node = TreeNode(val=root) 
        
        left_child = self.buildTree(
            preorder= preorder[1:index+1] , inorder=inorder[:index]
        )
        
        right_child = self.buildTree(
            preorder = preorder[ index+1 : ] , inorder=inorder[ index+1 :  ]
        )
        
        node.left = left_child 
        node.right = right_child 
        
        return node 