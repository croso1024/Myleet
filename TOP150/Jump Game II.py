
from typing import List 


# Jump game , 改為一定能走到最後 , 但求到達最後的最小步數 
# 算是DP的雙loop解
class Solution:
    
    # Dynamic Programming , dp[i] 代表到達這一格的最小步數
    # dp[0] = 0 
    # dp[i] = dp[i-j] + 1  if  nums[i-j] 可以走到 i  
    def jump(self, nums: List[int]) -> int:
        
        size = len(nums) 
        dp = [ float("inf") for i in range(size)]
        dp[0] = 0 
        
        for i in range(size): 
            
            for j in range(i ,   min(i+nums[i]+1 , size)): 
                
                dp[j] = min(dp[j]  , dp[i] + 1 )
                
        return dp[size-1]
    


from collections import deque
class Solution:
    
    # BFS的概念 , 在每一步把可以到達的加入queue 
    def jump(self, nums: List[int]) -> int:
        
        queue = deque() 
        # 存入其index和可以跳的格子數
        queue.append(  ( 0 , nums[0]) ) 
        visited = set() 
        step = 0 
        
        while queue:
            
            size = len(queue) 
            
            for i in range(size): 
                
                cur_pos , cur_reach = queue.popleft()  
                if cur_pos == len(nums)-1 : return step 
                
                
                for j in range( cur_pos , min(cur_pos+cur_reach+1 , len(nums) ) ):  
                    
                    if not (j , nums[j]) in visited : 
                        queue.append((j , nums[j]))
                        visited.add((j , nums[j]))
                    
            step += 1 
        
        return False 
                
from collections import deque
# BFS 拿掉visited , 只要注意不要加入重複
class Solution:
    
    # BFS的概念 , 在每一步把可以到達的加入queue 
    def jump(self, nums: List[int]) -> int:
        
        queue = deque() 
        # 存入其index和可以跳的格子數
        queue.append(  ( 0 , nums[0]) ) 
        step = 0 
        
        while queue:
            
            size = len(queue) 
            
            for i in range(size): 
                
                cur_pos , cur_reach = queue.popleft()  
                if cur_pos == len(nums)-1 : return step 
                
                for j in range( cur_pos+1 , min(cur_pos+cur_reach+1 , len(nums) ) ):  
                    queue.append((j , nums[j]))
                    
            step += 1 
        
        return False 