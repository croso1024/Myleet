""" 
    思路 :  
        這一類類似predict the winner , 在兩個玩家輪流選擇的情況下去計算遊戲結束時誰的分數高

        對於這類問題 , 使用既定的DP框架,建立一個 2D-DP table 
        
        dp[i][j] = (first , second) , 代表在使用 i ~ j 的石頭堆情況下 , 先手與後手所能得到的最大分數
        -- base case就是對角線 , 只有第一個玩家能拿分

        -- 狀態轉移函數 , 可以從"遞推"的方向思考 , 因為答案存在於 dp[0][-1] , 因此是往右上角去遞推
        
            對於玩家一來說 , 他能拿到的分數就是在左或右被拿掉的遊戲中,後手玩家可以拿到的最大分數加上他這一輪能拿的
            
            dp[i][j].first = max(
                nums[i] + dp[i+1][j].second ,
                nums[j] + dp[i][j-1].second ,   
                )
                
            比較需要注意的是對於玩家二來說 , 他是相對被動的後選 , 會根據玩家一到底拿了左邊的石頭還是右邊的石頭而定 
            假如玩家一選擇了 nums[i] + dp[i+1][j].second 這條路線 , 那玩家二實際上就是走  dp[i+1][j].first 
            
        
        --> 這一題蠻有代表性的也容易思考 , 狀態轉移的思考框架是 , 我做為玩家一拿走左邊的第一塊石頭 , 
            實際上就相當於在剩下遊戲中的後手 + 剛剛拿的第一塊石頭的總分
        
        
"""

from typing import List 
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        
        size = len(piles)
        dp = [ [  None for i in range(size)  ] for j in range(size) ]
        
        # 對角線上的元素就是只有先手拿分
        for i in range(size): 
            dp[i][i] = ( piles[i] , 0 )

        # DP 遞迴推進 , 這一題需要走斜向或著由底往上 , 我走斜向
        
        for idx1 in range(1 , size): 
            
            for idx2 in range( size - idx1  ): 
                
                i = idx2 
                j = idx1 + idx2 
        
                # 先手玩家跟後手玩家要分開計算, 因為這之間有相依關係 
                # 我們計算先手的玩家選擇左邊和右邊分別可以拿的分數  , 相當於剩下的石堆中後手玩家的最大分數與其選擇的石頭分數
                left = piles[i] + dp[i+1][j][1] 
                right = piles[j] + dp[i][j-1][1]
                
                
                # 如果先手選擇拿左邊 , 後手只能從剩下的右邊那堆去取值 
                if left > right : 
                    
                    dp[i][j] = (left ,  dp[i+1][j][0])
                
                else : 
                    dp[i][j] = (right  ,  dp[i][j-1][0])
            
        
        if dp[0][size-1][0] > dp[0][size-1][1] : return True 
        else : return False                 