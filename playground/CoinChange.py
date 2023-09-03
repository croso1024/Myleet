from typing import List

class Solution:
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     # Bottom up approach
    #     dp = [amount+1] * (amount+1)
    #     dp[0] = 0 
        
    #     for i in range(amount+1) : 
            
    #         for coin in coins: 
    #             if i-coin <0 : continue 
    #             dp[i] = min(dp[i] , 1 + dp[i-coin])

    #     return dp[amount] if dp[amount] != amount+1 else -1 
        
    
    
    def coinChange(self , coins:List , amount ): 
        
        coins.sort()
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0 
        
 
        for i in range(1 , amount+1) :  
            
            for coin in coins : 
                
                if (i-coin) < 0 : break 
                
                dp[i] = min( dp[i],1+ dp[i-coin]   )

        return dp[amount] if dp[amount] < amount+1 else -1
    
S = Solution()

print(S.coinChange([474,83,404,3] ,264))
        
        
        
        