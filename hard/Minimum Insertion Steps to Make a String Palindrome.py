""" 
    思路 :  
        此題也為東哥書本上範例題 , 給定一個字串s , 我們可以在任意位置插入任意字元 ,
        求讓該字串s變為回文串的最小動作數
        
        定義DP-talbe 
            這一題難度是hard , 只給了一個字串 -> 所以要馬是
            1. 1D-table dp[i] 表示s[0~i] 要插入的次數
            2. 1D-table dp[i] 表示以i結尾的sub-array的最小插入次數 
            3. 2D-table dp[i][j] 表示字串 s[i:j]的最小插入次數
        由於這一題涉及回文 , 似乎以第三種方法框架較為合理,並且這題基本上不需要空字串在前
        
        狀態轉移方程式 
            
            dp[i][i] = 0 , 因為單一個字母不需要任何操作就是回文,因此這一題也是2D平面上 ,
            要往右上角推進的DP , 答案在dp[0][len(s)-1] , 
            思考要計算 dp[i][j]的時候 , 要如何使用已經有的資訊來求解 
            利用test-case 的 "mbadm" 畫圖出來推導 
            
            -> s[i]=s[j] , 因為兩端已經是回文了不用操作 , 只要在內部的  s[i+1~j-1]操作
            因此此時 dp[i][j] = dp[i+1][j-1] , 為左下 
            
            -> s[i]!=s[j], 則此時可以選擇在左端插值或右端插值 , 以"mbadm"來說不管在哪端插值的次數都一樣
            所以我的推測是此時 dp[i][j] = 1 + min(dp[i+1][j] , dp[i][j-1])  , 左邊或下面
"""

class Solution:

    def minInsertions(self, s: str) -> int:
    
        size = len(s) 
        # base-case 為對角線與左下三角都是0 
        # dp[i][j] 代表 s[i]~s[j] (封閉區間) 的minimum insertion step 
        dp = [[0 for i in range(size) ]for j in range(size)]      
        
        # 這一題也需要走斜向尋訪 
        # 01->12->23 
        # 02->13
        # 03 
        
        for idx1 in range( 1,size   ): 
            
            for idx2 in range(size-idx1 ) : 
                # covert 輔助index回到 i , j 增加可讀性
                i = idx2 
                j = idx1+idx2 
                
                # 如果兩端的字串相同 , 那只要考慮內部的回文次數,即左下角
                if s[i] == s[j] :
                    dp[i][j] = dp[i+1][j-1] 
                
                else : 
                    dp[i][j] = 1 + min(dp[i+1][j] , dp[i][j-1]) 
        
        return dp[0][size-1]