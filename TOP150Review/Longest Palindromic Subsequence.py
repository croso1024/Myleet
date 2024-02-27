class Solution:
    
    # dp solution 
    # define dp-table dp[i][j] :  longest PS in s[i:j+1] 
    """ 
        base case :
        dp[i][i] = 1  , dp[i][j] = 0 if i>j
    
        state transition : 
        
        if s[i] == s[j] : 
            dp[i][j] == 2 + dp[i+1][j-1] 
        else : 
            dp[i][j] ==  max(dp[i][j-1] , dp[i+1][j] ) 
        
    """
    def longestPalindromeSubseq(self, s: str) -> int:
        
        size = len(s) 
        
        dp =   [ [0 for i in range(size)] for j in range(size) ] 
        
        # base case : 
        for i in range(size) : dp[i][i] = 1 
        
        
        # dynamic programming  # 這一題需要斜向推進 
        # 01 -> 12 -> 23 
        # 02 -> 13 
        # 03 
        for idx in range( 1 , size  ):  # 1,  2  ,3 
            for jdx in range( size - idx  ): # (0,1,2)  ,  ( 0,1) , (0)
                
                i = jdx  
                j = idx + jdx  
                
                if s[i] == s[j] : 
                    dp[i][j] = 2 + dp[i+1][j-1]  
                    
                else : 
                    dp[i][j] = max(
                        dp[i][j-1] , dp[i+1][j]
                    )                
        
        return dp[0][size-1]
        