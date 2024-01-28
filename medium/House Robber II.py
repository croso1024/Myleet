""" 
    思路 : 
        這一題相較House Robber I , 就是將頭尾兩端給串連起來 ,因此隔絕掉頭尾兩端都有偷的情況
        換個角度想這一題 , 
        1. 實際上可以先求去頭去尾的範圍內 , 最大值後再從頭或尾選一個就可以了 (但假如選頭 , 會沒辦法拿到 從 1 : len(nums)-1範圍的最大值來加)
        2. 二維的dp-table , 即 dp[i][j]是 i~j範圍內的最大值 , 但這樣可能會造成更多空間浪費
        
        3. -> 做兩次DP , 因為頭尾不能同時選 , 所以做 "含頭去尾" 範圍的最大值 與 "去頭含尾" 做比較
"""



""" 
    做兩次DP的戰術
"""
from typing import List 
class Solution:
    
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) <= 3 : return max(nums) 
        
        # dp函數的定義是給一個範圍 , 返回該範圍內的最佳值 
        def dp( nums ): 
            if len(nums) <= 2 : return max(nums) 
            prev_2 = nums[0]
            prev_1 = max(nums[0],nums[1]) 
            
            for i in range(2 , len(nums)): 
                temp = max( nums[i] + prev_2 , prev_1  )
                prev_2 = prev_1 
                prev_1 = temp 
            return temp 

        # 選擇head可以到達的最大值 
        head = dp( nums[: len(nums)-1 ]    ) 
        tail = dp( nums[ 1 : ])

        return head if head > tail else tail