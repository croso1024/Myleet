from typing import List 
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        
        sign = 1 
        
        for num in nums : 
            
            if num == 0 : return 0 
            elif num < 0 : sign +=1  
        
        return -1 if sign % 2 == 0 else 1 