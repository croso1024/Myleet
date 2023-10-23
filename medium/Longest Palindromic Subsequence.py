""" 
    思路: 
        這一題有用JS寫過一次了 , 這一次則是按順序讀到書中這個部份時所寫

        依照東哥的定義 : 
            1. 這一題屬於 -> 2D DP-table + 只有單一字串  
            2. 可以對比Longest common subsequence , 他是 2D table + 雙字串
            3. 而前面LIS : Longest increase subsequence 則是 1D-table + 單array
            
            大致上的Longest subsequence 的問題可以分為這幾種分類
            
            在這一題裡面我們使用的 2D-table 加單字串 , 通常DP會定義為 
            dp[i][j] 為 s[i~j] 的目標值 (此題的LPS) 
            
        對於這一題來說 dp[i][j]的LPS可以有幾種case
        
        1. 如果 s[i]==s[j] , 即 dp[i][j] = 2 + dp[i+1][j-1]  ( 左下 )
        2. 如果 s[i]!=s[j] , 則可以比 max ( dp[i+1][j] , dp[i][j-1] )  (下面或左邊)

        換句話說這一題的推進需要仰賴 左 , 下 , 左下 三個方向 , 而base case可以為我們填滿左下三角+對角線
        
        尋訪的方向為:
        1.斜著走 , 才能確保每一格都有左,下,左下 
        2.走倒數第二列開始走, 這樣也能確保
        
        
"""


""" 
    解法一. 就是按照上面的思路做bottom-up推進 , 使用從底往上的尋訪
"""
class Solution:

    def longestPalindromeSubseq(self, s: str) -> int:
    
        size = len(s)  
        if size == 1 : return 1 
        # dp table的定義是 dp[i][j] 即是 s[i~j] (包含j) 的最大回文長度 
        dp = [[None for i in range(size)] for j in range(size)] 
        
        # 根據上述定義 , 對角線上的最大回文LPS為1 , 左下三角則都是0 
        # 因此先走一個下三角的迴圈 , 對角線的迴圈去填入base case 
        for i in range(1,size):
            for j in range( i ):  
                dp[i][j] = 0 
        
        for i in range(size) : dp[i][i] = 1 
                
                
        # 依據DP狀態轉移方程式 , 我們這邊可以走斜向的推進或由底往上的推進 
        
        # 這邊走由底往上 
        
        for i in range( size-2 , -1 , -1 ): 
            
            for j in range( i+1 , size ): 
                
                if s[i] == s[j] : 

                    dp[i][j] = 2 + dp[i+1][j-1] 

                else : 
                    
                    dp[i][j] = max(dp[i+1][j] , dp[i][j-1]) 
        
        
        return dp[0][size-1] 
    
    
"""
    解法二 . 針對解法一做一點優化 , 主要是優化best case生成 , 然後改為斜向尋訪
"""

class Solution:

    def longestPalindromeSubseq(self, s: str) -> int:
    
        size = len(s)  
        if size == 1 : return 1 
        # dp table的定義是 dp[i][j] 即是 s[i~j] (包含j) 的最大回文長度 
        dp = [[0 for i in range(size)] for j in range(size)] 
        
        
        for i in range(size) : dp[i][i] = 1 
                
        
        # 斜向尋訪 
        
        # 01 -> 12 -> 23 -> 34
        # 02 -> 13 -> 24 
        # 03 -> 14 
        # 04 
        
        for i in range(1,size):
            
            for j in range( 0 , size-i ) : 
                
                if s[j] == s[j+i] : 
                
                    dp[j][j+i] = 2 + dp[j+1][j+i-1] 
                    
                else : 
                    dp[j][j+i] = max( dp[j+1][j+i] , dp[j][j+i-1]  )
        
        return dp[0][size-1] 
    