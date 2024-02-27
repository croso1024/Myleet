""" 
    題意:
        給定一個cost array , 其元素代表僱用 i-th worker的cost. 
        同時還有給定另外兩個整數 , k與candidate . 我們需要依據以下規則僱用剛好k個員工
        - 我們可以展開k次session , 但每個session一次只能hire一個員工
        - 每次的Session , 我們都只能選擇剩餘人選的前candidate個或後candidate個
        - 在每次的session , 我們都要選擇cost最低的員工 , 如果cost一樣抓index小的 
    
    思路:   

        雙指標從兩端將人選加入 , 接著做heap pop , 看是哪邊的被pop出來就在對應方向繼續抓人進heap 
        需要注意一下兩邊指標交匯的問題.
    
"""

from typing import List 
from heapq import heappop , heappush

""" 
    解法一. 雙端指標+heap ,
        TC :  前面放candidate : (candidate log (candidate)) + 後面走k次session k log (candidate) 
        worse case -> NlogN 
        MC : 2 candidate , O(N)
"""
class Solution:

    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        
        heap = [] 
        sol = 0 
        left , right = 0 , len(costs) - 1 
        
        
        # Put the candidate in the selection pool 
        while left < candidates : 
            heappush( heap , ( costs[left] , left ) )
            left += 1  
        
        while right > len(costs) - candidates - 1 and right >= left : 
            heappush( heap , (costs[right] , right )) 
            right -= 1     
        
        
        # we will hold k session to hire k people 
        for i in range(k):
            
            # every session , we hire one people than update the heap 
            hire_cost , hire_index = heappop(heap) 
            sol += hire_cost 
            print(hire_cost )
            # hire index must in the interval :     hire_index < left or hire_index > right 

            # in the left handside
            if hire_index < left  and left <= right  : 
                heappush( heap , (costs[left] , left) ) 
                left += 1 
                
            elif hire_index > right and left <= right : 
                heappush(heap , (costs[right] , right) )
                right -= 1 
        
        return sol 

S = Solution()
S.totalCost(costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4)