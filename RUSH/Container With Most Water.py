from typing import List 

class Solution:

    def maxArea(self, height: List[int]) -> int:
    
        sol = 0 
        left = 0 
        right = len(height) - 1 
        
        while (left < right): 
            
            sol = max(sol ,   min(height[left] , height[right]) * (right-left)  )
            
            if height[left] >= height[right] : 
                right -= 1 
            else : 
                left += 1 
                
        return sol 