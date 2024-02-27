""" 
    Given a integer array nums and an integer k . 
    we can perform k time 'plus 1' on any element in the array. 
    The problem want to find the most frequent element after these operation. 
    
    I think we can use sort + sliding-window approach to solve this problme. 
    After sorting, the element in the array will present by ascending order , 
    it's mean array[i] <= array[i+1] .  

    and we maintain a window , use k operation let all element in window equals max(window).
    once the 'k' time not enough , we contract the window end drawback the value give 
    for small number.

"""
from typing import List 
class Solution:

    def maxFrequency(self, nums: List[int], k: int) -> int:
        # sort integer array first 
        nums.sort() 

        left , right = 0 , 0
        solution = 0
        prevElement = None 
        needed = 0

        # we use a open interval [left , right) 
        while right < len(nums): 

            # we use the maximum value in window as pivot
            curElement = nums[right]
            
            # then check wheather k value enough to compensate 
            if prevElement : 
                needed = (curElement - prevElement) * (right - left)  
                k -= needed 
            # i put the right plus one here , for the correctness of needed calculate 
            right += 1 

            # when needed > k , shrink the window to decrease the needed

            while k < 0  :

                leftElement = nums[left]   
                k += ( curElement - leftElement )  
                left += 1 

            # At this line , the needed <= k , so we can update the solution now 
            prevElement = curElement  
            solution = max(solution , right-left )  
        
        return solution 
            

 


















