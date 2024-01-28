"""
    思路 :   
        買賣股票系列題 , 使用特殊的一維DP 
        
        令dp[i] = ( 到達第i天,如果持有股票的最大收益 , 到達第i天 , 沒有股票的最大收益 )
        base-case :  -prices[0] , 0 
        
        而我們要找到的答案在  dp[i][1] , 到達最後一天後沒有股票的最大收益(因為把手上的賣掉一定>留著) , 股票價格都是正的
        
        定義狀態轉移 : 
        
            // 持有股票只有兩種 : 當天買入 , 前一天就拿著  
            dp[i][0] = max ( dp[i-1][1] - (prices[i]+2) , dp[i-1][0] )
            // 沒有股票也是兩種 : 當天賣掉的 , 前一天就沒有 
            dp[i][1] = max ( dp[i-1][0] + prices[i] , dp[i-1][1] )

        注意這一題有交易手續費 , 一筆交易只收一次 , 我將他放在購買時 
"""


""" 
    解法一 , 標準DP 
"""

from typing import List 

class Solution:
    
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        dp = [[None,None] for i in prices] 
        
        # base case : 注意有手續費
        dp[0][0] = -(prices[0]+fee)
        dp[0][1] = 0 
        
        
        # 推進DP狀態
        for i  in range(1 , len(prices)): 
            
            # 持有股票的最大收益  , 注意買股票要多加收手續費
            dp[i][0] = max(dp[i-1][0] , dp[i-1][1] - (prices[i]+fee) ) 
            
            # 沒有股票的最大收益 
            dp[i][1] = max (dp[i-1][1] , dp[i-1][0] + prices[i]) 
    
    
        return dp[ len(prices) -1   ][1] 
            

""" 
    解法二 . DP狀態壓縮 , 節省空間
"""

class Solution:
    
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        
        # base case : 注意有手續費
        have_stock = -(prices[0]+fee)
        no_stock = 0 
        
        # 推進DP狀態
        for i  in range(1 , len(prices)): 
            
            next_have_stock = max( have_stock , no_stock -(prices[i]+fee) )
            next_no_stock = max(no_stock ,  have_stock + prices[i] )
            
            have_stock = next_have_stock 
            no_stock = next_no_stock 
            
        return no_stock             