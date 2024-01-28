"""
    背包問題的思路 : 
        在給定的coins情況下 , 湊出 1,2,3,4 ... amount元 共有幾種方式 
        
        定義DP table : dp[i][k] , 為使用coins[:i]的範圍湊出硬幣k個方法數  , 因此需要多一個沒有任何硬幣的情況
        
        dp[i][k] = dp[i][k-coins[i]] + dp[i-1][k]
        
        base case : dp[:][0] = 1  / dp[0][1:] = 0 
        
        答案就在 dp[len(coins)][k]
        

"""
import numpy as np 
from typing import List 
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = [ [ 0 for j in range(amount+1) ] for i in range(len(coins)+1) ]
        
        # base case : 
        for i in range(len(coins)+1) :     dp[i][0] = 1 
        # for i in range(1 , amount+1) :  dp[0][i] = 0 
        
        # DP-狀態推進 
        for i in range(1,len(coins)+1): 
            
            for k in range(1 , amount+1):            
                
                if k - coins[i-1]  >=0 : 
                    dp[i][k] = dp[i][ k - coins[i-1] ]  + dp[i-1][k]     
                else :
                    dp[i][k] = dp[i-1][k]
                    
        
        return dp[len(coins)][amount]
        
S = Solution()

print(S.change(amount=5 , coins=[1,2,5]))
        