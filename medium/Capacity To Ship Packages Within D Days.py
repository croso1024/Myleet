""" 
    題意:   
        給定一組貨物array , array[i]代表著該貨物的重量 , 以及一個整數day代表可用天數
        假設每天都會使用運輸車去運貨一趟 , 並且上貨的順序必須按照array的順序
        一趟的貨物重量不可超過運輸車的capacity , 
        要求capacity至少要多少才可以在給定天數內載完

    思路: 
        因為題目的N範圍在 10^4 , 而我們可以大略知道只要 capacity = sum(array) , 就一定可以一天載運完成
        因此我們將初始bound設定為 1 , sum(array) , 利用binary search
        
        每次binary search我們需要計算當前重量是否可以載運完成 , 而這件事情可以take O(N)達成 , 整個binary search則是take
        O(log(sum(array)))  

        基本上就是做找left bound的binary search 

"""

""" 
    解法一. 就是take O(N)去做檢查當前capacity可否完成任務 , 接著搭配binary search
        時間和空間都還不錯
"""
from typing import List 

class Solution:

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        
        # 用來計算給定重量是否可以完成運輸 , take O(N)
        def canComplete(capacity):  

            cur_capacity = 0 
            day = 0 

            for i in weights : 
                
                # 如果有任何貨物是直接大於運輸車重量 , 就不可能運輸
                if i > capacity : return False 
                    
                
                if cur_capacity + i > capacity : 
                    day += 1 
                    cur_capacity = i 

                else :  
                    cur_capacity += i 
            
            day += 1 if cur_capacity > 0 else 0 
            
            return True if day <= days else False 
        
        # binary search , calculate sum(weight) take O(N) 
        left , right = 1 , sum(weights)  
        
        while left <= right : 
            
            mid = left + ( right - left ) // 2 
            
            # 檢查當前capacity是否可以完成運輸 
            # 如果可以的話 , 就壓縮right 
            if canComplete(mid) :   
                
                right = mid - 1
                
            else : 
                
                left = mid + 1 
                
        
        return left 
                