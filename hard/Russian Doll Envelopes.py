
""" 

    思路 : 
        這一題是東哥DP的範例題目 , 要用到一些特殊的技巧 , 可以將這一題轉化為
        類似 Longest Increasing Subsequence 

        基本上就是先通過對寬度進行sort,並且是升序排序 , 並且如果兩個信封寬度一樣 , 
        則也對長度進行降序排序  
        ex.例題 envelopes = [[5,4],[6,4],[6,7],[2,3]] 
        要排序成 
        [
            [2,3],
            [5,4],
            [6,7],
            [6,4],
        ]
        
        第一個維度針對寬進行排序，確保說上面的信件如果高度允許的話就可以塞進下面的信件
        而第二個維度的高就可以被我們當作找最長遞增訓練的問題 , 只不過會需要跳過相同高度的部份
        
"""

from typing import List 

class Solution:
    
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        # 先對寬度進行升冪排序  , 對高度進行降冪排序 , python內建的排序可以用下面的方式來做
        # 即tuple比較大小時 , 先比第一位才比第二位 
        envelopes.sort(  key = lambda element : (element[0] , -element[1]) ) 
        
        # 接下來比照LIS那一題 , 建立一個dp-table 
        # dp[i]表示以index = i 為結尾作為嵌套的最後一封信時最大的累積數量 
        dp = [1] * len(envelopes)  # 這裡dp[0]就代表第一封 , 不過也必定為1
        
        #外層loop推進dp-state 
        for i in range(1, len(envelopes)): 
            
            # 比較到i為止 , 在滿足寬度與高度的情況下先前的最大嵌套是多少 ,
            # dp[j] = 1 + max(dp[ 0 -> i ] if conditions is satisfy )
            
            # best_with_i  : 初始化以這封信件為結尾的最大嵌套數
            best_with_i = 1 
            
            for j in range(i) : 
                
                if (envelopes[i][0] > envelopes[j][0]) and (envelopes[i][1]  > envelopes[j][1]):
                    best_with_i = max(best_with_i , 1+dp[j])
                
            dp[i] = best_with_i 
        
        # 最終是要返回dp 列表中最大值得結果
        return max(dp)


