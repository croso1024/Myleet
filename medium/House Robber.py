""" 
    思路 : 
        這一題也算經典DP , 很直觀能想到大致上的DP table定義與狀態轉移函數 
        
        此題使用1D-table , 令dp[i]為 在nums 0 ~ i的範圍內,可以拿到的最大值
        因為不能連續的拿 , 因此狀態轉移函數寫成如下 :

        dp[i] = nums[i] + dp[i-2] ( 雖然dp[i-1]也不見得拿了 nums[i-1] , 但使用dp[i-2]準沒錯 )
                or  dp[i-1] 
        
        base case : 
            dp[0] = nums[0] 
            dp[1] = max(nums[0],nums[1])
        
"""

""" 
    解法一. 直覺DP
"""

from typing import List 
class Solution:

    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1 : return nums[0] 
        
        dp = [None for i in range(len(nums))]  
        dp[0] = nums[0]
        dp[1] = max(nums[0] , nums[1])


        for i in range(2,len(nums)): 
            
            dp[i] = max(  nums[i] + dp[i-2] , dp[i-1]  )
        
        return dp[len(nums)-1]


""" 
    解法二. 略微優化空間 
"""
class Solution:

    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1 : return nums[0] 
        
        prev_2 = nums[0]
        prev_1 = max(nums[0] , nums[1])


        for i in range(2,len(nums)): 
            
            temp = max(  nums[i] + prev_2 , prev_1  )

            prev_2 = prev_1 
            prev_1 = temp 
            
        return prev_1