""" 
    Given definition of 'monotonic array' , is monotone increasing/decreasing. 
    this problem give us a nums array , just need to judge wheather this array is monotonic?

    I think we have two different siutation need discuss , 
    1. increasing 
    2. decreasing  , 
    The foremost thing is decide : this array is increasing type or decreasing type. 
    Note. the array given by problem isn't a sorted array(incre/decre), 
    so the type of array we must decide dynamically

"""
from typing import List 
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        size = len(nums)

        increasing = None 

        for i in range(1, size):

            if increasing is None :  

                if nums[i] - nums[i-1] == 0 : pass 
                elif nums[i] -  nums[i-1] > 0 : 
                    increasing = True 
                else: 
                    increasing = False 
            
            if increasing : 

                if nums[i] -  nums[i-1] < 0 : return False 
            
            else : 

                if nums[i] - nums[i-1] > 0 : return False 
        
        return True 