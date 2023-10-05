""" 
    思路 : 
        這一題看起來很類似換硬幣 , 但我們可以用的完全平方數是無限多個的 
        ->  但另一方面題目給定的可用數字也不像硬幣那一題是unorder的 ,
            因此一旦某個平方數大於目前可得
            我們就完全能夠直接捨棄繼續展開
            
        這一題就使用遞推,以dp[i]代表最少個完全平方數湊到i的結果
        
        狀態轉移方程式 : 
            dp[i] = min(  
                    1 + dp[i-1] 
                    1 + dp[i-4]
                    1 + dp[i-9] 
                    ... 
                    )
"""


""" 
    解法一 . 
        DP遞推 , 外層loop推state , 內層依照可用的動作分支展開 , 這一題的狀態轉移方程式清晰明瞭
        但直接sumbit會因為速度不夠被擋住 , 需要優化
"""
class Solution:
    
    def numSquares(self, n: int) -> int:
        
        dp = [float("inf")] * (n+1) 
        dp[0] = 0 
        dp[1] = 1 
        
        # 外層的loop推進state , 也就是要湊的數值 
        for i in range(2,n+1) : 

            # 內圈列出了所有可以做的動作分支
            for j in range(1,100) : 
                
                # 如果要湊的數字比起平方數還小就可以直接跳出了
                if i - pow(j,2) < 0 : break 
                
                dp[i] = min(dp[i] , 1+dp[i-pow(j,2)])

        
        # 返回題目所要湊出的數字所需要的最小平方數數量。
        return dp[n] 
            
C = Solution() 
print(C.numSquares(n=6405) )
             
""" 
    解法二. 
        前一個解法會慢的一個原因我認為還是在內迴圈 , 雖然有break的機制 ,
        但當n很大的時候 , 內迴圈for-loop的時間太久了 , 這邊透過根號+floor來定義可行的動作範圍 
        總共做了兩點優化
        - 1. 根號+floor來定義可行動作範圍
        - 2. 將所有可行動作的集合透過list comprehensive統合再取min , 把比較整合成一次  
        
    實測來說這個版本大概比第一個解法快一倍 , 通過LC的結果是空間極優 , 時間很慢
"""
from math  import sqrt , floor 

class Solution:
    
    def numSquares(self, n: int) -> int:
        
        dp = [float("inf")] * (n+1) 
        dp[0] = 0 
        dp[1] = 1 
        
        # 外層的loop推進state , 也就是要湊的數值 
        for i in range(2,n+1) : 
            
            # 優化內部迴圈的執行
            dp[i] = min(
                dp[i] , 
                1+ min( [dp[i-j**2]  for j in range(1,floor(sqrt(i)) + 1 ) ]       )
            )

        
        # 返回題目所要湊出的數字所需要的最小平方數數量。
        return dp[n] 
            

""" 
    解法三 . Top-Down遞迴 + memo     
        遞迴樹的展開的樣子如下 :

                    15 
                  / |  \
               14   11    6
                   ...  
                   
    這個解法純粹讓我練練手 , 此解法的性能和解法一是差不多的
"""
from math import floor , sqrt 
class Solution:
    
    def numSquares(self, n: int) -> int:
        
        self.memo = [None] * (n+1)
        self.memo[1] = 1 
        
        
        # 使用遞迴加上備忘錄來求解 
        def recursion(n) : 
            # base case , 如果n小於0就不用回傳了 , 但應該不會遇到這個情況在我們有floor(sqrt())時
            if n<0 : return float("inf")
            elif n == 0 : return 0
            
            # 如果目標已經存在memo裡面 , 那就可以直接返回了
            if self.memo[n] : return self.memo[n]
            else : 
                
                self.memo[n] = min(
                    [ 1+recursion(n-i**2) for i in range(1 , 1 + floor(sqrt(n)) )    ]
                )
                        
            return self.memo[n]                
        
        return recursion(n)