""" 
    題意:

        給定一個array nums , 要求計算最大的交替substring sum , 交替subsequence sum的意思就是選擇一個subsequece sub
        最大化 sub[0] - sub[1] + sub[2] - sub[3] ... 的值,
        而subsequence的定義只要保證其元素在原始nums中的相對順序,而不必要是連續的
    
    思路:

        dp[i] : (0:i範圍 , 最後一個選正的最大值 , 0:i範圍, 最後一個選負的最大值)
        state transition fuction:

            dp[i][0] = max(nums[i] , nums[i] + dp[i-1][1] )
            dp[i][1] = max( -nums[i] , dp[i-1][0] - nums[i]  )        
        
        算是蠻直觀 , 當前要選的是正的時候 , 就看 :
        1. 只選這個正值
        2. 在先前範圍內上一個選負的最大值加這個正值
        3. 完全不動這個數值, 先前範圍最後一次選正的最大值 
        
"""
from typing import List 

class Solution:

    def maxAlternatingSum(self, nums: List[int]) -> int:

        dp = [ [None , None] for i in range(len(nums))]
        dp[0] = [nums[0] , -(nums[0])]
        for i in range(1 , len(nums)): 
            
            dp[i][0] = max(nums[i] , nums[i] + dp[i-1][1] ,dp[i-1][0] )
            dp[i][1] = max( -nums[i] , dp[i-1][0] - nums[i] , dp[i-1][1] ) 
        return dp[-1][0]         

S = Solution()
# print(S.maxAlternatingSum([6,2,1,2,4,5]))
print(S.maxAlternatingSum([5,6,7,8]))


""" 
    因為實際上只用到前一格dp, 可以做空間壓縮
"""
class Solution:

    def maxAlternatingSum(self, nums: List[int]) -> int:

        prev = [nums[0] , -nums[0]]
        
        for i in range(1 , len(nums)): 
            
            temp = [None ,None]
            temp[0] = max(nums[i] , nums[i] + prev[1] ,prev[0] )
            temp[1] = max( -nums[i] , prev[0] - nums[i] , prev[1] ) 
            prev = temp 
            
        return prev[0]
