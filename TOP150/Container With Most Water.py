
from typing import List 

class Solution:
    
    # [ 1,6,3,5,2 ]
    def maxArea(self, height: List[int]) -> int:
    
        left = 0 
        right = len(height) - 1  
        best = float("-inf")
        # width = right - left   
        while right > left : 
            
            if height[left] > height[right] : 
                best = max(best , (right-left)*height[right]  )
                right -=  1 
            else : 
                best = max(best , (right-left)*height[left]  )
                left += 1 
        
        return best 
            
            