"""
    Given an binary array only contain 0 and 1 , 
    If you can arbitrary choose an element delete , return the longest subarray contains all 1

    My intution solution is DFS , cause we can only just delete one element in array 
    so i think , maybe the recursion tree won't be huge  

    but the actually approach should be sliding window !?
"""
# class Solution:
#     def longestSubarray(self, nums: List[int]) -> int:
        
#         solution = 0 
#         size = len(nums )

#         def DFS( i  , canDelete , length  ): 
#             nonlocal solution
#             if i == size : 
#                 solution = max(solution , length-1 ) if canDelete else max(solution , length)
#                 return 

#             if nums[i] == 0 and canDelete : 
#                 DFS(i+1 , False , length  ) 
#                 DFS(i+1 , canDelete , 0)
            
#             elif nums[i] == 0 :   
#                 solution = max(solution , length) 

#             else : 
#                 DFS(i+1 , canDelete , length + 1 ) 

#         DFS(0 , True , 0)
#         return solution 
from typing import List 
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        left , right = 0 , 0
        zeros = 0 
        ones = 0 
        size = len(nums)
        solution = 0

        while right < size: 
            
            if nums[right] == 1 : ones += 1  
            else : zeros += 1 
            right += 1 
            
            if zeros == 0: solution = max(solution , ones-1) 
            else : solution = max(solution , ones)

            while zeros > 1 : 

                if nums[left] == 1 : ones-=1
                else : zeros-= 1 
                left += 1 

        return solution 
                








