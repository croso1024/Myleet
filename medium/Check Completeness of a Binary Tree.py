""" 
    題意:

        給定一個binary tree , 檢查其是否是complete的 , 
        complete的binary tree除了最底層的leaf以外都要填滿,並且最後一層必須是由左往右的填,不能有空缺
        
    思路:
    
        所謂的最後一層必須由左往右填,在使用BFS去traverse tree的時候就應該會一直發現child ,
        一旦從某個節點沒有發現child , 那之後的節點(因為BFS , 因此仍在同一level的其他節點就不允許發現child)
        可以接受都沒有發現child .
        
        上面這個解法還需要去擋住 , 可能在第一次消失之後的右邊沒有其他節點,但左邊的節點卻還有更多child的情況
        一次我的作法就是BFS ,並且把None也作為節點加入 , 一旦BFS的queue吐出一個None , 代表後面不應該再有節點被queue吐出來

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import Optional

""" 
    Method.1 BFS  , effective , efficient
"""

from collections import deque
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:

        queue = deque()
        queue.append(root) 
        empty = False 
        while queue : 
            
            size = len(queue) 
            
            for _ in range(size):
                
                node = queue.popleft() 
                
                if node is None : 
                    empty = True 
                    continue
                if node and empty : return False 
                
                queue.append(node.left)
                queue.append(node.right) 
        
        return True 
                    