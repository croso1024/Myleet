from typing import List 
""" 
    題意 :  
        給定一組interger array nums , 需要透過以下的操作去最大化得到的分數
        - 從nums中選擇一個數值獲得他的分數,接著刪除掉該分數+-1的所有值 
        這個action可以重複執行不限制次數 .
        要求可以得到的最大分數 , ex. nums=[3,4,2] , 可以得到最大分數為6分
    
    思路 : 
        對於這一題的處理方式,如果暴力展開,則每一個nums[i]都有選擇與不選兩種 , worse case來說可能是 2^n複雜度 
        因此想到使用DP , 去思考如果array很小的時候怎麼解 , 以及如何用小array的結果去判斷大array的結果
        
        ---  失敗的解法 ---
        我們先對nums進行sort , 接下來dp[i]的定義是 0-i這一段可以得到的最大分數值 
        dp[i] 的狀態轉移如下 : 
            在計算dp[i]的時候 , 從0開始traverse , 只要 nums[j] != nums[i] - 1 (我們sort過了)  
            就可以更新當前的最大分數值為dp[j] + nums[i] 
            
        實做上一個版本有問題後的另一個想法 , dp[i]分別紀錄選擇了nums[i]與不選擇nums[i]的最大分數值
        -------------------
        
"""


""" 
    解法一. 
        實際上這不是最一開始的實做了 , 我發現上述的概念可能會因為nums裡面重複的部份而出問題,
        因此下面的實做我先將選了nums[i]能夠得到的實際分數(也就是nums內該數值 x 該數值的出現次數)都放入table
        因為當我們能夠選nums[i] , 代表所有與nums[i]值相同的也都能選 .
        
        整理入table後就可以follow原先的想法 , 雙迴圈去回頭看先前整理過的值來更新解
        但這個解用到了雙迴圈 , 整體複雜度為O(N^2) ,雖然能過測資但時間很差 ,而空間的表現則較好一點 ,
        
"""


class Solution:
    
    def deleteAndEarn(self, nums: List[int]) -> int:

        table = {} 
        for num in nums : 
            if num in table : table[num] += num 
            else : table[num] = num 
        
        keys= sorted(table.keys()) 

        dp = [float("-inf") for i in range(len(keys))]
        dp[0] = table[keys[0]] 
        
        for i in range(1 , len(keys)): 
            
            for j in range(i) : 
                
                if keys[j] == keys[i] - 1 : 
                    dp[i] = max(dp[i] , dp[j] + table[keys[i]])   
                else : 
                    dp[i] = max(dp[i] , dp[j] , table[keys[i]]) 
        
        return max(dp)
        


""" 
    解法二. 
        參考了Solution的解法來進一步優化,我認為的主要優化空間在內部的雙迴圈  , 
        我們可以結合將dp[i]改為存放選與不選來完成 , 因為有了table避免掉了 不選i-1可能i-2也和i一樣的窘境

        計算速度上極大的上升 , 從O(N^2) 變成O(N) , space也變為O(N) worse case 
        空間上略遜於上面的雙loop , 因為我們在dp中額外去保存了拿i與不拿i
"""


class Solution:
    
    def deleteAndEarn(self, nums: List[int]) -> int:

        table = {} 
        for num in nums : 
            if num in table : table[num] += num 
            else : table[num] = num 
        
        keys= sorted(table.keys()) 
        dp = [ [float("-inf"),float("-inf")] for i in range(len(keys))]
        dp[0] = [ table[keys[0]] , 0  ]
                
        for i in range(1 , len(keys)): 
            
            # 如果前一個值和當前+1 , 那我們只能使用不選前一個值的情況來更新 , 或是直接放棄當前值
            if keys[i-1] == keys[i] - 1 :              
                # 如果還是要選當前值 , 就得拿不選上個值的最大分數   
                dp[i][0] = dp[i-1][1] + table[keys[i]] 
                # 也可以不選當前值了 , 拿累積到上個值的最大分數
                dp[i][1] = max( dp[i-1] ) 

            else : 
                dp[i][0]  = max(dp[i-1] ) +  table[keys[i]] 
                dp[i][1]  = max(dp[i-1] )  
        return max(dp[len(keys)-1])

test_case=[2,2,3,3,3,4]
S = Solution()
S.deleteAndEarn(nums=test_case)