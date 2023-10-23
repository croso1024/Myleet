
from typing import List 

""" 
    思路 : 
        明確思路的一題1D DP , 而且我覺得比起普通的爬摟梯問題更加有意思 , 加入了minimize cost的元素 
        但還是算很簡單 , 在每一個階梯上只要支付該階梯的cost , 就可以往上爬1或2 
        需要注意這一題所謂的"top" , 依照example來看是要超出array範圍 . 
        
        使用dp[i]表示爬到index = i 處的最小cost , 
        
        dp的state transition function : 
        
        dp[i] = min( cost[i-1] +  dp[i-1]  , cost[i-2] + dp[i-2] ) 
        
        另外因為超出範圍才是到達top 
        因此我們的最終目標是求 
        min (  cost[-1] + dp[-1]  , cost[-2] + dp[-2] )

        note : 題目給定起碼有兩階階梯 
"""

""" 
    解法一. 就爬摟梯問題的變化型而已
"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        if len(cost) == 2 : return cost[0] if cost[0] < cost[1] else cost[1] 
        
        # minimum cost for climb to index=i 
        dp = [None] * (len(cost)) 
        # you can start with index 0 or index 1  , no cost 
        dp[0] = 0 
        dp[1] = 0 
        
        # outer loop to push the state transition 
        for i in range(2,len(cost)):  
            dp[i] = min( cost[i-1] + dp[i-1]  , cost[i-2] + dp[i-2] )
            
        return min( cost[-1] + dp[-1] , cost[-2] + dp[-2]  )
            
            