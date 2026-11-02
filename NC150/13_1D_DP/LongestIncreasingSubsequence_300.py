"""
    題意 :
    給定一個整數陣列 nums。
    回傳最長嚴格遞增子序列的長度。
    子序列不必連續,但留下的數字必須保持原本的相對順序。

    LeetCode 300 · Medium
    URL : https://leetcode.com/problems/longest-increasing-subsequence/

    Example :
    nums = [10,9,2,5,3,7,101,18] -> 4
    nums = [0,1,0,3,2,3]         -> 4
    nums = [7,7,7,7]             -> 1

    Constraint :
    1 <= nums.length <= 2500
    -10^4 <= nums[i] <= 10^4

    思路 :
    
    這一題的關鍵應該是該如何定義 DP 狀態 , dp[i] 要表示什麼? 
    用 dp[i] 表達 , 以 nums[i] 結尾的子陣列的單調遞增最大值為多少,那解答就是在Traverse過程中找到的最大值. 
    以此定義去描述,那可以怎樣推導出狀態轉移!? 

    dp[i] 是以 nums[i] 為結尾的最大子陣列單調遞增數 , 
    但要填入 dp[i] 時 , 要看的應該是 nums 在 i 之前,所有小於 nums[i] 的值對應的nums[j] 對應的 dp[j] , 找出 dp[j] 最大的 +1 就是 dp[i]

    以原題 [ 10 9 2 5 3 7 101 18 ]
    10 : 第一格值固定為1 
    9 : 往前找有沒有 < 9 的 , 沒有就 1 
    2 : 往前找有沒有 <2 的 ,沒有就1 
    5 : 往前找有沒有 <5 的 , 從所有小於5的對應的 dp[j] 找最大的 + 1
    3 : 往前找有沒有 <3 的 , 從所有小於5的對應的 dp[j] 找最大的 + 1
    ... 
    
    複雜度 : 
    這個解法的時間複雜度就是 O(N^2) , 空間複雜度 O(N)

    follow up 要求 O( N Log N ) 級別的解法,我的理解是在往前看搜索時要有更快的方式

    Trade-off :

"""

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [None for _ in range(len(nums))]
        dp[0] = 1 

        for i in range(1,len(nums)) : 

            # current index = i , 
            # handle dp[i] 
            # 找出所有小於 nums[i] 的 nums[j] 內 dp[j] 最大的 + 1 就是 dp[i]
            dp[i] = max([ dp[j] for j in range(i) if nums[j] < nums[i] ] + [0])  + 1  
        
        return max(dp)


if __name__ == "__main__":
    c = Solution()

    # (nums, 預期, 說明)
    test_set = [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4, "官方範例"),
        ([0, 1, 0, 3, 2, 3], 4, "官方範例"),
        ([7, 7, 7, 7], 1, "官方範例"),
        ([1], 1, "邊界:只有一個數字"),
        ([1, 2, 3], 3, "嚴格遞增"),
        ([3, 2, 1], 1, "嚴格遞減"),
        ([-2, -1], 2, "含負數"),
        ([1, 3, 6, 7, 9, 4, 10, 5, 6], 6, "中段插入較小的數字"),
        ([4, 10, 4, 3, 8, 9], 3, "有重複的起點"),
        ([2, 2, 2, 3], 2, "前段相同"),
        ([10, 9, 8, 1, 2, 3], 3, "前段遞減"),
        ([1, 2, 0, 3], 3, "中間插入較小值"),
    ]

    for nums, expected, note in test_set:
        result = c.lengthOfLIS(nums)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       input={nums} | expected={expected} | got={result}")
