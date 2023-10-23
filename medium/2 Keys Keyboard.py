""" 
    思路 : 
        此題是書上四鍵盤問題的另一種版本 , 動作變為只有兩種 , 
        但要做的事情變為至少要幾步可以讓畫面上剛好有n個"A"
    
    這一題在類似的概念(四鍵盤問題)書上說明了對於狀態的不同定義方式與看法會造成DP算法在效率上的巨大差別 

    
    解法1,2,3 . 
        我來嘗試使用Top-down的解法 , 並將狀態定義為 : 1.畫面上A的數量 , 2. 剩餘操作數量 3. 剪貼本上的A數量 
        去列舉所有可能到達 n 個A的方法 
        
        !! 這邊有個很關鍵的部份 , 如果我在初始狀態令step=0 , copy_num=0 ,兩種解法都會自成無限迴圈 ,
        因為一定有一個分支會一直嘗試要去貼上 , 但在C_nums=0時不斷貼上永遠不會觸發中止 
        
        因此改進就是 , 貼上的動作必須要在C_nums != 0 , 而複製的動作則要在上一個動作不是複製才能用


    解法三. 則改以Bottom-up的遞推 , 定義狀態轉移函式
    
        --> 這題看起來沒有明確的最佳子解構 , 湊集5個"A"的最小步數和湊齊6個沒有明確關係(且剪貼簿裡面的狀態也沒有考慮到)
        需要換一個角度思考 , 可以去計算每一步能到達的最大A數 , 那答案會在那個可以超過目標n的值? 
        
        令dp[i] = i步情況下可以到達的最大A數
        
        
    
"""

""" 
    解法一. Top-down 遞迴 , 
        這邊是參考了東哥版本 , 把"複製和貼上綁定在一起的方式" , 否則如果單獨開放只有複製
        就會造成無限遞迴 
"""

class Solution:
    
    def minSteps(self, n: int) -> int:
        
        if n == 1 : return 0
        best = float("inf")
        
        def dp(step,A_nums , C_nums):
            nonlocal best
            if A_nums == n : 
                best = min(best , step) 
                
            elif A_nums > n : return 
            
            else : 
                # 我們要禁止不斷的做複製 , 其辦法就是複製後一定要接貼上 
                dp( step+2 , A_nums+A_nums , A_nums) 
                
                # 也可以繼續只做貼上
                dp(step+1 , A_nums+C_nums , C_nums) 
                
        
        dp(1, 1 , 1)
        return best 

        
""" 
    解法二. 同樣是Top-down 遞迴 , 
        但我這邊嘗試自己加入變數c (前一run是否有用過複製) 來限制動作  ,
        為了解決無限遞迴 , 關鍵在於要把C_nums!=0的情況禁止貼上
    
"""

class Solution:
    
    def minSteps(self, n: int) -> int:
        
        best = float("inf")
        
        def dp(step,A_nums , C_nums,c):
            nonlocal best
            if A_nums == n : 
                best = min(best , step) 
                
            elif A_nums > n : return 
            
            else : 
                if not c :
                    dp( step+1 , A_nums , A_nums,True) 
                
                if C_nums!=0 :
                    dp(step+1 , A_nums+C_nums , C_nums,False) 
                
        
        dp(0 , 1 , 0 , False)
        return best 
    
""" 
    解法三 : 再次微調 Top-down ,不使用外部變數保存了 , 但沒有比較好的Time/Space
"""
class Solution:
    
    def minSteps(self, n: int) -> int:
        
        if n == 1 : return 0
        def dp(step,A_nums , C_nums):
            if A_nums == n : 
                return step 
            
            # 步數最多也就複製一次然後一直貼 
            elif A_nums > n : return n
    
            return min(
                
                dp(step+2 , A_nums+A_nums , A_nums) , 
                dp(step+1 , A_nums+C_nums , C_nums) ,
                
            )
        
        return dp(1 , 1 , 1)

""" 
    解法四. 帶memo的top-down遞迴 , 但效果也不是很好
"""
class Solution:
    
    def minSteps(self, n: int) -> int:

        memo = dict()

        if n == 1 : return 0
        def dp(step,A_nums , C_nums):
            if A_nums == n : 
                memo[(A_nums,C_nums)] = step 
                return step 
            
            # 步數最多也就複製一次然後一直貼 
            elif A_nums > n : return n
    
            elif (A_nums,C_nums) in memo : return step

            return min(
                
                dp(step+2 , A_nums+A_nums , A_nums) , 
                dp(step+1 , A_nums+C_nums , C_nums) ,
                
            )
        
        return dp(1 , 1 , 1)



""" 
    解法五 . Bottom up遞推

        這一題使用遞推的想法比較特殊 , 我也是回家路上才想到 ,
        令 dp[i]代表湊集i個"A"在畫面上需要的最小次數 ( 也可以當作i個"A"在畫面上以及剪貼簿的最小次數 , 只要加offset)

        這樣, 假設要湊到 4個"A" , 可能的作法就是在只有一個"A"的時候再貼上三次 , 或是兩個"A"時貼上一次 ,
        同樣的道理 , 要湊集 i 個 "A" , 可以檢查 1~(i-1) 的迴圈去找i%j == 0 
        
        如此一來  dp[i] =  dp[j] + ((i//j)-1)   +  1   
        -> 湊到 j 個"A"的最小步數 + 按複製 + 貼上  (i//j)-1 次 (因為dp[j]個操作後畫面上已經有j個"A")

"""

class Solution:
    

    def minSteps(self, n: int) -> int:
        
        dp = [float("inf")] * (n+1)                 
        # base case , dp[1] 為0 ,一開始就在畫面上
        dp[1] = 0 
        
        
        # 外層推進狀態 
        
        for i in range(2,n+1): 
            
            for j in range( 1,i ) : 
                
                if i%j == 0 : 
                    
                    dp[i] = min(dp[i] , ((i//j)-1) + dp[j]  + 1    )
        
        
        return dp[n]
        
        
        
        
C = Solution()
C.minSteps(n=10)


class Solution:
    
    def minSteps(self, n: int) -> int:

        memo = dict()

        if n == 1 : return 0
        def dp(step,A_nums , C_nums):
            if A_nums == n : 
                memo[(A_nums,C_nums)] = step 
                return step 
            
            # 步數最多也就複製一次然後一直貼 
            elif A_nums > n : return n
    
            elif (A_nums,C_nums) in memo : return step

            return min(
                
                dp(step+2 , A_nums+A_nums , A_nums) , 
                dp(step+1 , A_nums+C_nums , C_nums) ,
                
            )
        
        return dp(1 , 1 , 1)

