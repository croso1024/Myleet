from typing import List 


class Solution:
    
    # dp solution ,
    # dp[i][j] mean the unique path arrive i,j
    # base-case : dp[0][0] = 1 
    # dp[i][j] == 0 if grid[i][j] = 0 
    # state transtion  : dp[i][j] = dp[i-1][j] + dp[i][j-1]      
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        height , width = len(obstacleGrid) , len(obstacleGrid[0]) 
        
        dp = [ [0 for i in range(width)] for j in range(height) ] 
        
        
        for i in range(height) : 
            
            for j in range(width): 
                
                if obstacleGrid[i][j] == 1 : continue 
                
                if i == 0 and j == 0 :  dp[i][j]  =  1 
                elif i == 0 :  dp[i][j] = dp[i][j-1] 
                elif j == 0 :  dp[i][j] = dp[i-1][j]
                else : 
                    
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[height-1][width-1]