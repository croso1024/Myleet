""" 
    題意: 
        給定一組數列nums , 其中可能包含duplicate element . 
        要求返回所有 unique permutation
        
    思路: 
        這一題帶有duplicate element , 所以在backtrack的外層展開的時候要有意地跳過所有相同element
    
"""
from typing import List 

""" 
    解法一. 就是帶有跳過相同值的backtrack , 展開到底後只有size等於的才可以被納入solution
"""
class Solution:
    
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        size = len(nums)
        solution = [ ]

        # 做一個sort , 因為我的跳過機制是直接看當前值是否等於前一個值
        nums.sort()
        
        
        def backtrack( action : list , track : list) -> List : 
            
            if not action and len(track) == size : 
                solution.append( list(track) ) 
                return 
            
            # prev用來紀錄前一個丟進展開的action number 
            prev = None 
            
            for idx , number in enumerate(action) :  
                
                if prev == number : continue 
                
                prev = number 
                track.append(number)
                backtrack( action[:idx] + action[idx+1:] , track )
                track.pop()
                
                
            return 
        
        backtrack(nums , [])            
        
        return solution