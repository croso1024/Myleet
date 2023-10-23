""" 
    思路 : 
        這題要在給定的資料點上 , 去求能夠串連所有資料點的最小距離 , 注意距離使用曼哈頓距離
        即 |x_i - x_j| + |y_i-y_j| .
        
        最直觀的方法是 double loop , 去遍瀝一次就可以 會要 n^2 / 2 得時間

"""

""" 
    解法一. 雙迴圈遍瀝 , 我們只要為每一個節點找到連接距離最短的就可以了 
    但為了避免互相連接的cost重複計算 , 用一個hashtable來存這件事 
    
    --> 這個解法無法處理 如果點群是兩坨密集的 , 那會導致兩坨之間沒有互相連接 
"""
from typing import List 

class Solution:
    
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        if len(points)==1 : return 0 
        
        cost = 0 ; 
        # hash table用來紀錄每個點所連接到的最近鄰居 , 用來避免重複算cost 
        hashtable = dict() 
        def calculateDist(point1,point2) : 
            return abs(point1[0]-point2[0]) + abs(point1[1]-point2[1]) 
            
        
        for i in range(len(points)): 
            
            min_cost_for_i = float("inf")
            min_cost_point_for_i = None 
            
            for j in range(len(points)): 
                
                if i == j : continue
                
                dist = calculateDist(points[i] , points[j])
                
                if dist < min_cost_for_i : 
                    min_cost_for_i = dist 
                    min_cost_point_for_i = j
     
            # 如果節點i所找到的最短連接鄰居已經在hashtable , 且他的最短連接鄰居也是節點i , cost不重複算
            if min_cost_point_for_i in hashtable and hashtable[min_cost_point_for_i] == i : 
                hashtable[i] = min_cost_point_for_i
            
            # 其餘情況來說 , 就是要增加cost , 同時紀錄在hashtable
            else : 
                cost += min_cost_for_i 
                hashtable[i] = min_cost_point_for_i
        
        return cost 
    
    
""" 
    解法二 . 
    
    從DP的概念下手 , 如果今天已經知道 n個點的情況下最小cost是多少 , 那n+1個的最小cost是多少?
    -> 把新增的點和所有點對比 , 增加那個距離最近的點的cost 
    透過這樣一個個新增的方式
"""