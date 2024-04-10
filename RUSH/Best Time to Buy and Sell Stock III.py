from typing import List 


# dp solution : dp[i][k] : 在0:i範圍內做最多k次交易的最大收益值 : ( 持有的最大收益 , 非持有的最大收益 )

class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        
        k = 2 
        
        dp = [ [ [0,0] for i in range(k+1)  ] for i in range(len(prices)) ]
        
        for i in range(k+1) : dp[0][i] = [-prices[0] , 0] 
        
        for i in range(1 , len(prices)): 
            
            for j in range( 1, k+1): 
                
                # 在第i天 , 交易j次的持有最大收益等於前一天就買了股票 或著 今天才買
                dp[i][j][0] = max(
                    dp[i-1][j][0] , dp[i-1][j-1][1] - prices[i] 
                )
                # 在第i天 , 交易j次後尚未持有的最大收益等於把前一天就拿著的賣掉, 或著昨天就沒有拿股票
                dp[i][j][1] = max(
                    dp[i-1][j][0] + prices[i] , dp[i-1][j][1] 
                )
        
        # 最大收益在沒有拿股票的時候,
        return dp[len(prices)-1][2][1]
        

class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        
        # 這邊寫的是以下四個操作後最低的購買成本與販售後收益
        firstBuy = float('inf')
        firstSell = 0 
        secondBuy = float('inf')
        secondSell = 0 
        
        # 以下每一個iterative,都可以看作,走到目前為止,以下四個動作的最低購買成本與販售收益
        for i in range(len(prices)): 
            
            firstBuy = min(firstBuy  , prices[i]) 
            firstSell = max(firstSell , prices[i] - firstBuy) 
            secondBuy = min(secondBuy , prices[i] - firstSell )
            secondSell = max(secondSell , prices[i] - secondBuy)
            

        return secondSell

    

class Solution2:

    def maxProfit(self, prices: List[int]) -> int:
        
        # 這邊寫的是以下四個操作後最低的購買成本與販售後收益
        firstBuy = float('-inf')
        firstSell = 0 
        secondBuy = float('-inf')
        secondSell = 0 
        
        # 以下每一個iterative,都可以看作,走到目前為止,以下四個動作的最低購買成本與販售收益
        for i in range(len(prices)): 
            
            firstBuy = max(firstBuy  , -prices[i]) 
            firstSell = max(firstSell , prices[i] + firstBuy) 
            secondBuy = max(secondBuy , firstSell - prices[i] )
            secondSell = max(secondSell , prices[i] + secondBuy)
            

        return secondSell



S = Solution2()
# print(S.maxProfit(prices = [3,3,5,0,0,3,1,4]))
print(S.maxProfit(prices = [7,6,4,3,1]))
