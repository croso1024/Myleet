class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort( key = lambda x : x[0]  )
        sol = [] 
        temp = None 
        for interval in intervals:  
            
            if temp is None : 
                temp = [interval[0] , interval[1]] 
            else : 
                
                if temp[1] >= interval[0] : 
                    temp[1] = max( interval[1] , temp[1])   
                else : 
                    sol.append(temp) 
                    temp = [interval[0] , interval[1]] 
        
        sol .append(temp) 

        return sol 




        