"""
    思路 : 
        這一題在概念上與使用inorder+preorder類似 , 透過post order去找到root,並在inorder中找尋對應該root的左右子樹 
        核心的差別在於如何定義切分inorder/postorder的索引 。 

        以原始題目為例 : inorder [9,3,15,20,7] , postorder:[9,15,7,20,3] 
        我們使用post order的最後一個element 3來表示root , 在inorder左邊範圍中 , 9 代表left child , 15,20,7則是right child 

        這邊的重點就是如何去拆分post order中左右子樹的部份。 ,
        注意 
        inorder : 左 -> 中 -> 右 
        postorde : 左 -> 右 -> 中 
        換句話說 inorder和postorder的前半部份是一樣的 , 我這邊打算就使用 inorder中 "root的左半部份的最後一個元素" , 
        在上面的例子中就是 [9] 的最後一個元素index , 即0 作為拆分的index


"""
from typing import List , Optional 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        if len(inorder) == 0 : return None 
        elif len(inorder) == 1 : return TreeNode(val = inorder[0]) 
        else : 
            # root的value
            # 使用root的值 , 在inorder中定義左右子樹的範圍 
            index = inorder.index(postorder[-1])     
            
            return TreeNode(
                val = postorder[-1] ,
                left = self.buildTree( inorder[:index] , postorder[:index]    ) ,
                right = self.buildTree( inorder[index+1:] , postorder[index : -1 ] ) )  
        
        