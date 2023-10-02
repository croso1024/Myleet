""" 
    思路: 
        這一題的關鍵在於狀態轉移方程式如何定義,因為最佳子結構以及重疊子問題在這一題當中比較明顯。
        給定
            Case1. n=2 1+1 , 1*1 
            Case2. n=3 1+2 , 1+1+1 , 2+1  ,
            Case3. n=4 1+3 , 2+2 , 3+1  , 1+1+2 , 1+2+1 , 1+1+1+1 
            
            可以看到一個規律 , 
            - 如果拆成兩個 , 那n=i時必然時拆 i-j , j  , 因此所有 (i-j)*j都要考慮(列舉出來) 
            - 如果拆到大於兩個 , 那結果就會是 i-j , 構成j的組合 , 即(i-j) * ( n=j 時的最大乘積 )
            我們在遞推的過程中需要考慮到這些Case來求取最大
            
            note: 我們需要在max()中也加入dp[i] , 以免後續尋找的過程把先前最大的刷掉，
                  因此我們要馬在初始化的時候把dp table用數字來初始化 , 要馬就是加入dp[i] is None的判斷
            
"""

# 用判斷dp[i] is None的 比較慢
class Solution:

    def integerBreak(self, n: int) -> int:
        
        if n == 2: return 1 
        
        # create dp table , dp[i] means if n = i , maximum production 
        dp = [None] * (n+1) 
        dp[2] = 1  
        
        # recursion from 3 to n 
        for i in range(3 , n+1): 
            
            for j in range( 2 , i ):  
                if not dp[i] : 
                    dp[i] = max( (i-j)*j  , (i-j)*dp[j] ) 
                else : 
                    dp[i] = max(dp[i] , (i-j)*j  , (i-j)*dp[j] )
    
        return dp[n]


# 使用數字來初始化dp-table 快上不少
class Solution:

    def integerBreak(self, n: int) -> int:
        
        if n == 2: return 1 
        
        # create dp table , dp[i] means if n = i , maximum production 
        dp = [float("-inf")] * (n+1) 
        dp[2] = 1  
        
        # recursion from 3 to n 
        for i in range(3 , n+1): 
            
            for j in range( 2 , i ):  
                dp[i] = max(dp[i] , (i-j)*j  , (i-j)*dp[j] )
    
        return dp[n]
C = Solution()
print(C.integerBreak(10) )