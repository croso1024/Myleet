from typing import List 

# merge interval , then return the length after merge
class Solution:

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort() 
        sol = 0         
        currentInterval = points[0]
        
        for i in range(1 , len(points)): 
            nextInterval = points[i] 
            
            # check 重疊 , 只抓真正的重疊區間
            if currentInterval[1] >= nextInterval[0] : 
                # currentInterval[0] = nextInterval[0] 
                currentInterval[1] = min(currentInterval[1] , nextInterval[1])  
                
            # 沒有重疊, 把current 加入,但這一題實際上不用返回merged interval , 只要計數
            else : 
                sol += 1 
                currentInterval = nextInterval 
                
        return sol + 1 
    

S = Solution() 
print(S.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
        