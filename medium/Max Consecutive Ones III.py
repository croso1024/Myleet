""" 
    思路 : 
    
        此題感覺起來像是DP題 , 給定一個只有0,1的array , 
        假設我們可以將其中k個0轉成1 , 最長可以得到幾個連續的1 . 

        令DP table dp[i][k]: 在以nums[i]結尾的subarray中, 可以翻k次的情況下可以得到的最大長度 
        
        - nums[i] = 1 : dp[i][k] = dp[i-1][k]  
        - nums[i] = 0 and k > 0  : dp[i][k] = dp[i-1][k-1]
        - nums[i] = 0 and k = 0  : dp[i][k] = dp[0] 
        
        令 dp table : dp[i][k] : 在nums[0:i+1]的範圍中 , 可以翻k次的情況下可以得到的最大長度
        
        - nums[i] = 1 : dp[i][k] = dp[i-1][k] + 1  
        
        
        想了一段時間DP解沒有概念 , 後來去看這一題的主題發現不是DP , 可以用sliding window去解
        一想到sliding window這一題算是別的更加明朗了
    
"""

from typing import List 


""" 
    解法一. sliding window . 

        控制視窗內有幾個是翻轉的值 ,當剩餘翻轉數量允許的情況下可以擴展window , 否則縮小window , 

        重點在於釐清縮小window的時間在於剩餘翻轉數量小於0的情況 , 我們將擴展時只要遇到0就會減少flip , 
        如此一來就算nums[0] =0 ,k = 0 , 也會馬上跟進縮小window , 我們在縮小完window後更新最佳解
        
        這個解法時間普通 , 空間還行
"""

class Solution:

    def longestOnes(self, nums: List[int], k: int) -> int:
        
        left = 0 
        right = 0 
        # 紀錄最佳解 
        solution = 0 
        # 紀錄剩下可以翻轉的次數
        flip =  k 
        
        
        # 實現開放區間的sliding window [left , right)
        while right < len(nums):  
            
            if nums[right] == 0 : flip -= 1 
            right += 1 
            
            
            while left < right and flip < 0 : 
                
                if nums[left] == 0 :  flip += 1 
                left += 1 
            
            solution = max(solution , right-left) 
        
        return solution                     
                
                
nums =  [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3    
S = Solution() 
print(S.longestOnes(nums=nums , k=k) )
                
                
            
                
                            