
""" 
    思路 :  
        這一題是書本上背包問題的延伸範例 , 我一開始直覺上會認為這一題是因為要做"選擇" 
        選擇是否要把nums[i]放入另一個set , 然後算是類似backtrack去展開( 展開到底有滿足的解就直接return )
        
        但實際上東哥解這題的思路很特殊 , 首先計算nums的總和sum , 把問題轉換成
        -> 能否從nums中取出一些物品 , 剛好填滿 sum//2 ? 

"""
from typing import List 

""" 
    解法一. 使用我原先backtrack的想法去處理 ,
            方法論是OK , 但會出現時間太慢的問題
"""

class Solution:

    def canPartition(self, nums: List[int]) -> bool:
        
        sol = False        
        # 定義backtrack函數 , action代表剩餘可選的動作 , 而set1 , set2則代表兩個set目前的總和 
        # 在action的部份我們透過從後面往前選 , 比較滿足python list的性質 
        def backtrack(actions , set1 , set2):
            nonlocal sol
            # terminate case 
            if len(actions) == 0  or sol: 
                print(set1 , set2)
                if set1 == set2 : 
                    sol = True 
                return 
            
            # 把該數值加入set1 
            backtrack( actions[1:] , set1+actions[0] , set2  )
            # 把該數值加入set2
            backtrack( actions[1:] , set1, set2 + actions[0]   )
    
        backtrack(nums , 0 , 0 ) 
        return sol 
                            

""" 
    解法二. 
        依照東哥所謂的 , 找到能不能有集合大小為 sum//2 來填滿背包這個思路進行 
        並套用背包問題一貫的2D dp 框架 
        
        標準背包問題的 dp[i][j]為在擁有前 i 個可用物品的情況下 , 背包重量為 j 可以裝進的最大總數 
        
        稍微修改一下作為這一題的DP定義 : dp[i][j] 代表在有前i個問題下 , 背包重量為j的情況下是不是能夠剛好裝滿
        而我們要找的答案就在 dp[len(nums)-1][sum//2]  , 即在有所有物品的情況下是不是有辦法剛好裝滿背包
        
        依照這個思路去想狀態轉移方程式和base case 
        
        dp[0][0] = True 
        dp[1:][0] = True 
        dp[0][1:] = False , 背包都無法裝滿 
        
        考慮第i件物品在內的情況 , 就是在沒有i的時候 , 是否可以只用 j-nums[i] 的容量來裝滿
        
        # 關鍵思路 ----- 
        
        狀態轉移函數的 dp[i][j] 等於True的情況有兩種 
        1. 把新的物品放進來 , 即 dp[i-1][j - 新物品重] 為True  ,那樣可以剛好放滿
        2. 不考慮放新的物品 , 即 dp[i-1][j] 為True , 那我可以將這個物品納入考量 , 但不選擇放進,同樣滿足定義
        3. 如果新的物品重量大於背包剩餘重量 : j - 新物品重 < 0 , 則dp[i][j] = dp[i-1][j]
        
        我在自己寫的時候忽略了第二點 , 和第三點 , 尤其是第三點
        
        雖然我在初始化的時候將所有值都初始為False ,但沒有考慮到假設 dp[i-1][j]是可以剛好放滿
        而又來了一個新的更重的物品 ,可以選擇不要放 , 仍然dp[i][j]為True 的情況
        

"""
import numpy as np 
class Solution:

    def canPartition(self, nums: List[int]) -> bool:
        
        sum = 0 
        
        for i in nums : sum+=i 
        
        if sum%2 != 0 : return False 
        
        # 依照定義建立 DP-table :  n個物品 x 容量 , 有做額外的+1 
        dp = [[ False for i in range( sum//2 + 1 ) ] for j in range(len(nums)+1)] 
        
        # 沒有容量的話都算是裝滿 , 沒有物品的話就是裝不滿 , 但在初始化的時候都填False了
        for i in range(len(nums)+1): dp[i][0] = True 
        
        # 外層堆進狀態一 : 物品數量 , 由0件到n件
        for i in range(1 , len(nums)+1): 
            
            # 內層堆進狀態二 : 重量 , 從0到sum//2 + 1 
            for j in range( (sum//2) + 1 ): 
                
                # 注意nums需要給一個index offset來配合DP-table 
                # 這邊保護 index out of range的情況
                if j - nums[i-1] < 0 : 
                    dp[i][j] = dp[i-1][j]
                    continue

                # 可以把第i件物品放進來 , 或著選擇不放 , 繼承先前的結果
                if dp[i-1][ j - nums[i-1] ] or dp[i-1][j] : 
                    dp[i][j] = True 
                else : 
                    dp[i][j] = False  
        # print(np.array(dp))
        return dp[len(nums)][sum//2]
                
