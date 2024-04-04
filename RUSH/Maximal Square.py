from typing import List 

# dp solution , use "left" , 'up' , 'left up' to formulate a more big square 
class Solution:

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        # definition of dp[i][j] : the biggest square side length include the matrix[i][j]
        dp = [[ None for i in range(len(matrix[0])) ] for j in range(len(matrix)) ]
        maximum_square = 0
        for i in range(len(matrix)) : 
            
            for j in range(len(matrix[0])) : 

                if i == 0 or j == 0 : 
                    dp[i][j] = int(matrix[i][j]) 

                elif matrix[i][j] == "0": 
                    dp[i][j] = 0 
                else : 
                    dp[i][j] = 1 + min( dp[i-1][j] , dp[i][j-1] , dp[i-1][j-1])

                maximum_square = max(maximum_square , dp[i][j])
               
                    
        return maximum_square**2
