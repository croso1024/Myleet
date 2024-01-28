from typing  import List 
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
                
        # maximum transation times 
        K = k
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
        return dp[len(prices)-1][K][1]
    