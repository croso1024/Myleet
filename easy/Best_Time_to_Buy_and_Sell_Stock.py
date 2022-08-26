# 第一次寫的是Solution2的作法 最慢, 會跑超時
# 第二次寫的是Solution 測試上比一開始快, 會在更後面的測資超時
# 第三次的是參考discussion  , 天才

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0 
        # 由便宜到貴的日子 --> 當作購買日
        ref = sorted(range(len(prices)) , key = lambda index : prices[index] ) 
        # 由貴到便宜的日  --> 當作販售日
        ref_inv = ref[::-1]

        for buy_day in ref: 
            for sell_day in ref_inv: 
                if sell_day < buy_day : pass  
                else: 
                    profit = prices[sell_day] - prices[buy_day]  if prices[sell_day] - prices[buy_day]  > profit else profit 
                    break 

        return profit 

class Solution2: 
    
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0 
        
        for index , price in enumerate(prices[:-1]):    
            temp = max(prices[index+1:]) - price   
            profit = temp if temp > profit  else profit 
            
        return profit 


class Solution3: 
    def maxProfit(self,prices): 
        minprice = float("inf")
        maxProfit = 0 

        for price in prices:
            if price < minprice: minprice = price 

            maxProfit = price-minprice if price-minprice > maxProfit else maxProfit 
        return maxProfit

C = Solution() 
#D = Solution2()  too slow !
E = Solution3() 
from random import randint as r 
from time import time as t

test = [r(0,999) for i in range(999999)]
start = t() 
print(C.maxProfit(test ))
print(t() - start )

start = t() 
print(E.maxProfit(test ))
print(t() - start )