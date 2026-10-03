"""
    題意 :
    給定整數陣列 nums,找出總和最大的連續子陣列,回傳該總和。
    子陣列至少包含一個元素,空陣列不算。

    LeetCode 53 · Medium
    URL : https://leetcode.com/problems/maximum-subarray/

    Example :
    nums = [-2,1,-3,4,-1,2,1,-5,4] -> 6
    nums = [1]                     -> 1
    nums = [5,4,-1,7,8]            -> 23

    Constraint :
    1 <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4

    思路 :
    這一題直覺上會想到雙指標,但稍微想一下會發現沒有特別能控制指標範圍伸縮的條件. 
    下一條路就是DP , 會思考要 1D or 2D DP
    會覺得可以用 DP , 
    dp[i] 表示 : 包含 nums[i] 作為結尾的子陣列最大可以到多少. 
    由於答案必定存在某一個子陣列 , 因此 max(dp) 就是答案. 
    而以 nums[i] 作為結尾的子陣列最大值 : max(nums[i] , nums[i] + dp[i-1]) 
    
    複雜度 : 
    時間複雜度 O(N) , 空間上只要常數個變數去紀錄當前最大值與 dp[i-1] 即可 , 故空間複雜度為 O(C)

    Trade-off :

"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maximum_subarray_sum = float("-inf")
        hook = None 

        for num in nums : 
            if hook is None : 
                hook = num 
            else :
                hook = max(num ,  num + hook)
            maximum_subarray_sum = max(maximum_subarray_sum , hook)
        
        return maximum_subarray_sum



if __name__ == "__main__":
    c = Solution()

    # (輸入, 預期輸出, 說明)
    test_set = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6, "官方範例:[4,-1,2,1]"),
        ([1], 1, "官方範例:單一正數"),
        ([5, 4, -1, 7, 8], 23, "官方範例:整段都要"),
        ([-1], -1, "邊界:單一負數"),
        ([-2, -1], -1, "全是負數,取最大的那個元素"),
        ([-3, -2, -1], -1, "全是負數,答案在尾端"),
        ([0], 0, "邊界:單一 0"),
        ([-1, 0, -2], 0, "0 比兩側的負數大"),
        ([1, 2, 3], 6, "整段遞增"),
        ([-2, 1], 1, "前面的負數要丟掉"),
        ([8, -19, 5, -4, 20], 21, "中段 [5,-4,20] 勝過單看兩端"),
        ([10000, -10000, 9999], 10000, "數值上下限,前段單看較大"),
        ([-10000, 10000], 10000, "數值上下限,答案是後半"),
    ]

    for nums, expected, note in test_set:
        result = c.maxSubArray(nums)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       input={nums} | expected={expected} | got={result}")
