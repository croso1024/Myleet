from typing import List 

# find maximum sum of circular array => find the sum of array - minimum value subarray 

class Solution:

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        n = len(nums) 
        if n == 1 : return nums[0]
        array_sum = sum(nums) 
        # dp_max[i] : the maximum value subarray end at i 
        # dp_min[i] : the minimum value subarray end at i 
        dp_max = [None for i in range(n)]
        dp_min = [None for i in range(n)]
        
        dp_max[0] = nums[0]
        maximum = nums[0]
        # case1 . the maximum subarray appearr doesn't cross the array two side 
        for i in range(1 , n):
            dp_max[i] = max( nums[i] , dp_max[i-1] + nums[i] )
            maximum = max(maximum , dp_max[i])

        dp_min[1] = nums[1]
        minimum = nums[1]
        # case2. the maximum subarray across the two side , => equal to the sum of entire array minus the minimum array 
        for i in range(2 , n-1):
            dp_min[i] = min( nums[i]  ,dp_min[i-1] + nums[i]) 
            minimum = min(minimum  , dp_min[i]) 
        
        return maximum if maximum >= array_sum - minimum else array_sum - minimum
        

class Solution:

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        n = len(nums) 
        if n == 1 : return nums[0]
        array_sum = sum(nums) 
        # dp_max[i] : the maximum value subarray end at i 
        # dp_min[i] : the minimum value subarray end at i 
        
        dp_max = nums[0]
        maximum = nums[0]
        # case1 . the maximum subarray appearr doesn't cross the array two side 
        for i in range(1 , n):
            dp_max = max( nums[i] , dp_max + nums[i] )
            maximum = max(maximum , dp_max)

        dp_min = nums[1]
        minimum = nums[1]
        # case2. the maximum subarray across the two side , => equal to the sum of entire array minus the minimum array 
        for i in range(2 , n-1):
            dp_min = min( nums[i]  ,dp_min + nums[i]) 
            minimum = min(minimum  , dp_min) 
        
        return maximum if maximum >= array_sum - minimum else array_sum - minimum
        
        