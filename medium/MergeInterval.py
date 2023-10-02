from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals) == 1 : return  intervals
        # sort the every intervals use the "start"
        intervals.sort( key = lambda interval : interval[0]) 
        # print(intervals)
        
        current_interval = intervals[0] 
        result = [] 
        
        for start , end  in intervals[1:] :  

            # case.1  Need expand the current interval
            if current_interval[1] >= start and current_interval[1] <= end  : 
                current_interval[1] = end 

            if current_interval[0] >= start and end >= current_interval[0] :  
                current_interval[0] = start 


            # case.2 Cut-off interval 
            if current_interval[1] < start or current_interval[0] > start : 
                result.append(current_interval) 
                current_interval = [start , end] 
        
        result.append(current_interval)
        
        # print(result) 
        return result 
    
C = Solution() 
C.merge([[1,4],[4,4],[4,12],[8,10]])
C.merge([[1,4],[0,4]])
C.merge([[1,4],[0,0]])
C.merge([[2,3],[3,5],[6,7],[8,9],[11,15]])