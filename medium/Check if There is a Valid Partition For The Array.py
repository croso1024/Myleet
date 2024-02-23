""" 
    題意:
        給定一個array nums , 我們要將該array分塊成一個或多個連續的subarray , 
        而我們稱滿足'valid-partition' , 代表原始array可以被分成多個sub-array後,每個subarray都滿足以下其中一條規則
        -. subarray剛好是兩個一樣的元素
        -. subarray剛好是三個一樣的元素
        -. subarray剛好是3個連續增加的整數 , ex.[3,4,5] 
        題目要我們求給定的原始array是否存在這樣的sub-array 
    
    思路:   
        這一題我認為可以用DP解, 定義dp[i]代表在array[0:i]的情況下是否存在valid partition
        因為要確認valid partition可以用三種方式 
        -> 回顧dp[i-1] , 其無法滿足valid partition且array[i-1] == array[i] 
        -> 回顧dp[i-1] , dp[i-2] 都無法滿足partition且array[i-2]==array[i-1]==array[i]
        -> 回顧dp[i-1] , dp[i-2] 都無法滿足partition且array[i-2]+2 == array[i-1] + 1 == array[i]
        定義以上規則後,這一題的問題在於 , 會不會有情況是要先解除前面的partition , 才能增加新的partition? 
        
        即[1,1,2,3] , 所以應該可以看,假如前面的也可以分進partition , 後面再加入新值的時候是否會讓前面的partition失效
        我認為這一題應該從頭開始推 , 同時擴展上方的規則,並不一定要確認dp[i-1]或著dp[i-2]無法滿足partition , 因為有可能原先不滿足,但在加入新值後滿足了

        -> 上方[1,1,2,3]的情況 , 我直覺的去想,應該只有透過3個相同所組成的partition可以接受被拆掉一個作為123類型的partition , 只有2個的拆了會有異常    
            ,123類型的partition拆掉最後一個去配對2也會出問題
            
        -----------------------------
        被這一題挫折到了 , 看起來這一題的關鍵在於定義dp[i]為nums[0:i]範圍內是否可以valid partition,而不是在nums[0] -> nums[i]範圍 
        這樣在狀態轉移的使用到dp[i-2]實際上是在代表 nums[0:i-2]範圍是否可以滿足, 如果我用我原本的解法,那麼可能window要maintain四格
"""

""" 
    解法一. 按照我原先的思路,實際上狀態轉移不是單看前一格與前兩格所對應的dp , 而是要看到前三格 , 
            亦即 A B C D, 我們在D的回合檢查BC後,要用array直到A的範圍來判斷是否可以合併
"""
from typing import List 
class Solution:

    def validPartition(self, nums: List[int]) -> bool:
        
        dp = [False for i in range(len(nums))] 
        
        dp[0] = False 
        if nums[0] == nums[1] :  dp[1] = True 

        if len(nums) < 3 : return dp[-1] 
        
        if nums[0] == nums[1] == nums[2] :  
            dp[2] = True 
        elif nums[0] + 2 == nums[1] + 1 == nums[2] : 
            dp[2] = True 
            
            
        for i in range(3,len(nums)): 
            
            if nums[i] == nums[i-1] and dp[i-2] : 
                dp[i] = True 
            elif nums[i] == nums[i-1] == nums[i-2] and dp[i-3] : 
                dp[i] = True 
            
            elif nums[i] == nums[i-1]+1 == nums[i-2] + 2 and dp[i-3] : 
                dp[i] = True 
        return dp[-1] 
                
        
S = Solution() 
S.validPartition([803201,803201,803201,803201,803202,803203])



""" 
    解法二. 
        看Solution , 透過定義dp[i]為nums[0:i]範圍來解, 雖然在for loop內只用到2格之前,但要在dp額外建立一格我覺得也沒方便到哪
        而且index比較複雜
"""
from typing import List 
class Solution:

    def validPartition(self, nums: List[int]) -> bool:
        
        dp = [False for i in range(len(nums)+1)] 
        dp[0] = True 
        if nums[0] == nums[1] : 
            dp[2] = True 
            
        # dp[i] 表示nums[0:i]
        for i in range(2 , len(nums)): 
            
            if nums[i] == nums[i-1] and dp[i-1] == True : 
                dp[i+1] = True 
            
            elif nums[i] == nums[i-1] == nums[i-2] and dp[i-2] == True : 
                dp[i+1] = True 
            
            elif nums[i] == nums[i-1]+1 == nums[i-2] + 2 and dp[i-2] == True : 
                dp[i+1] = True 
        return dp[-1]


                

""" 
    解法三. 按照我原先的思路, 且dp的每一個步驟實際上只需要前三格 , 因此儲存可以提昇為O(C)
            
"""
from typing import List 
class Solution:

    def validPartition(self, nums: List[int]) -> bool:
        
        dp = [False for i in range(3)] 
        
        if nums[0] == nums[1] :  dp[1] = True 

        if len(nums) < 3 : return dp[1] 
        
        if nums[0] == nums[1] == nums[2] :  
            dp[2] = True 
        elif nums[0] + 2 == nums[1] + 1 == nums[2] : 
            dp[2] = True 
            
        
        # dp[2] : 前1格
        # dp[1] : 前2格
        # dp[0] : 前3格
        for i in range(3,len(nums)): 
            
            current = False 
            
            if nums[i] == nums[i-1] and dp[1] : 
                current = True 
            elif nums[i] == nums[i-1] == nums[i-2] and dp[0] : 
                current = True 
            
            elif nums[i] == nums[i-1]+1 == nums[i-2] + 2 and dp[0] : 
                current = True 
                
            dp[0] , dp[1] , dp[2] = dp[1] , dp[2] , current
            
        return dp[2]
                
        