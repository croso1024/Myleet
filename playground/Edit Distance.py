
""" 
    
    dp[i][j] : 考慮 word1[0:i+1] 和 word2[0:j+1] 的部份納入考慮的Edit Distance 
    #這一題要加入空字串進去 , 故DP-table size :   1+len(word1)  x 1 + len(word2)

    # base case : 空字串配對 word1 , word2 的時候  
    
        ""  "h"  "o"   "r"  "s"  "e" 
    ""   0   1    2     3    4    5 
    "r"  1   1    2     2    3    4
    "o"  2   2    1     2    3    4
    "s"  3   3    2     2    2    3
    
    # 計算 dp[i][j]時 , 要比較  word1[i] , word2[j] 是否為相等 , 如果相等 , 他們可以等於左上角的dp[i-1][j-1] , 
    # 代表兩個字串各自增加一個字不需要額外修改 
    
    # 但如果不相等 , 就要看 dp[i-1][j] (word2少個字母) 和 dp[i][j-1] ( word1少個字母 )  , dp[i-1][j-1] ( 各少一個字母 )
    # 三個中選最小值 + 1 
    
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        #   size為  |word2| x |word1|
        dp =[ [ None for i in range(len(word1)+1) ] for j in range(len(word2) +1) ]

        # 放進base case 
        for i in range(len(word1)+1) : dp[0][i] = i 
        for i in range(len(word2)+1) : dp[i][0] = i 
        
        # 推進DP-state 
        for i in range(1, len(word2)+1 ) : 
            
            for j in range( 1, len(word1) +1): 
                
                if word2[i-1] == word1[j-1] : 
                    
                    dp[i][j] = dp[i-1][j-1]
                
                else : 
                    
                    dp[i][j] = 1 + min(
                        dp[i-1][j-1] , 
                        dp[i][j-1] , 
                        dp[i-1][j]
                    )
        
        
        return dp[ len(word2) ][ len(word1) ]