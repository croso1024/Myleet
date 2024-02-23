""" 
    題意:   
        給定4個整數 zero , one , low , high , 
        接下來從一個空字串開始, 在每一回合 , 我們都可以做以下幾件事情:
        - 在空字串append '0' zero 次
        - 在空字串append '1' one 次
        以上的動作可以分別執行無限次 
        
        而一個good string , 就是長度介於low-high(inclusive)的字串 .
        題目要問在給定的條件下 , 總共可以湊出多少種不同的good string , 因為答案很大,要mod pow(10,9) + 7
        
    思路:   
        我在想能否想成 , dp[i]紀錄可以湊出的長度為i的種類數 , 而答案就是 sum(dp[low:high+1]) ,
        這樣來想的話 , dp[i] = dp[i-zero] + dp[i-one]
        
        這個情況要處理初始狀態的問題 , 可能zero=1 , one=2 , 那這樣 dp[2] 就會是 2 , 即1+dp[1] , dp[1]=1
        我的辦法就是一個迴圈額外處理那個部份 , 假設zero < one , 那在 zero->one的途中單獨只使用zero來計算這樣 , 實際上這個步驟是可以被優化的
        
"""

""" 
    解法一. 原始概念雛型
"""
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
        dp = [0 for i in range(high+1)] 
        # 空字串
        dp[0] = 1 
        if zero == one : 
            dp[zero] = 2 

        elif zero < one :
            pass 
        else :
            zero , one  = one , zero 
            
            
        dp[zero] = 1 
        for i in range(zero+1 , one): 

            dp[i] = dp[i-zero]  
            
        dp[one] = 1 + dp[one-zero] 
      
        for i in range(one+1 , high+1):  
            
            dp[i] = dp[i-zero] + dp[i-one] 
        
        
        return sum(dp[low:high+1]) % (pow(10,9)+7)


""" 
    解法二. 略為優化,把處理初始狀態的迴圈改為在for-loop內的條件
    
    dp[i]就是湊出長度為i的字串的種類數
"""
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
        dp = [0 for i in range(high+1)] 
        # 空字串
        dp[0] = 1 
        if zero == one : 
            dp[zero] = 2 
        elif zero > one : 
            zero , one = one , zero 
            dp[zero] = 1 
        
        sum = 0 
        for i in range(high+1):
            
            if i < zero : continue 
            
            elif zero <= i < one : 
                
                dp[i] = dp[i-zero] 
            
            else :
                
                dp[i] = dp[i-zero] + dp[i-one]             
            
            if i >= low : 
                sum += dp[i] 
        
        
        return sum % (pow(10,9)+7)

S = Solution()
S.countGoodStrings(3,3,1,2)
      
      
            