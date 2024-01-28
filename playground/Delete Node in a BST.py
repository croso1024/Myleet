# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


""" 
    刪除節點的幾個case :
    1. 如果刪除的目標沒有child -> 直接刪除
    2. 只有一個child , 把刪除的那個節點的parent接在他child上 
    3. 有兩個child , 則得從right-subTree中挑最小的出來 , 接在被刪除節點的parent之下 , 替代其位置
"""



from typing import Optional 

class Solution:

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        # 先找到要刪除的目標
        probe = root 
        prev = None 
        while probe : 
            
            if probe.val > key :                    
                prev = probe 
                probe = probe.left 

            elif probe.val < key : 
                prev = probe 
                probe = probe.right  

            # 發現要砍的節點了 
            else:
                # 兩個child都在的情況 , 比較複雜 
                # 從right-sub tree去找最小的節點(或反過來) , 作為被砍掉節點那個位置的替代
                if probe.left and probe.right : 
                    
                    # 找probe.right的子樹中最小的
                    temp = probe.right 
                    prev2 = None 
                    while temp.left :  
                        prev2 = temp 
                        temp = temp.left 
                    
                    if prev2 is None  : 
                        temp.left = probe.left 
                    elif temp.right and prev2 : 
                        prev2.left = temp.right  
                        temp.left = probe.left 
                        temp.right = probe.right 
                    elif prev2 : 
                        prev2.left = None 
                        temp.left = probe.left 
                        temp.right = probe.right                         
                            
                    if prev is None :  
                        return temp 
                    
                    if prev.val > probe.val : 
                        prev.left = temp 
                    else : 
                        prev.right = temp

                    return root 
                # 只有一個child或著沒有child ,那就直接接上就可 
                else : 
                    # 例外情況是如果發現要砍的就是root , 且root只有或沒有child , 
                    if prev is None : 
                        return probe.left if probe.left else probe.right 
                    
                    # 如果prev的值比較大 , 代表我們砍的是left child  , 反之right_child 
                    if prev.val > probe.val : 
                        prev.left = probe.left if probe.left else probe.right
                    else : 
                        prev.right = probe.left if probe.left else probe.right
                    
                    return root 
        
        
        return root 