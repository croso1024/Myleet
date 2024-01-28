""" 
    思路 :
    
        這一題直接參考了東哥對於這類兩人輪流選擇遊戲問題的框架 , 這個套路應該是比較通用的可以直接記憶下來 
        即令 dp[i][j] = (first , second)  , 表示在可以用的資源在 [i,j] 這個範圍內時 , 先手玩家與後手玩家可以得到的最高分數 
        
        這一點是利用到了，這類選擇遊戲通常是"輪流進行" ，前一輪的後手會在下一輪變為先手。 這個循環會每兩回合輪替一次
        換句話說要知道原始問題誰能勝利 , 可以看縮小兩輪後的狀態
        
        以這一題玩選數字為例 , 初始狀態為 [1,5,2] ,兩人輪流從兩側選擇 , 並計算累積分數多者勝利 
        
        Base case :
            依照我們剛剛對DP的定義 dp[i][i] = ( 有分數 , 0 ) , 因此只有一個選擇的時候也只有先手能拿分 
        
        我們的目標是計算遊戲結束(所有數字都被選完後)，誰的分數比較高 , 換句話說要求dp[0][last] , 右上角
        
        狀態轉移函數的定義就需要稍微思考一下 : 

        ---第一個想法 , 就是兩輪前的結果

        
        dp[i][j] = (  dp[i+1][j-1].first + nums[i] 或nums[j]中大的  , dp[i+1][j-1].second + nums[i] 或nums[j]中小的 )
        
        --- 第二個想法 , 更加周全一點
        
        dp[i][j].first = max(
            dp[i+1][j].second + nums[i] , 
            dp[i][j-1].second + nums[j] , 
            dp[i+1][j-1].first + nums[i] , nums[j]中大的
        )
        
        -> 實做過程其實可以發現根本不需要左下 , 一定是挑少一顆的情況 ,因為左下的情況應該會包含在左邊和下面 
        尤其這一題需要考量的兩邊都會最佳化 , 先手選擇完後後手只能拿特定的部份 , 同時使用到這類遊戲輪流的機制 
        
        這一題的狀態轉移確實有點特別之處。
        
        
"""

from typing import List 
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        # 左邊下三角區域 , 初始化為None
        dp =[ [None for i in range(len(nums))] for j in range(len(nums)) ]  
        
        # 對角區域 , 一定是先手玩家拿到分數而已 
        for i in range(len(nums)): dp[i][i] = (  nums[i] , 0  ) 
            
        
        # 依照我們的狀態轉移函數 , dp[i][j]的更新是仰賴 左邊/下面/左下 , 因此這一題又是典型的斜向traverse
        for idx1 in range( 1 , len(nums)) :
            
            for idx2 in range( len(nums)-idx1 ) : 
                
                i = idx2 
                j = idx1+idx2
                
                # 原本的寫法 - 沒有考慮到兩人會思考 -> 這個寫法就是一昧的選當前最大沒有戰略
                
                # dp[i][j] = (
                #     # first 部份
                #     max( dp[i+1][j][1] + nums[i]  , dp[i][j-1][1] + nums[j] ) , 
                #     # second部份
                #     max( dp[i+1][j][0] + nums[i]  , dp[i][j-1][0] + nums[j] ) ,
                # )
                
                # 先手的人可以選擇這兩個動作 , 取得相應的分數 , 而後手則只能被動選擇了 
                left = dp[i+1][j][1] + nums[i] 
                right = dp[i][j-1][1] + nums[j] 
                
                # 後手被動選擇的過程不是拿走剩下那堆 , 是要考慮沒有那塊被拿走得情況下 first可以得到的最高分
                if left >= right  : 
                    dp[i][j] = ( left , dp[i+1][j][0] ) 
                else : 
                    dp[i][j] = ( right , dp[i][j-1][0] )
                
        first_score , second_score = dp[0][len(nums)-1]
        
        if first_score >= second_score : return True
        else: return False 

test_case = [1,2,99]
S = Solution() 
print(S.predictTheWinner(test_case))
        
        