
class Solution:

    # 迴圈保持一個指標說明到此前最便宜買入價格 , 在每一格計算最大profit 
    def maxProfit(self, prices: List[int]) -> int:
        
        best = 0 
        min_buy = prices[0] 

        for i in range(1 , len(prices)):  

            best = max(best  , prices[i] - min_buy)  
            min_buy = min(min_buy , prices[i]) 
        
        return best 


        