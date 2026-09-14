"""
題意 :
給定一個 Array[int] , 代表每天的股價. 
我們只能做一次買+賣 , 求最大收益. 若無法有最大收益則回0 

Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 104

思路 :

雙指標 , left 標代表買 , right 標表示賣出.
求 maximize : right-left  

後續思考後的思路 , 其實應該只要走一圈,單指標能搞定.


複雜度 : Time O(?) / Space O(?)

Trade-off :

"""

from typing import List 
class Solution:

    def maxProfit(self, prices: List[int]) -> int:

        
        cur = 0 
        size = len(prices) 

        max_profit = 0 

        while cur + 1 < size : 

            probe = cur + 1  

            while probe < size : 

                if prices[probe] > prices[cur] : 
                    max_profit = max( max_profit , prices[probe]  - prices[cur] ) 
                    probe += 1 
                else : 
                    cur = probe 
                    break 
        
        return max_profit



class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # 記錄一路上看過最低的價格,然後一直比. 
        max_profit = 0 
        lowest_price_so_far = float("inf") 

        probe = 0 

        while probe < len(prices) : 

            lowest_price_so_far = min(lowest_price_so_far , prices[probe]) 
            max_profit = max( max_profit , prices[probe] - lowest_price_so_far )  
            probe += 1 
        
        return max_profit

