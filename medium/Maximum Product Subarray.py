""" 
    思路:   
        首先看到這一題找Subarray->想到DP , 這題是要找一段連續的子陣列 , 但因為缺乏明確何時要收縮/擴大
        所以不太能上sliding window , 思考流程往 single-array 1D/2D DP去想
        
        看起來是可以Run 1D , dp[i]代表以i為結尾的sub-array的Maximum product 
        因為這一題對於subarray的定義要求元素間的連續 , 因此這樣定義確保了在計算dp[i+1]的時候 , 使用dp[i]是合法的
        因為計算完如果可以採用 , 則nums[i]和nums[i+1]為連續 
        
        定義dp[i]代表 以index=i為最後一個元素的sub-array的 maximum product 
        最後的解為 max(dp)
        
        State transition function :  以 i+1 為結尾的subarray, 他最大maximum product只有兩個可能性(動作)
        1. 和先前的sub-array相乘 , 可以得到更大的sub-array的話
        2. 不要用先前的sub-array了 , 從i+1開始去找新的sub-array
        
        以上的思路有問題 , 遇到[-2,3,-4]的時候會認為答案是 3 而不是24  
        
        我想問題是出在我直接捨棄掉先前的sub array , 好像是一個我常犯下的bug 
        如果要更改, 可能會需要類似 Longest increase subsequence , 去在內迴圈尋訪所有先前元素 
     
        --------------
     
        根據東哥的想法 , 剛剛那樣的情況是指 
        假設我已知由 i 結尾的array最大乘積為 10 , 那當nums[i+1]= -1 的時候 
        不能直接使用  dp[i+1] = max( nums[i] , nums[i] * dp[i] ) = -1  
        因為nums[i]有可能是負數 , 所以我們還要額外maintain一個由 i 結尾array的最小值 
        
        dpMax[i+1] = max( nums[i] , nums[i]*dpMax[i] , nums[i]*dpMin[i] )
        dpMin[i+1] = min( nums[i] , nums[i]*dpMax[i] , nums[i]*dpMin[i] )
        

        
"""


""" 
    解法一. 按照東哥的套路思維 , 兩個1D table去maintain 最大值和最小值
    
    速度非常快了 , 但空間不太好
"""

from typing import List 

class Solution:

    def maxProduct(self, nums: List[int]) -> int:

        size = len(nums)
        
        dpMax = [None] * size
        dpMin = [None] * size
        
        dpMax[0] = nums[0]
        dpMin[0] = nums[0]             
        
        for i in range(1,size): 
            
            dpMax[i] = max( nums[i] , nums[i]*dpMax[i-1] , nums[i]*dpMin[i-1] )
            dpMin[i] = min( nums[i] , nums[i]*dpMax[i-1] , nums[i]*dpMin[i-1] )
        
        return max(dpMax)
    
    

""" 
    解法二. 解法一 , 去優化空間
    
"""

from typing import List 

class Solution:

    def maxProduct(self, nums: List[int]) -> int:

        size = len(nums)
        
        
        max_prev = nums[0]
        min_prev = nums[0]             
        
        best = max_prev
        
        for i in range(1,size): 
            
            tempMax = max( nums[i] , nums[i]*max_prev , nums[i]*min_prev )
            tempMin = min( nums[i] , nums[i]*max_prev , nums[i]*min_prev )
            
            if tempMax > best : 
                best = tempMax
            
            max_prev = tempMax 
            min_prev = tempMin
        
        return best