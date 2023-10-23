"""
    思路 : 
        給定一個序列nums,返回其中有著總和最大的子序列的序列值  
        這裡的子序列(sub-array) 定義是要連續的element所構成的序列 
        
        雖然知道這一題是DP , 但乍一看還有一瞬間會以為可以用sliding window ,
        但sliding window在這一題會因為無從判斷window內是合法的解, 來調整window範圍 , 因為此題是一個求極值問題 
        
        但從DP的思路來說比較直觀可以想到 , 令狀態 i 定義為以 index=i 的element作為結尾的子序列的最大和  
        如此一來 ,  dp[i+1] = max( nums[i+1] , nums[i+1]+dp[i] ) 
        亦即新加入一個元素後 , 以該元素為結尾的最大子序列和要馬就是只有他 , 或著是截止前一個的最大子序列和+他 
        
        得到dp-table , 紀錄了截止每個元素的最大和後 , 就可以通過O(N)尋訪得到最佳解 

"""



""" 
    解法一 . 直接根據以上看出的DP 狀態轉移去寫 , 
        把best的更新放在for-loop內 , 比較省時間 , 
        但實際上 , 這是一個 1D DP問題  , 為了解dp[i] , 我們只會需要dp[i-1]也就是前一個
        因此根本不必要keep O(N) 的space complexity 
"""
from typing import List 
class Solution:
    
    def maxSubArray(self, nums: List[int]) -> int:
        
        # dp-table, 這邊不用再多加一了 , 根據定義 dp[i] = 以index = i 為結尾的子序列最大和 
        dp = [None] * len(nums) 
        dp[0] = nums[0] 
        
        best = dp[0]
        
        for i in range(1 , len(nums)): 
            
            dp[i] = max(nums[i] , nums[i] + dp[i-1] )
            best = dp[i] if dp[i] > best else best
            
        return best 
    

""" 
    解法二. 對space compleixty做個優化 , 只保留前一個元素 
    
    --> 這個解法在空間上最優 , 速度也和上一種差不多 
"""
class Solution:
    
    def maxSubArray(self, nums: List[int]) -> int:
        
        dp = [None] * len(nums) 
        prev = nums[0] 
        best = prev 
        
        for i in range(1 , len(nums)): 
            
            next = max(  nums[i] , nums[i] + prev ) 
            best = best if best > next else next 
            prev = next 
        
        return best 