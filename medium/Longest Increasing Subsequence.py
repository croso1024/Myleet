""" 

    思路 :  
        這一題是一個DP , 具備最佳子結構  ,重點是我們要如何定義狀態和狀態轉移方程式 , base case 
        
        這邊我自己想了幾種 
        1. dp[i]表示從i開始的array的最大遞增數 , 但這樣dp[0]等於原題目不太合理 
        2. dp[i]表示到i為止的array最大遞增數 ,
        3. dp[i][j] 表示i開頭到j結束的最大遞增數 
        
        主要是在2/3之間思考 , 但如果使用3 , 應該也會是一個只需要推上半的DP三角的table 
        
        以2.來思考可能的狀態轉移方程式 
        - base case : dp[0] 等於 1 即自己 
        - state transition equation : 
            dp[i] = 0 ~ i-1 中 , 參與累積的最大值小於nums[i] , 並且dp最大的
        

"""

"""
    解法一. 
        在上述思路解到一半的時候 , 我突然想到將dp[i]視為 "選擇了nums[i]作為結尾(最大值)的subsequence最大長度" 
        這樣比較直觀的就可以將上述所說的 參與累積的最大值直接與nums[i]連結 . 
        
        就可以更簡單的去計算說 , 如果當前nums[i]的值大於 nums[j] , 就一定可以把1+dp[j]視為dp[i]的候選人
        因此雙迴圈去找出 所有 nums[i]>nums[j]的部份中 , 1+dp[j]最大的就可以了
        
        速度與空間都還不錯
"""

from typing import List 
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # 和nums長度相同就可以了 , dp[i]代表以i作為最後一個值(最大值)的sub sequence的最大累積數
        dp = [None] * len(nums)  
        dp[0] = 1
        
        
        for i in range(1 , len(nums)) : 
            
            best = 1 
            
            for j in range(i) : 
                if nums[i] > nums[j] : 
                    best = max(best , dp[j]+1) 
            
            dp[i] = best 
            
        
        
        return max(dp)            
            