# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


# 目標是以O(1)實現next() , hasNext() , 並且只使用O(h)的space , h為樹的高度,
# 我認為可以使用iterative的方式實做in-order traverse來完成,利用stack去存先前的node就能達到O(h)的space
# 具體來說要把步驟做個分解 , 在初始化時移動pointer到最小的元素上 ,而這個pointer也用來做hasNext , Next所要返回的對象
# 當next()返回了原本pointer的內容 , 即開始iterative的更新inorder traverse的pointer
# 若pointer有right child , 先移動上right child之後不斷往left child走並且更新stack , 停下的位置即新pointer位置
# 但若沒有right child了 , 從stack拿一個節點出來作為新的pointer即可 
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        
        self.pointer = root 
        self.stack = [] 

        while self.pointer.left : 
            self.stack.append(self.pointer)
            self.pointer = self.pointer.left
        
        # 到此 , pointer停留在tree中最小的部份

    def next(self) -> int:
        
        returnVal = self.pointer.val 
        
        if self.pointer.right :
            
            self.pointer = self.pointer.right 
            
            while self.pointer.left : 
                self.stack.append(self.pointer)
                self.pointer = self.pointer.left 
        
        else :
            
            if self.stack :
                self.pointer = self.stack.pop() 
            else : 
                self.pointer = None 
        
        return returnVal         
        

    def hasNext(self) -> bool:
        
        return bool(self.pointer)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()