from typing import List 

# 標準的遞推 , 注意三角形 dp-table的初始化
class Solution:
    # dp solution 
    # base case : dp[0][0] = triangle[0][0] 
    # state transition : dp[i][j] = min( dp[i-1][j-1] , dp[i-1][j] ) beside two end-point
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        
        high = len(triangle)  
        dp = [ [ None for j in range(i) ] for i in range( 1 , high+ 1) ] 

        # base case 
        dp[0][0] = triangle[0][0]
        
        # Outer-loop traverse the vertical direction
        for i in range(1 , high):  
            
            # inner loop traverse the horizontal direction
            for j in range( 0 , i+1 ): 
                
                if j == 0 : 
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif j == i : 
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                else : 
                    dp[i][j] = min( dp[i-1][j-1] , dp[i-1][j]  ) + triangle[i][j]
        
        
        return min( dp[high-1] )
        

# 狀態壓縮 , 只保留前一列 , 增加space性能
class Solution:
    
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        prev_state = triangle[0] 
        high = len(triangle)
        
        for i in range(1 , high):  
            
            new_state = [] 
            
            for j in range(0  , i+1) :  
                
                if j == 0 :  
                    new_state.append( prev_state[0] + triangle[i][j] )
                elif j == i  : 
                    new_state.append( prev_state[j-1] + triangle[i][j] )
                else : 
                    new_state.append( 
                        min( prev_state[j-1] , prev_state[j]  ) + triangle[i][j]
                    )
            
            prev_state = new_state 
        
        return min(prev_state) 
    
    
# Top down + memo 

class Solution:
    
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        high = len(triangle) 
        memo = dict() 
        
        # dp(i,j) 的定義為到達 i , j 格的最小cost 

        def dp(i,j):  
            # base-case , i==0,j==0     
            if i == 0 and j == 0 : return triangle[0][0]
            elif (i,j) in memo : return memo[(i,j)] 
            else : 
                
                # 特殊的case在於 j==0 或著 j == i , 這樣只能往單一方向找 
                if j == 0 : 
                    
                    sol = triangle[i][j] + dp(i-1 , 0) 
                
                elif j == i : 
                    
                    sol = triangle[i][j] + dp(i-1 , j-1)
                    
                else : 
                    
                    sol = triangle[i][j] + min(
                        dp(i-1 , j-1) , dp(i-1,j)
                    )     
                
                memo[(i,j)] = sol 
                return sol 
            
        best = float('inf')
        for j in range(high):  
            best = min(best  , dp( high-1 , j  )  )
        
        return best 
                    
    