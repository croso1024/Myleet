""" 
    思路 : 
        這一題就是計算到達終點的可行路徑數量 , 但這邊多加了障礙物 . 
        
        直觀的想法是DP , 在base case上需要根據石頭做調整 , 完成第一個row/column作為Base case之後應該就可以直接走DP
        另外一個想法則是BFS , 在BFS的過程去紀錄每一個格子的可到達步數 , 換句話說也是DP , 只是尋訪改為BFS 
"""

from typing import List 
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0]) 
        if obstacleGrid[0][0] == 1 : return 0
        # m x n table 
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0][0] = 1 
        # 填入第一個row的base case 
        temp = 1 
        for i in range(1,m): 
            # 如果第一個column有石頭 , 過了石頭之後的位置都是到不了
            if obstacleGrid[i][0] == 1 and temp : temp = 0 
            dp[i][0] = temp 
        
        temp = 1 
        for j in range(1 , n): 
            if obstacleGrid[0][j] == 1  and temp : temp = 0 
            dp[0][j] = temp 
        
        # 至此填完了base case 
        
        # DP狀態轉移開始 , dp[i][j]  代表到達這一格的路徑數 
        for i in range(1,m): 
            for j in range(1,n): 
                
                if obstacleGrid[i][j] == 1 : continue
                
                # 如果該格子的左邊跟上面都是可以走的 , 那方法數就是相加
                if dp[i][j-1] != 0 and dp[i-1][j] != 0 : 
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
                
                elif dp[i][j-1] != 0 : 
                    dp[i][j] = dp[i][j-1] 
                elif dp[i-1][j] != 0 : 
                    dp[i][j] = dp[i-1][j] 
                # 如果上面和左邊都是無法到達 , 那也代表這格無法到達
                else : 
                    dp[i][j] = 0 

                
        return dp[m-1][n-1]