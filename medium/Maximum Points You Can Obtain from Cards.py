""" 
    題意:
        給定一個整數array cardPoint,代表每一張卡片的分數 
        在每一個回合,我們都可以從最前面或最後面拿走一張卡片 
        題目要問在總共的k個回合中我們可以得到的最高分數
        
    思路:
        我的想法是prefix , 將cardPoint從左至右,以及從右至左都計算prefix
        這樣 , 在拿k個數值的時候相當於 拿左邊n個加上右邊m個 , m+n = k
        
        如此一來traverse一次 m+n的組合take O(N)就可以得到解
        而前面計算prefix也是O(N)
        Totally TC:O(N) , MC:O(N)
        
        我看解答 , 一個更加天才一點點的做法就是計算整個array的sum
        然後以 len(cardPoint) - k 的範圍作為window去減掉sum , 取最大值
        
"""

""" 
    解法一. 
        雙邊prefix
        這個解的時間偏差 , 但O(N)應該就是這個題目的最佳解沒錯 ,我猜是我寫code的方式 
        至於空間則還不錯.
        
        我看
"""
from typing import List 

class Solution:

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        
        # LR[i]: 從cardPoint[0]累加到cardPoint[i]的值
        # RL[i]: 從cardPoint[i]累加到cardPoint[ len(cardPoint)-1  ]的值 
        LR = [None for i in range(len(cardPoints))]
        RL = [None for i in range(len(cardPoints))]

        sum = 0 
        for i in range(len(cardPoints) ):
            sum += cardPoints[i]
            LR[i] = sum  
        
        sum = 0 
        for i in range(len(cardPoints)-1 , -1, -1 ): 
            sum += cardPoints[i] 
            RL[i] = sum
        
        # 要快速計算左邊取n個加上右邊取m個的總分 , 但要跳過n == 0 or m == 0
        # LR[n-1] + RL[len(cardPoint)-m]
        
        sol = float("-inf")
        # 從左邊取0->k個 , 從右邊取k->0個
        for n in range(k+1):

            if n == 0 : 
                
                sol = max(sol , RL[len(cardPoints)-k] )
                
            elif n == k : 
                
                sol = max(sol , LR[k-1])
                
            else : 
                
                sol = max(sol , LR[n-1] + RL[len(cardPoints)-k+n])
         
        
        return sol 