
class Solution:
    
    def insert(self, intervals, newInterval) :

        sol = list() 
        
        currentInterval = newInterval 
        
        # 如果有重疊, 就擴張,沒有就把當前interval加入
        for interval in intervals : 
            
            if currentInterval[0] <= interval[0] and currentInterval[1] >= interval[0] : 
                currentInterval[1] = max(interval[1] , currentInterval[1])   
                
            elif currentInterval[0] >= interval[0] and currentInterval[0] <= interval[1] :
                currentInterval[0] = interval[0] 
                currentInterval[1] = max(currentInterval[1] , interval[1])  
            
            else : 
                
                if currentInterval[1] < interval[0] : 
                    sol.append(currentInterval)
                    currentInterval = interval 
                elif currentInterval[0] > interval[1] : 
                    sol .append(interval) 
        
        sol.append(currentInterval)
        return sol 
            
        
        
        
    
    
S = Solution() 
print(S.insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]))

             