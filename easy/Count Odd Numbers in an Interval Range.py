""" 
    題意:
        給定low,high作為邊界 , 計算這個範圍內有多少奇數(包含bound) 
    
    思路:
        只有4種case 
        - low:odd , high:odd :  (high-low)//2 + 1  
        - low:even , high:even : (high-low)//2     
        - low:odd , high:even :  (high-low)//2 + 1  
        - low:even , high:odd : (high-low)//2 + 1 
"""
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        if low%2 == 0 and high % 2 == 0 : 
            return (high-low)//2 
        else : 
            return (high-low)//2 + 1 