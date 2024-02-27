from typing import List 
from numpy import array
class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        
        # 最多只能執行k次的buy-sell 
        # if k == 1 dp solution  : dp[i] = ( max profit if keep stock in day i , max profit if non stock in day i ) 
        # generalize to k > 1 :
        # dp[i][k] = (  max profit if keep stock and make k time transation   , max profit if non stock and k time transation)
        """ 
        base case 
        1.dp[:][0] = (  0 ,  0 )   
        2.dp[0][1] = ( -prices[0] , 0  ) # -> 這邊有錯誤 , 應該是dp[0][:] = (-prices[0],0) 
        
        state transition : 
            dp[i][k] =  (     
                max ( dp[i-1][k-1][1] - prices[i]  , dp[i-1][k][0]
                max ( dp[i-1][k][0] + prices[i]    , dp[i-1][k][1]   )
        )

        第i天 , 並在執行了k次交易後(以購買算做一次) . 
        則拿著股票的最大收益值 會等於 前一天就已經買了(同樣在k次)  或著今天買 , 則收益為前一天在少一次交易的情況下沒有股票的最大值-prices[i]
        而沒拿股票的最大收益 , 則是 前一天有拿著股票的最大收益加上今天賣出 , 或著 前一天就沒拿著
        
        """
        
        # maximum transation times 
        K = 2 
        dp = [ [ (0,0) for i in range(K+1) ] for j in range(len(prices))  ] 

        # base case : 
        # dp[0][1] = (-prices[0] , 0)
        for k in range(K+1):
            dp[0][k] = (-prices[0] , 0)
        
        # 推進DP狀態 
        
        for i in range( 1 , len(prices) ): 
            
            for k in range( 1,K+1 ): 
                dp[i][k] = (
                    # 在前一天少一次交易狀況下的無股最大 - 買股價格 , 前一天就買完了 
                    max( dp[i-1][k-1][1] - prices[i]  ,  dp[i-1][k][0] ), 
                    
                    # 賣掉今天的股票 , 收益為昨天買入的加上今天賣出 , 或著前一天就買入的繼續拿著
                    max( dp[i-1][k][0] + prices[i] , dp[i-1][k][1]      )
                    
                )
        # 最終答案位在 dp[len(prices)-1][k] 
        return dp[len(prices)-1][k][1]
    
# test = [3,3,5,0,0,3,1,4]
test = [1,2,3,4,5]
S = Solution()
print(S.maxProfit(test))