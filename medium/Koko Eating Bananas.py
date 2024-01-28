""" 
    思路 :  
    
        此題是要求極值 , 給定一組array , array[i]代表第i堆香蕉的數量 
        我們要計算一個最低的吃香蕉速度k (per hr) , 可以在守衛回來的h小時前吃完所有香蕉 . 
        注意如果速度大於該香蕉堆 , 則吃完後不會馬上前往下一個香蕉推 
        -> 無論速度多快, 一個香蕉堆至少要一小時

        原先認為這一題是求極值問題套用DP , 但仔細思考沒有推敲出什麼狀態轉移的端倪,
        看起來這個問題沒有明顯的最佳子結構
        
        看一下題目分類才發覺這一題是Binary search
        先去寫出暴力解 , 再來看有沒有優化的方向
        
        -- 寫完暴力解 , 會發現我們實際上在一個速度範圍內去找值 , 接下來思路就很清晰了
            透過Binary search去定位值 , 因為題目要求最小速度 , 這邊就是要用找左側邊界的Binary search

"""


""" 
    解法一.
        暴力解 , 列舉所有可能的速度 , 最多就是到 max(piles) 
        
"""
from typing import List 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        for speed in range(1 , max(piles)): 
            acc_time = 0 
            for pile in piles : 
                
                if pile % speed == 0 : 
                    acc_time += (pile // speed) 
                else : 
                    acc_time += (pile //speed) + 1 
                
                
            # 由於我們是從speed = 1 開始走 , 一旦遇到可以滿足的就是答案了
            if acc_time <= h : 
                return speed 
        
        return max(piles)
    
""" 
    解法二. 透過鎖定左側邊界的Binary search去找最小speed 
    
    速度與空間都相當優
"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # 用來測試在給定速度下是否能吃完全部
        def valid( speed ): 
            acc_time = 0 
            for pile in piles : 
                acc_time = acc_time + (pile//speed) if pile % speed == 0 else acc_time + (pile//speed) +1
            return acc_time <= h 
            
            
        
        
        
        # 定義速度區間 , 我們使用封閉區間的Binary Search [1,max(piles)]
        left , right = 1 ,  max(piles) 
        
        while left <= right : 
            # speed 中央 
            mid = ( left + right ) // 2 
            
            effect = valid(mid) 
            
            # 如果這個速度是有效的 , 繼續往左邊壓縮視窗 
            # 如果無效,代表速度要提高 , 往右邊去壓縮
            if effect : 
                right = mid - 1     
            else :             
                left = mid + 1 
        
        # 走完這個Binart search , 中止條件在於 left > right  
        # 此時left所指向的位置就是滿足的解了
        return left     
    
S = Solution()
S.minEatingSpeed([30,11,23,4,20] , h=6)
        