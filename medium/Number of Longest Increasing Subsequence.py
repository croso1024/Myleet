""" 
    思路 : 
        題目給定一組array , "求最長的Increaseing subsequence有幾組" , 
        ex. 例如可能最長的sub-array長度為4, 一共有多組可以到達
        
        稍微想了一下 , 一樣使用1D-DP , 定義dp[i]為 : 以index=i為結尾的subsequence , 其最大長度為x , 該長度共有y條
        即 dp[i]=(x,y) 
        
        base-case : dp[0] = (1,1)

"""

from typing import List 

class Solution:
    
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [[1,1] for i in range(len(nums))] 
        
        # 外層推進DP狀態 , 但實際上我們還要推內層 , 往前檢查 
        for i in range(1 , len(nums)): 
            # 內層迴圈 , 因為我們要檢查前面的元素 , 是否可以更長 , maintain最長的組數 
            for j in range(i) : 
                
                if nums[i] > nums[j]  : 
                    
                    if dp[j][0] + 1 > dp[i][0] : 
                        dp[i][0] = dp[j][0] + 1 
                        dp[i][1] = dp[j][1]  

                    elif dp[j][0] + 1 == dp[i][0] : 
                        dp[i][1] += dp[j][1] 

                elif nums[i] == nums[j] : 
                    
                    if dp[j][0] > dp[i][0] : 
                        dp[i][0] = dp[j][0]
                        dp[i][1] = dp[j][1] 
                else : 
                    pass                     
                    
        # 最終會得到一個array , 包含了以所有元素為結尾的最長subsequence , 以及其有幾組 
        # 透過一個迴圈去收取這些資訊 
        max_length = float("-inf")
        max_length_freq = 0 
        
        for i in range(len(nums)): 
            
            if dp[i][0] > max_length : 
                max_length = dp[i][0]
                max_length_freq = dp[i][1] 
            
            elif dp[i][0] == max_length : 
                max_length_freq +=  dp[i][1]
        return max_length_freq

test = [1,3,5,4,7]
S = Solution() 
print(S.findNumberOfLIS(test) ) 
