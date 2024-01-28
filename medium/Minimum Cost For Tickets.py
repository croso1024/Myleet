from typing import List 

""" 
    思路: 
        買票題， 給定一個days array , 代表要搭車的"日子" , 以及一個Cost array ,分別代表1天,7天與30天的票價  
        day array的範圍為 1<=days[i]<=365 , 假設我們在第3天買七日票 , 則 3,4,5,6,7,8,9都可以使用 
        因此這一題就問,要再所有日子都能搭車的最少cost是多少 
        
        每一個搭車日 , 我們都有三個選擇 , 購買1,7,30天的票( 假設票價合理 1日票<=7日票<=30日票) , 使用DP來求解這一題 
        這一題的困難點在於 ,我很難直接將狀態定義在dp-table中 ,
        例如直觀的將dp[i]做為搭乘days[0]到days[i]範圍的最小cost , 並且想用 前7/30日範圍內的最小cost來算當下cost
        我們也很難知道在前7/30日所得到的cost是不是依靠更前面就買得票 , 到當前已經失效的狀況
        
        這一題是看Solution來找到解法 , 一樣是使用DP , 但加上兩個queue來輔助 , 
        dp[i] 一樣如上定義 , 是搭乘到days[i]最便宜的價格 , 
        
        -- 整個function開始 : 

            首先在dp[0] = 設定為最便宜的票( 因為測資會有7日票比起1日票更便宜的case ) 
            同時把在第一天買7/30日票放進queue

            接著迭代走過days[1:] , 
            每一輪迭代 , 先將已經無效的7/30日票從queue中去除 ,
            接著計算dp[i] , 只有3種case : 
            
                1. dp[i-1] + cost[0] 單日票加上到達前一個的最便宜價格
                2. 7天queue拿出來的價格 
                3. 30天queue拿出來的價格 
            
            計算完到達dp[i]的值後 , 也要去將"如果當天買7/30票的價格"加入Queue , 具體就是dp[i-1]的價格加上票價
            並且將其加入queue中
             
            這一題考驗的思路算是相當複雜 , 以上解法時間O(N) , 空間O(N) , 實際結果都很優            
"""

from collections import deque
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        dp = [0 for i in range(len(days))] 
        # 用來保存先前7/30天內買過得票卷
        queue7 = deque()
        queue30 = deque() 
        
        # 加入base case : 
        dp[0] = min(costs)
        queue7.append( (days[0] ,  costs[1]) )
        queue30.append( (days[0],  costs[2]) )
        
        
        # 主迴圈 , 每天的價格就是到達前一天的價格+單日 , 或著從queue中去看是不是先前的queue價格能夠cover到
        for i in range(1,len(days)): 
            
            # 先把日期不和條件的queue7 / queue30給排除
            while queue7 and ( days[i] -  queue7[0][0] >= 7 ) :
                queue7.popleft() 
            
            while queue30 and (days[i] -queue30[0][0] >= 30):
                queue30.popleft() 
            
            # 接下來就計算這一回合的dp, 買當日票/使用先前的7,30日票這幾種作法
            pass1 = dp[i-1] + min(costs)
            pass2 = queue7[0][1] if queue7 else float("inf")
            pass3 = queue30[0][1] if queue30 else float("inf") 
            
            dp[i] = min(pass1,pass2,pass3) 
            
            # 最後要考慮如果在今天買7/30日票的狀況 , 價格是dp[i-1] + costs[1] , dp[i-1] + costs[2] 
            queue7.append( ( days[i] , dp[i-1] + costs[1] ) ) 
            queue30.append( ( days[i] , dp[i-1] + costs[2] ) ) 
        return dp[len(days)-1]

days = [1,4,6,7,8,20]
costs = [2,7,15]
S = Solution() 
S.mincostTickets(days , costs) 
