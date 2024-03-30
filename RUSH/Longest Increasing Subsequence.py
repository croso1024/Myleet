from typing import List 

# dp solution , dp[i] : the longest increasing subsequence stop at i 
class Solution:
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1 for i in range(len(nums))]
        
        for i in range(1 , len(nums)): 
            
            for j in range( i ): 
                
                if nums[i] > nums[j] : 
                    
                    dp[i] = max( dp[i] , 1 + dp[j] ) 
        
        print(dp)
        return max(dp) 
                    
                    
S = Solution()
S.lengthOfLIS([10,9,2,5,3,7,101,18,3,5,3,7])
            
            
            
            
        