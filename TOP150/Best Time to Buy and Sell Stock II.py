
class Solution:

    def maxProfit(self, prices: List[int]) -> int:

        # dp solution , dp[i] = ( 在第i天持有股票的最大收益 , 第i天沒有的最大收益   )    
        # base case dp[0] = ( -prices[0] , 0 ) 
        dp = [ None for i in range(len(prices)) ]       
        dp[0] = [  -prices[0] , 0  ]
        
        for i in range(1 , len(prices)): 

            max_profit_have = max( dp[i-1][0]  , dp[i-1][1] - prices[i]   ) 
            max_profit_not = max(  dp[i-1][0] + prices[i] ,  dp[i-1][1]   ) 

            dp[i] = [ max_profit_have , max_profit_not ]

        return dp[len(prices)-1 ][1]

class Solution:

    def maxProfit(self, prices: List[int]) -> int:

        # dp solution , dp[i] = ( 在第i天持有股票的最大收益 , 第i天沒有的最大收益   )    
        # base case dp[0] = ( -prices[0] , 0 ) 
        dp = [ None for i in range(len(prices)) ]       
        dp[0] = (  -prices[0] , 0  )
        
        for i in range(1 , len(prices)): 

            dp[i] = (
                max( dp[i-1][0]  , dp[i-1][1] - prices[i]   ) , 
                 max(  dp[i-1][0] + prices[i] ,  dp[i-1][1]   ) 
             )

        return dp[len(prices)-1 ][1]

class Solution:

    def maxProfit(self, prices: List[int]) -> int:

        # dp solution , dp[i] = ( 在第i天持有股票的最大收益 , 第i天沒有的最大收益   )    
        # base case dp[0] = ( -prices[0] , 0 ) 
        last_hold =  -prices[0]
        last_empty = 0 

        for i in range(1 , len(prices)): 

            cur_hold = max(last_hold , last_empty-prices[i])
            cur_empty = max(last_empty , last_hold + prices[i])

            last_hold = cur_hold
            last_empty = cur_empty

        return last_empty
