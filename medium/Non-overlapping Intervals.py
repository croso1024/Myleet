""" 
    題意:
        給定一個包含多個區間的array , 其中的元素array[i] = [start_i , end_i] , 
        題目要問我們最少需要移除幾個element , 才可以讓剩下的區間全部都沒有重疊 ,
        note : 一段區間的end等於另一段區間的start不算重疊.
    
    思路:
        我的想法是,重疊的元素會有兩種case, 以兩個interval為例A,B 
        第一種情況 : A,B的start相同 , end不同 , 為了盡可能減少重疊 , 我們移除end比較後面的那個
        第二種情況 : A,B的start不同(假設B較後) , 則B的start一定小於A的end , 同樣為了減少重疊可能 , 移除兩個之中end延伸到最後面的
        以這種方式來做interval removal , 就是盡可能以最少次數remove達到non-overlapping
        
        當然以上操作的前提需要使用sort
"""


from typing import List 
""" 
    解法一. follow上述思路 , 
        速度就是O(NlogN) , 空間則是O(C) 
        實際的結果速度不錯,空間很優
        
"""
class Solution:

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        # 將其排序,會以第一個元素為主 , 接著才比較第二個元素
        intervals.sort() 
        
        # 紀錄需要移除的次數
        removal = 0 
        
        cur_s , cur_e = intervals[0]
        
        # 再看到下一個interval的時候有幾種情況 
        # -1. 沒有重疊,那麼不用刪除 ,
        # -2. 當前interval的start等於其start , 比較誰的end長來看移除誰(因為我們的排序 , 一定是後面那個大於等於 ,因此可以直接移除)
        # -3. 當前interval的end > 其start , 比較誰end長來看移除誰 
        for (next_s , next_e) in intervals[1:] :  
            
            # Case.2
            if cur_s == next_s : 
                removal += 1 
            
            # Case.1
            elif cur_e <= next_s : 
                cur_s , cur_e = next_s , next_e 
            
            # Case.3
            elif cur_e > next_s :  
                removal += 1 
                # 如果當前的end更大 , 保留下一個interval 
                if cur_e > next_e : 
                    cur_s , cur_e = next_s , next_e 
        
        return removal
                
            
            
                

                
                
            
            
        
        