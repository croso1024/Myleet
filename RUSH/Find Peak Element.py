
from typing import List 

class Solution:

    def findPeakElement(self, nums: List[int]) -> int:
        
        if len(nums) == 1 : return 0
        
        left = 0 
        right = len(nums) - 1  
        
        while (left <= right) :

            mid = left + (right-left)//2
            
            # special case 
            if mid == 0 or mid == len(nums) - 1 : 
                
                if mid == 0 and nums[mid] > nums[mid+1] : return mid
                elif mid == 0 : 
                    left = mid + 1 
                elif mid == len(nums) - 1 and nums[mid] > nums[mid-1] : return mid  
                elif mid == len(nums) - 1 :
                    right = mid - 1 
                
            else : 
                
                if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1] : 
                    return mid 
                elif nums[mid + 1] >= nums[mid-1] : 
                    left = mid + 1 
                else : 
                    right = mid - 1 
        
        return -1 
    
S = Solution()
print(S.findPeakElement([1,2,1,3,5,6,4]))