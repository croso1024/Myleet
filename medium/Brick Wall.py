
from typing import List 
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        
        gapMap = dict() 
        for row in wall : 
            acc = 0 
            for block in row[:-1] : 
                acc += block 
                if acc in gapMap:gapMap[acc]+= 1 
                else : gapMap[acc] = 1 
        # we get the wall gap map , so we can calculate the vertical line which 
        # across the minimum number of block .
            
        if gapMap : 
            
            return len(wall) - max(gapMap.values()) 
            
        else : 
            return len(wall)                

S =Solution()
print(S.leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]))
# print(S.leastBricks([[1],[1],[1]]))