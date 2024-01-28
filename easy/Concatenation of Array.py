from typing import List 

class Solution:

    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        
        size = len(nums)
        ans = [None for i in range(size*2)] 
        
        for i in range(size*2): 
            
            ans[i] = nums[   i % size ]
        
        return ans