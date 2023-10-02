from typing import List 


""" 
    解法一 . Top Down 遞迴 
    此問題具備最佳子結構 , 即子問題之間相互獨立 , 另外就是透過for迴圈展開traverse 
    透過拆解問題的方式 , 使用子問題的解答來求解原始問題。 
    
    每一個recursion(n)都是要計算子問題的答案，並回傳兌換其需要最少的硬幣數，
    透過一個best用來紀錄, for coin in coins來展開所有分支。  
    如果n<0就代表該分支無解必須跳過。
    
    --> 雖然空間應該很優,但速度太慢導致 Exceed Time Limit
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # n 為要湊出的零錢數
        def recursion(n) : 
            
            # 如果n==0的話就剛好湊滿，不用其他硬幣了 
            if n==0: return 0 
            # 如果n<0 代表這個分支是無解的
            elif n<0 : return -1
            
            # 使用best紀錄，要兌換n的話需要的最少硬幣數量 , 也作為要返回的子問題答案
            best  = float('inf')        
                
            for coin in coins : 
                # 往下展開子問題分支
                subproblem = recursion( n - coin ) 
                # 如果該分支最終無解就跳過 ( 等到執行到此,就是已經展開回來了)
                if subproblem == -1 : continue 
                # 該分支有解，比較現有最少兌換數量 
                best = min(best , 1 + subproblem)
            
            # 回傳最少的兌換數量，如果所有分支都無解就回傳1
            return best if not best == float("inf") else -1 
                    
        return   recursion(amount) 
        


""" 
    解法二. 帶有memo的Top down遞迴 , 運用類似的概念,但在遞迴過程中
    使用一個dict or array來保存已經求解的子問題 , 我這邊實做使用array保存。 
    
    --> 可以過LeetCode檢查 , 但time/space都不太好
"""
class Solution1:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # 使用None代表還沒有求解 , -1代表該子問題無解
        self.dp = [None] * (amount+1) 
        self.dp[0] = 0 
        
        def recursion(n) : 
            # 如果子問題是已經解過( 可能有解也可能無解(-1) )，就直接使用         
            if n<0 : return -1 
            if not self.dp[n] is None : return self.dp[n]
            
            
            best = float('inf')
            
            for coin in coins : 
                
                subproblem = recursion( n - coin )
                # 子問題無解，跳過 
                if subproblem == -1 : continue 
                # 子問題有解，比較最好的結果 
                best = min(best , 1 + subproblem) 
                
            #走完迴圈，已經知道兌換 n 個硬幣的最佳解或是無解 , 紀錄到備忘錄 
            self.dp[n] = best if not best == float('inf') else -1 

            return self.dp[n]
        

        return recursion(amount)
    


""" 
    解法三 . Bottom up 的DP-table 
    這邊一樣使用array存子問題的最佳解,dp[i]表示要兌換i元的最佳解
"""
class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        self.dp = [None] * (amount+1) 
        self.dp[0] = 0     
        
        # Bottom up , 遞推到目標值amount , 並一路填充self.dp內容
        for i in range(1 , amount+1):  
            
            best = float("inf")
            for coin in coins : 
                # 無解 ( 包含減完後小於0 , 或著dp表中對應i-coin是無解 )
                if i - coin < 0  or  self.dp[i-coin] == None : continue    
                best = min(best , 1+self.dp[i-coin])
            self.dp[i] = best if not best == float("inf") else None 
        
        return self.dp[amount] if not self.dp[amount] == None else -1 


""" 
    優化一下解法三 
"""
class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        self.dp = [float("inf")] * (amount+1) 
        self.dp[0] = 0     
        
        # Bottom up , 遞推到目標值amount , 並一路填充self.dp內容
        for i in range(1 , amount+1):  
            
            for coin in coins : 
                # 無解 ( 包含減完後小於0 , 或著dp表中對應i-coin是無解 )
                if i - coin < 0 : continue 
                self.dp[i] = min(self.dp[i] , 1 + self.dp[i-coin])
        
        return self.dp[i] if not  self.dp[i] == float('inf') else -1 

C = Solution2() 
print(C.coinChange([1,2,5],11))
# print(C.coinChange([2147483647] ,2))
            
