""" 
    思路: 
        給定兩種形狀的的骨牌 , 求要拼出 2xn的形狀可以有幾種不同的方式 , 
        這一題我覺得比較像是找規律 , 透過test_case把 n=1,2,3,4,5,6,7的答案秀出來後可以找到某些規律 
        n=1 -> 1 
        n=2 -> 2
        n=3 -> 5
        n=4 -> 11
        n=5 -> 24
        n=6 -> 53
        n=7 -> 117

        從這邊可以看到,以n=1,n=2,n=3作為basecase ,令 f(n)代表n=n時可以的方式數
        
        f(n) = 2f(n-1) + f(n-3)  , n>3 
        
        這邊來解釋, 假設 n=5 , 就等於 n=4的排法乘上2 , 加上n=2的排法數量
        
        
    
"""
class Solution:
    def numTilings(self, n: int) -> int:
        
        if n==1 : return 1 
        elif n==2: return 2
        elif n==3 : return 5
        
        dp = [0 for i in range(n+1)] 
        
        
        dp[1] = 1 
        dp[2] = 2 
        dp[3] = 5 
        
        for i in range(4,n+1): 
            dp[i] = 2*dp[i-1] + dp[i-3] 
        return dp[n] % (pow(10,9)+7)