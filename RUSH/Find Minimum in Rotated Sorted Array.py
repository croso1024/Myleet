from typing import List 

class Solution:

    def findMin(self, nums: List[int]) -> int:
        
        size = len(nums)
        
        if size == 1 : return nums[0]
        elif size == 2 : return min(nums) 
        
        left = 0 
        right = size - 1 
        
        def check( index ):
            
            leftIndex=  (index + size - 1) % size 
            rightIndex =(index + size + 1 ) % size 
            
            if nums[leftIndex] > nums[index] and nums[rightIndex] > nums[index] :
                return True 
            else : 
                return False 

        while (left <= right): 
            
            
            mid = left + (right-left)//2 
            
            if check(mid) : return nums[mid]
            
            if nums[left] > nums[right] : 
                
                if nums[mid] >= nums[left] : 
                    left = mid + 1 
                else : 
                    right = mid - 1 
            
            else : 
                right = mid - 1
        
        return nums[left]
                
        
            
            
        
        
class Solution:

    def findMin(self, nums: List[int]) -> int:
        
        
        if len(nums) == 0 : return float('inf')
        elif len(nums) == 1 : return nums[0]
        elif len(nums) == 2 : return min(nums)
        
        left = 0 
        right = len(nums) - 1 

        if nums[left] < nums[right] : return nums[left] 
        else : 
            mid = left + (right-left)//2
            return min( self.findMin(nums[:mid]) , self.findMin(nums[mid:]))            
            
            
S = Solution()
S.findMin([11,13,15,17,9])