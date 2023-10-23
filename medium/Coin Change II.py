
""" 
    思路 : 
        這一題看到題目的硬幣array大小大概就知道不能使用backtrack 
        不過可以透過DP來處理 
        
        這一題也是卡住想了一段時間 , 嘗試去構思一維DP的作法 , 用dp[i]表示換i塊的方法數
        但似乎不可行 
        
        改以東哥的觀點 -> 將此問題視為背包問題 , 
        amount是我們的最大容量 , coins則代表可以無限取用的物品 
        
        定義dp[i][j] : 在考慮前i個物品的情況下 ,amount=j 時的兌換方法數 
        
        base case: 
            dp[0][:] => 0 無法兌換 
            dp[:][0] => 1 只有1種?  
            
        狀態轉移方程式 :

            1.有了新的面額可用 , 則加入這個面額後可用的方法數為 
                -> 沒有這個面額前湊到 j - coins[i] 的方法數 
                -> 沒有這個面額也要湊到j的方法數

                dp[i][j] = dp[i-1][  j - coins[i]  ] + dp[i-1][j]

            # 我一開始的思路有錯誤在此 , 在確定要使用這個新面額時的狀態轉移應該是 :

                並不是"沒有這個面額時湊到 j - coins[i] 的方法數" , 而應該是有這個面額時湊 j - coins[i] 的方法數

                dp[i][j] = dp[i][ j - coins[i] ] + dp[i-1][j] 


                
            2. 一旦新的面額大於目前背包size , 那這個面額也不能選 
                dp[i][j] = dp[i-1][j]  , if j - coins[i] < 0 
        
        

"""

from typing import List 

class Solution:
    
    def change(self, amount: int, coins: List[int]) -> int:
        
        # create dp-table : 面額種類 * amount(重量)
        dp = [[0 for i in range(amount+1)] for j in range(len(coins)+1)]
        
        # 無論面額種類是啥 , 如果amount=0 , 那湊到的方法只有一種(不選)
        for i in range(len(coins)+1): dp[i][0] = 1 
        
        
        # 外層推進狀態一 : 面額種類 
        for i in range( 1 , len(coins)+1) : 
            
            # 內層推進狀態二 : 湊集到硬幣數量 
            for j in range( 1 ,  amount+1   ): 
                
                # 如果當下的面額是完全大過重量 , 那dp[i][j] = dp[i-1][j]
                # 記得對coins加入index offset 

                if j - coins[i-1] < 0 : 
                    dp[i][j] = dp[i-1][j] 
                    continue 
                
                #-> 採用了這個面額,並湊到 j - coins[i] 的方法數 ( 這些方法都是再+ coins[i-1]就達到j )
                #-> 沒有這個面額也要湊到j的方法數
                dp[i][j] = dp[i][ j - coins[i-1] ] + dp[i-1][j]   
                
        # 依據dp-table的定義 , 答案是可以湊到amount的方法數 
        # 即 dp[len(coins)][amount]
        return dp[len(coins)][amount]
        
        
                 
S = Solution() 
print(S.change(5 , [1,2,5]))
                

            
        