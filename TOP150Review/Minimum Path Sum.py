
class Solution:

    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m = len(grid) 
        n = len(grid[0]) 

        # def : dp[i][j] : minimum cost to arrive grid[i][j] 
        dp = [ [ None for i in range(n)] for j in range(m) ] 

        # base-case : dp[0][0] = grid[0][0] 
        dp[0][0] = grid[0][0] 

        for i in range(m) : 
            for j in range(n):  

                if i == 0 and j == 0 : pass 
                elif i==0 :  
                    dp[i][j] = dp [i][j-1]  + grid[i][j] 
                elif j == 0 : 
                    dp[i][j] = dp[i-1][j] + grid[i][j ] 
                else : 
                    dp[i][j] = grid[i][j] + min( dp[i-1][j] , dp[i][j-1]  )

        return dp[m-1][n-1] 


# State compression
class Solution:

    def minPathSum(self, grid: List[List[int]]) -> int:
                 
        m = len(grid) 
        n = len(grid[0]) 

        # first row :  
        prev_row  = [None for i in range(n)]
        temp = 0 
        for i in range(n): 
            temp += grid[0][i]
            prev_row[i] =  temp  

        for i in range(1 , m): 

            new_row = [None for i in range(n)]  

            for j in range(n): 

                if j == 0 : 
                    new_row[j] = prev_row[j] + grid[i][j] 
                else : 
                    new_row[j] = grid[i][j] + min(new_row[j-1] , prev_row[j]) 

            prev_row = new_row 

        return prev_row[-1] 
                    
