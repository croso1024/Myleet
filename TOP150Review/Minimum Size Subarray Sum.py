
# sliding window , easy to keep track the window content 
class Solution:

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left = 0 
        right = 0 
        window = 0 
        sol = float("inf") 

        # use open interval [left , right) 
        while right < len(nums): 

            window += nums[right]
            right += 1 

            
            while left < right and window >= target : 
                sol = min(  right-left   , sol  )
                window -= nums[left]
                left += 1 
            
        return sol if sol != float("inf") else 0 
