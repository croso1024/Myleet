""" 
    題意: 
        給定一個tree以及目標value , 要計算在這顆tree上一共有幾條path的節點值sum等於目標value 
        注意path並不一定要從root開始 , 並且節點的值也並非全都是positive
    
    思路:
        第一種想法 , 是定義一個recursion function , 其回傳從這個節點開始可以展開的所有可能值
        這個可能值包含了: [ 該節點值本身 , 該節點值+left child可型成的所有值 , 該節點值+right child可形成的所有值] 
        同時在每一個recursion的時候去檢查上面這些值有多少個等同於target sum並計算入答案值中 
        
        這種作法粗略的算 , 在每個節點都需要處理 O(其下path數量)的操作 ,絕對不是O(N)級別
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

""" 
    解法一. 
        就是用recursion function去回傳 "以每個節點為起點展開的path sum值" 之後去檢查這些sum值有多少條等於targetSum , 
        在時間複雜度上不佳,因為每一個節點都需要去執行與其path數相同的操作, 而空間上則最大需要 O(path數量) ,
        實際的結果來說速度不佳 , 空間倒是很不錯
"""
class Solution:
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        solution = 0 
        
        # recursion function要回傳以node能組成的所有可能值(即以node展開的所有可能path sum)
        def recursion(node): 
            nonlocal solution 
            if node is None : return None
            
            pathSum = [] 
            
            if node.left : 
                pathSum.extend( recursion(node.left)  )
            if node.right : 
                pathSum.extend(  recursion(node.right) )
            
            pathSum.append(0)
            
            # 去檢查說有多少個符合targetSum 
            for i in range(len(pathSum)) : 
                pathSum[i] += node.val 
                if pathSum[i] == targetSum : 
                    solution += 1 
                        
            return pathSum

        recursion(root)
        
        return solution

""" 
    解法二. 
        用traverse的思路 , 在展開的時候做以下的事情 :
            繼續累積 , 即包含當前節點繼續往left/right child 累積 or 重新開始展開
            但這麼做會遇到一個問題 , 就是有可能會重複展開
            
            我們使用一個visited set去紀錄 "曾經單獨從這邊展開" 這件事情
            就可以避免重複的展開導致重複計算
        
        這個解法的實際時間複雜度好像也普通 , 空間也是還不錯
"""


class Solution:
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        solution = 0 
        visited = set()
        visited.add(root)
        if root is None : return solution
        # recursion函數用來從給定節點進行展開 , 這個解法使用traverse思路
        
        def recursion(node, acc ): 
            nonlocal solution 
            
            if node.val + acc == targetSum  :
                solution += 1 
                
                
            if node.left : 
                
                recursion(node.left , acc + node.val)
                
                if not node.left in visited : 
                    visited.add(node.left)
                    recursion(node.left , 0 )
                    
            
            if node.right : 
                recursion (node.right , acc+node.val)

                if not node.right in visited : 
                    visited.add(node.right)
                    recursion(node.right , 0 )
            
            
        recursion(root , 0 )
        return solution 
    
""" 
    解法三. 
        prefix sum hashtable , 使用hashtable去保存目前遍瀝到此節點時 , 先前可以行成的path
        即在往下探索的過程去更新prefix sum( 代表這次展開從root到每一個節點的prefix ) 一旦在traverse過程中出現currentSum - prefixSum == targetSum的情況
        就代表這目前展開的某一段滿足了path. 
        
        參考 : https://www.youtube.com/watch?v=Cb5Me5oBfwo&t=360s

        這個解的時間複雜度就是O(N) , 空間則和總共有幾種sum成正比 ,
        
        一句話概括這個解法 , 就是使用hashtable去保存展開至此的path prefix , 同時應用hashtable的特性做到"快速檢查某一段path是否符合" 
        而因為在每個節點 , 都只能檢查沿著到達自身的path , 因此我們需要在展開的過程中去保持對hash-table的更新
        
"""

from collections import defaultdict
class Solution:
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        solution = 0 
        
        hashtable = defaultdict(int) 
        # prefix Sum = 0的路徑一開始有一條
        hashtable[0] = 1 
        
        def recursion(node , prefixSum) : 
            nonlocal solution
            if node is None : return node 
            
            currentSum = node.val + prefixSum  
            
            # currentSum - prefixSum == targetSum的情況就代表滿足解的path , 
            solution += hashtable[currentSum - targetSum]  
            
            # 準備往下展開 , 在展開的過程中需要maintain hashtable 
            hashtable[currentSum] += 1 
            recursion(node.left , currentSum) 
            recursion(node.right , currentSum) 
            hashtable[currentSum] -= 1 
            return 
        
        recursion(root , 0) 
        return solution 