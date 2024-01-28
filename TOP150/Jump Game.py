from typing import List 


# dp solution : dp[i] : 在這一格可以到達的最大距離
# state transition : 
class Solution:
    
    def canJump(self, nums: List[int]) -> bool:

        size = len(nums)
        canReach = [False for i in range(size)]
        canReach[0] = True 
        
        for i in range(size): 
            
            if canReach[i] : 
                
                for j in range( nums[i]+1  ): 

                    canReach[i+j] = True    
                    if i+j == size-1 : return True 
        
        return False  



class Solution:
    
    # canReach 保存目前可以走到的最大值 
    def canJump(self, nums: List[int]) -> bool:
        size = len(nums)
        canReach = nums[0]  
        step = 0  
        # step 則是目前的位置 , 必須要小於等於可以到達的位置 
        while step <= canReach :  
            
            canReach = max(  step + nums[step]   , canReach  ) 
            step += 1 
            
            if canReach >= size - 1 : return True 
            
        return False 
    
    

# 使用DP
class Solution:
    
    # dp[i] 代表可以走到的最大值 : dp[i] = i + nums[i]  
    def canJump(self, nums: List[int]) -> bool:

        size = len(nums) 
        dp = [None for i in range(size)]

        maximum_can_reach = nums[0]

        dp[0] = nums[0]
        
        for i in range(1 , size): 
            
            if maximum_can_reach < i : return False 
            
            dp[i] = max( i+nums[i] , dp[i-1]  )
            maximum_can_reach = max(dp[i] , maximum_can_reach) 
        
        
        return True if maximum_can_reach >= size-1 else False 
        