
# 擴散法: 
# take O(N^2)
class Solution:

    def longestPalindrome(self, s: str) -> str:
        
        
        probe = 0 
        size = len(s) 
        best = float("-inf") 
        best_sol = None 
        
        # 一個一個char作為中心 , 向左右擴散找回文串
        while probe < size: 
            
            
            # 如果回文串為奇數長度: 
            i = 1
            temp = 1  
            while   ( probe-i >= 0 and probe+i < size ) and s[probe-i] == s[probe+i] : 
                temp += 2 
                i += 1 
            
            if temp > best : 
                best = temp  
                best_sol = (  probe-i+1 , probe+i-1   )
            
            # 如果回文串是偶數長度 
            if probe+1 < size and s[probe] == s[probe+1] : 
                temp = 2
                i = 1 
                
                while (probe-i >=0 and probe+1+i < size ) and s[probe-i] == s[probe+1+i] : 
                    temp += 2
                    i += 1 
            
            if temp > best : 
                best = temp 
                best_sol = ( probe-i+1  , probe+i )
            
            probe += 1
            
        return s[best_sol[0] : best_sol[1]+1]
                
        

# DP solution 

class Solution:

    def longestPalindrome(self, s: str) -> str:
        
        # let dp[i][j] = longest palindromic substring start at i , end at j 
        # basecase dp[i][i] = s[i] 
        """ 
            state transiton : 
            
            if s[i] == s[j] : 
                dp[i][j] ==  2 + dp[i+1][j-1] 
            else : 
                
                dp[i][j] = max( dp[i+1][j] , dp[i][j-1] )
            
        """