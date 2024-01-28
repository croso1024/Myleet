""" 
    思路 : 

        解法一. backtrack
        這一題看起來可以嘗試使用backtrack去展開 , 因為nums.length <= 20 不算大 , 且每一輪的分支只有2
        因為可以+和- , 所以也無法在中途大於sum就直接跳掉 , 必須要展開到底 

        

"""


""" 
    解法一. backtrack 
        動作就是nums array , 我們傳入一個累計數值表示當前expression的計算結果 , 
        並且在nums-array ( action) 為空時去判斷當前的expression是否等於target , 透過外部變數累計總共有幾種方法  
        
        以這一題來說這個解法是OK的 , 但速度不夠快, 會是 2^n 時間複雜度 , 無法通過測試資料
"""

from typing import List 

class Solution:

    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        sol = 0 
        
        
        def backtrack(  resNumber , expression_sum ):
            nonlocal sol 
            # 如果已經用完所有數字 , 檢查表達式的結果
            if not resNumber : 
                if expression_sum == target : 
                    sol += 1 
                return         
            
            # 每一個節點都只有兩個分支 , 要馬是做加 , 或著做減 
            backtrack(  resNumber[1:] ,  expression_sum + resNumber[0] )            
            backtrack(  resNumber[1:] ,  expression_sum - resNumber[0] )            

        backtrack(nums , 0)

        return sol 

""" 
    解法二. 
    
        往DP去思考 ,先想到top-down遞迴+memo的手段 , 
        
        dp(i,j ,tar) : 代表在使用 nums array [i , j] 的範圍 , 組合出tar的方法數有多少 , 
        
        狀態轉移方程式 : 
            dp(i,j,tar) = dp(i , j-1 , tar - nums[j] ) + dp(i , j-1 , tar+nums[j] )

        需要特別注意 , 在base case 也就是 dp(i,j,tar) , i==j 時 
        我原先是寫  if tar == nums[i] or -1*nums[i] 就可以回傳-1 , 但實際上也有情況是 nums[i] == 0
        , tar同時等於兩種 , 這時候其實就是兩種方法

"""

class Solution:

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        
        memo = dict() 
        
        # 用閉區間 [i,j] , 當 i>j表示區間為空 
        def dp(i,j,tar): 
            
            # base case , 當只剩下一個元素 , 並且該元素正或負等於tar 
            if i==j : 
                sol = 0
                if tar == nums[i] :sol += 1 
                if tar == -1 * nums[i] : sol += 1 
                return sol 
            
            elif (i,j,tar) in memo : 
                return memo[(i,j,tar)] 
            
            else : 
                
                result = dp(i,j-1 , tar+nums[j]) + dp(i,j-1 , tar-nums[j])  
                
                memo[(i,j,tar)] = result 
                
                return result 
        
        return dp(0 , len(nums)-1  , target)