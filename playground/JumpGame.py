class Solution:
    def canJump(self,nums): 
        
        # use Dynamic programming , 
        # dp[i] represent the maximum reach position by nums[0 - i] 
        
        dp = [None] * len(nums)
        
        dp[0] = nums[0]  
        maximum_can_reach = nums[0]
        
        for i in range(1 , len(nums)): 
            
            if maximum_can_reach < i : return False 
            
            dp[i] = max( i + nums[i] , dp[i-1] )
            
            maximum_can_reach = max(dp[i] , dp[i-1])
        
        return maximum_can_reach >= len(nums)-1

S = Solution()

print(S.canJump([2,3,1,1,4]))
print(S.canJump([3,2,2,0,3,2,1,0,5]))


            
        
        