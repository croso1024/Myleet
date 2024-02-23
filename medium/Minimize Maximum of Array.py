""" 
    Naive solution : Reverse iterate the array and move the high value to the left 
    -> Exceed time limit 
"""
from typing import List 
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        done = False 
        while not done: 
            done = True 
            for i in range(len(nums)-1 , 0 , -1):  
                if nums[i] > nums[i-1] : 
                    temp =  (nums[i] + nums[i-1] ) 
                    if temp % 2 == 0 : 
                        nums[i] = nums[i-1] = temp // 2 
                    else :  
                        nums[i] = temp // 2 
                        nums[i-1] = ( temp // 2 ) + 1 
                    done = False 
        return max(*nums)


""" 
    Method.2 : Prefix Sum + Average solution , 
    Calculate the prefix sum first , and create a dp table , 
    dp[i] represent the maximum value can by form in nums[0:i+1] 
    
    then , state transformation function : 
    dp[i] = max(dp[i-1] ,   ceil (prefixsum[i] // (i+1)) )
"""
from math import ceil 
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:

        prefix_sum = [None for i in range(len(nums))]
        prefix = 0 
        for i in range(len(nums)) : 
            prefix += nums[i]
            prefix_sum[i] = prefix

        dp = [None for i in range(len(nums))] 
        dp[0] = nums[0] 

        for i in range(1,len(nums)): 

            dp[i] = max(
                        dp[i-1] ,  ceil(  prefix_sum[i] / (i+1) )
                    )

        return dp[-1]

""" 
    Optimize of method.2 , use state compression skill 
"""
from math import ceil 
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:

        current_sum = nums[0] 
        current_maximum = nums[0] 

        for i in range(1 , len(nums)): 

            current_sum += nums[i]
            current_maximum = max(current_maximum ,     ceil(current_sum / (i+1) ) )
        return current_maximum




