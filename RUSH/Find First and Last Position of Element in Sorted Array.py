from typing import List 



# perform normal binary search to find element 
# then find the left & right bound by second binary search 
class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        left = 0 
        right = len(nums) - 1 
        
        def LBS(left , right):
            
            while (left <= right):
                mid = left + (right-left)//2 
                if nums[mid] == target : 
                    right = mid -1 
                elif nums[mid] > target : 
                    right = mid - 1 
                else : 
                    left = mid + 1 
            return left 
            
        def RBS(left , right): 
            while (left <= right):
                mid = left + (right-left)//2 
                if nums[mid] == target : 
                    left = mid +1 
                elif nums[mid] > target : 
                    right = mid - 1 
                else : 
                    left = mid + 1 
            return right
                
        while (left <= right):
            
            mid = left + (right-left)//2 
            
            if nums[mid] == target : 
                leftBonud = LBS(left , mid-1 )
                rightBound = RBS(mid + 1 ,right) 
                return [leftBonud , rightBound]
            elif nums[mid] > target : 
                right = mid - 1 
            else : 
                left = mid + 1 
        
        # if leave the outer while loop -> target value doesn't exist in nums array
        return [-1,-1] 


class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def LBS():
            left = 0 
            right = len(nums) - 1 
        
            while (left <= right):
                mid = left + (right-left)//2 
                if nums[mid] == target : 
                    right = mid -1 
                elif nums[mid] > target : 
                    right = mid - 1 
                else : 
                    left = mid + 1
                     
            if not (left >=0 and left < len(nums)): 
                return -1 
            
            return left if nums[left] == target else -1  
                
        def RBS(): 
            left = 0 
            right = len(nums) - 1 
            while (left <= right):
                mid = left + (right-left)//2 
                if nums[mid] == target : 
                    left = mid +1 
                elif nums[mid] > target : 
                    right = mid - 1 
                else : 
                    left = mid + 1 
            
            if not (right >=0 and right < len(nums)) : 
                return -1 
            return right if nums[right] == target else -1 
        
        return [LBS() , RBS()]                