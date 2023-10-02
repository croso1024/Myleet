""" 
    思路 : 
        這一題是經典的機器人走到某一個的方法數有多少的問題 使用DP來做
        機器人從左上出發要到右下角 ,且每一步都只能走往下或往右 ,求到終點的方法數有多少種
        
        我們用DP-Table dp[i][j] 紀錄機器人到達 i,j這個格子的方法數 ,
        
        到達i,j的方法數 : dp[i][j] = dp[i-1][j] + dp[i][j-1]  
        base case則是i或j等於0的時候 , 都只有一種方式可以到達 (單純往右或往下)
        
        因此這一題就是建一個DP table計算完成就結束 
"""



class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        
        # 建立一個 m x n 的dp table, 不預留欄位了 
        dp =[ [None for i in range(n)]  for j in range(m) ]    
        
        # 直接把0列0行初始化為1, 這樣在迴圈內也不用在判斷 
        for i in range(m) : dp[i][0] = 1 
        for i in range(n) : dp[0][i] = 1 
        
        
        # 題目有給說 m , n 至少>=1 
        for i in range(1,m): 
            for j in range(1,n) : 
                
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        # 到這邊就取得完整dp table , 答案就在表的右下角 
        return dp[-1][-1]    
    
        
        