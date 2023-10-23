
""" 
    思路 : 
        這一題乍一看我覺得有點像Back track , 去爆搜走到右下角的所有軌跡並找出其中最小的值 , 
        實際上我覺得確實可以這麼做 , 但這一題的問題條件告訴說 m x n ,最大會到200x200 ,這讓backtrack不太現實.
        
        因此一定有其他更好的作法可以去處理 , 實際上仔細想一下這一題要的是走到右下角那一個最小的sum 
        從DP的思路來說 -> "思考在我們有全部資訊的情況下 , 要怎麼得到解"
        答案就是 : 右下角的最小sum等於 右下角的值 + min (右下角上面那格的最小sum , 右下角左邊那格的最小sum) 
        
        因為這一題跟Unique path很像 , 我們從起點只能走右邊或下面 , 因此可以用類似的方式推進DP table
        此題屬於2維DP table , 
        DP Table定義為 : dp[i][j] 待表走到 i,j 這個位置的最小path sum 
        DP state transition function :  dp[i][j] = grid[i][j] + min( grid[i-1][j] , grid[i][j-1] )

"""

""" 
    就是按照上面的想法去寫 ,我這次沒有特別先處理first row與first column , 而是將這部份邏輯放進loop
    我個人覺得這樣比較clean , 但我覺得速度可能會隨著問題規模比起先處理的方法還要略遜一點。

"""
from typing import List 

class Solution:
    
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        # create 2-dimension dp table 
        dp = [  [None for i in range(len(grid[0]))]  for j in range(len(grid)) ] 
        
        dp[0][0] = grid[0][0] 
        
        for i in range(len(grid)): 

            for j in range(len(grid[0])): 
                
                if i == 0 or j==0: 
                    # both i ,j ==0 
                    if i==0 and j==0 : continue
                    # only i == 0 -> first row 
                    elif i==0 : 
                        dp[i][j] = grid[i][j] + dp[i][j-1]   
                    # only j == 0 -> first column
                    elif j==0 : 
                        dp[i][j] = grid[i][j] + dp[i-1][j]
                
                else :   
                    dp[i][j] = grid[i][j] + min(dp[i-1][j] , dp[i][j-1])
                
        
        return dp[  len(grid)-1    ][ len(grid[0]) - 1 ]