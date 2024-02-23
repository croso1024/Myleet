""" 
    This problem need a tricky mathmatical approach , we can format all the formula and ovserve it
    Use the test case as example , [4,3,2,6] , we define the '0' as pivot
    
    In first round , we calculate the sum ( F(0) ) directly , and the pivot of this round is 4.
    Second round , we can observe that 
        F(1) = F(0) - nums[(pivot+size)%size] * (size-1) + sum(nums[pivot:pivot+size-1]) 
             = F(0) - nums[(pivot+size)%size] * (size-1) + sum(nums) - nums[pivot] 
    
    That is pretty implict rule. but once we find it , this problem can be solve quite simply 
   


"""
from typing import List 
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        
        size = len(nums)
        totalSum = sum(nums)    
        

        # we still need calculate the first round manual
        lastRound = 0 
        for i in range(size):lastRound += i * nums[i]
        sol = lastRound 
        for i in range(1,size): 
            lastRound = lastRound - ((size-1) * nums[size-i]) 
            lastRound += (totalSum - nums[size-i])
            sol = max(sol , lastRound)
        return sol 
            
