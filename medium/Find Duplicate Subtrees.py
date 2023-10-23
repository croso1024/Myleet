
""" 
    思路 : 這一題要找到Tree中 所有具有相同結構和值的子樹 , 
    稍微思考一下最naive的作法可能是將每個子樹的 pre-order / in-order / post-order 任意挑兩個出來做Key 
    即Hashmap的Key , 並保存他們的節點參考 
    這樣在尋訪的過程中不斷將Key加入hash map , 同時去對照是否有key已經存在就好
    這一題的思路上要用到遍尋的作法 
    
    
    --> 這個作法可以處理常規狀況 , 但透過pre-order / post-order沒有辦法分辨例如 
          0左邊接0 , 或0右邊接0 這兩種結構 ,會導致誤以為他是一樣的  
          所以需要透過在 node is None 不是返回 [] , 而是 [None] , 這樣才能讓pre/post order能夠分辨以上情況
          
    
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List , Optional

""" 
    解法一. 在Post-order處去計算每一個節點的 pre-order / post-order作為Key , 來判斷是否有重複的結構
    時間空間都不太佳
"""
class Solution:
    
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        solution = set()
        hashmap = dict() 
        # 遞迴函數會返回該節點的pre-order post-order
        def traverse(node):     
            if node is None : return None , [None] , [None] 
            
            
            left_child , l_pre , l_post = traverse(node.left)
            right_child , r_pre,r_post = traverse(node.left) 
            # 拿到了左右child的pre-orde / post-order就可以組裝自己的pre-order / post-order
            
            pre_order = [node.val]+ l_pre + r_pre 
            post_order = l_post + r_post + [node.val] 
            
            key = (  tuple(pre_order) , tuple(post_order) )
            # 如果已經有重複的出現在tree中 , 就append這個節點(子root)
            if key in hashmap and key not in solution: 
                solution.add(key)
            else : 
                hashmap[key] = node   
            
            return node , pre_order , post_order
        
        traverse(root)
        
        solution = [ hashmap[key]  for key in solution]
        
        
        return solution


""" 
    解法二 . 調整了Key的產生方式 , 沒必要透過pre/post order , 我們可以去紀錄這顆樹的形狀來完成key的產生 
    
    --> 計算速度跟空間都大幅上升 , 我猜測也和從list改用str有關
"""

class Solution:
    
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        hashmap = dict() 
        used = set() 
        solution = [] 
        # 遞迴函數返回該節點作為root的子樹的結構字串
        def traverse(node):     
            # 如果節點是空的 , 回傳這個井字號 
            if node is None : return None 
            
            left_child_structure = traverse(node.left)
            
            right_child_structure = traverse(node.right) 
            
            l_struct = left_child_structure if left_child_structure else "L"
            r_struct = right_child_structure if right_child_structure else "R"
            
            
            key =   l_struct + str(node.val) + r_struct
            
            if not key in hashmap :  hashmap[key] = node 
            else :  
                if not key in used :
                    solution.append(node) 
                    used.add(key) 
                    
                    
            return key 
        
        traverse(root) 
        
        return solution
            
        
            
        
        