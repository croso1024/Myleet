
""" 
    思路 :  
        這題比較明顯使用回溯算法去硬爆解 , 從candidates陣列中組合出可以=target的值 , 
        candidates陣列會有重複的元素 , 而且每個元素看起來只能取一次 
        這種題目比較需要想一下的部份 -> 不能有重複combination也有在內 
        寫backtrack算法 , 逐漸縮小action list應該就可以完成

"""


"""

    解法一. 
        就是普通backtrack , 第一次寫的時候我把track_sum > target or not actions 放在前面
        會導致有可能剛好走到最後一個action才==target sum的情況沒有被加入solution , 調整一下順序即可 
        
        另一方面則是避免重複組合 , 由於這一題candidates會出現duplicate element , 
        所以不能單單只是隨outer loop前進action-list  , 而是會需要搭配一個prev 變數 ,如果要展開的部份有和先前的重複就跳過
        另外也是因為這個緣故 ,我先做了一個Sorted .

        不做sort 可能就需要把一個memo一起丟進去給backtrack function
"""

from typing import List 
class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    
    
        solution = [] 
        candidates.sort()
        
        
        
        # backtrack : 可用動作清單 , 目前的軌跡 , 軌跡的sum
        def backtrack( actions , track : list, track_sum) :
            print(track , track_sum)
            
            
            if track_sum == target : 
                solution.append(list(track)) 
                
            # 當軌跡和超越target , 或著沒有可用動作清單了就清除
            elif track_sum > target or not actions : return 

            
            else : 
                
                prev = None 
                
                for idx ,  action in enumerate(actions)  : 
                    
                    if not prev is None and action == prev : continue
                    
                    
                    track.append(action) 
                    backtrack(  actions[idx+1:]  , track , track_sum + action  )
                    track.pop() 
                    
                    prev = action 
                    
        backtrack(candidates , [] , 0 )
        return solution
    

