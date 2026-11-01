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
    dp[i] 定義成「以 nums[i] 結尾的最長嚴格遞增子序列長度」。
    單一個數字本身就是長度 1,所以初值全是 1。

    轉移:看所有排在 i 前面的 j。
    若 nums[j] < nums[i],就可以把 nums[i] 接在那條子序列後面,
    dp[i] = max(dp[i], dp[j] + 1)。
    答案是整排 dp 的最大值,不一定在最後一格,因為最長的那條不一定以最後一個數字結尾。

    這輪先寫這個 O(n^2) 定義。它把「結尾元素」釘死,轉移才看得清楚。

    複雜度 :
    時間複雜度 O(n^2),每一對 (j, i) 都看一次。
    空間複雜度 O(n)。

    Trade-off :
    另有 patience sorting:維護一排「長度為 k 的遞增子序列裡,結尾最小的那個值」,
    對每個數字做二分插入或取代,時間 O(n log n)。
    那一排的長度是答案,但裡面的內容不一定是真正的某一條子序列。
    CORE_LIST 要求 O(n^2) 先寫熟,二分版留到這題的定義已經穩了再加。

"""

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # dp[i]: 以 nums[i] 結尾的最長嚴格遞增子序列長度
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


if __name__ == "__main__":
    c = Solution()

    # (nums, 預期, 說明)
    test_set = [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4, "官方範例:2,3,7,101"),
        ([0, 1, 0, 3, 2, 3], 4, "官方範例:0,1,2,3"),
        ([7, 7, 7, 7], 1, "官方範例:相等不能接,答案是 1"),
        ([1], 1, "邊界:只有一個數字"),
        ([1, 2, 3], 3, "整串已經嚴格遞增"),
        ([3, 2, 1], 1, "嚴格遞減"),
        ([-2, -1], 2, "負數也可以遞增"),
        ([1, 3, 6, 7, 9, 4, 10, 5, 6], 6, "1,3,6,7,9,10"),
        ([4, 10, 4, 3, 8, 9], 3, "3,8,9 或 4,8,9"),
        ([2, 2, 2, 3], 2, "相等的 2 只能留一個,再接 3"),
        ([10, 9, 8, 1, 2, 3], 3, "最長的一段在尾巴"),
        ([1, 2, 0, 3], 3, "1,2,3,中間的 0 接不進這條"),
    ]

    for nums, expected, note in test_set:
        result = c.lengthOfLIS(nums)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       input={nums} | expected={expected} | got={result}")
