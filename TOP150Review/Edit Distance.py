# DP solution
class Solution:
    
    def minDistance(self, word1: str, word2: str) -> int:
        
        # dp table :  word1.length+1 x word2.length+1
        dp =  [ [ None for i in range(len(word1)+1)  ] for j in range(len(word2)+1)  ]
        
        # base case : dp[0][i] = i  , dp[i][0] = i 
        
        for i in range(len(word1)+1):   dp[0][i] = i 
        for j in range(len(word2)+1):   dp[j][0] = j 
        
        
        for i in range(1 , len(word2)+1) : 
            
            for j in range(1,len(word1)+1) :  
                
                
                if word1[j-1] == word2[i-1] : 
                    dp[i][j] = dp[i-1][j-1] 
                
                else : 
                    
                    dp[i][j] = 1+ min(
                        
                        dp[i-1][j] , # 上
                        dp[i][j-1] , # 左 
                        dp[i-1][j-1] , # 左上
                    )
        
        return dp[len(word2)][len(word1)]
            
        
        