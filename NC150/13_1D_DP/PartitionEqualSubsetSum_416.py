"""
    題意 :
    給定一個只含正整數的陣列 nums。
    判斷能不能把它切成兩個子集,讓兩邊的元素和相等。
    每個元素只能放進其中一邊。

    LeetCode 416 · Medium
    URL : https://leetcode.com/problems/partition-equal-subset-sum/

    Example :
    nums = [1,5,11,5] -> True
    nums = [1,2,3,5]  -> False

    Constraint :
    1 <= nums.length <= 200
    1 <= nums[i] <= 100

    思路 :
    兩邊和相等,等於「能不能挑出一組數字,總和剛好是 sum(nums) / 2」。
    總和若是奇數,直接不可能。

    這是 0/1 背包的可行性版本,和 322 Coin Change 對照看。
    322 每種硬幣可以重複拿,問的是最少枚數;
    這一題每個數字最多用一次,問的是能不能剛好湊到 target。

    dp[s] 表示「不重複使用手上的數字,能不能湊出和 s」。dp[0] = True。
    外層走每一個 num,內層從 target 往回倒到 num。
    倒著走的原因:更新 dp[s] 時,dp[s - num] 還是「還沒用過這個 num」的舊值。
    若從左往右走,dp[s - num] 可能已經被同一個 num 更新過,就變成 322 的完全背包。

    複雜度 :
    時間複雜度 O(n * target),target = sum(nums) / 2。
    空間複雜度 O(target),只留一列布林值。

    Trade-off :
    二維表 dp[i][s] 比較好對照「前 i 個數字能不能湊出 s」,空間是 O(n * target)。
    因為轉移只依賴上一列、而且同一列要從右邊讀,壓成一列就夠,這輪用滾動陣列。

"""

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total // 2
        # dp[s]: 目前看過的數字能不能湊出和 s。0 什麼都不拿就湊得到。
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            # 倒著走,同一個 num 不會被用兩次。
            for amount in range(target, num - 1, -1):
                if dp[amount - num]:
                    dp[amount] = True

        return dp[target]


if __name__ == "__main__":
    c = Solution()

    # (nums, 預期, 說明)
    test_set = [
        ([1, 5, 11, 5], True, "官方範例:1+5+5 = 11"),
        ([1, 2, 3, 5], False, "官方範例:總和是奇數"),
        ([1, 2, 5], False, "總和 8,target 4,但不能把 2 用兩次"),
        ([1, 2, 3, 4], True, "1+4 = 2+3"),
        ([2, 2], True, "兩半各一個 2"),
        ([1, 1], True, "兩半各一個 1"),
        ([100], False, "只有一個數"),
        ([1], False, "邊界:長度 1"),
        ([1, 1, 1, 1], True, "四個 1,各邊兩個"),
        ([3, 3, 3, 4, 5], True, "3+3+3 = 4+5"),
        ([1, 2, 3, 6], True, "1+2+3 = 6"),
        ([2, 2, 2], False, "總和 6,target 3,2 湊不出 3"),
        ([1, 5, 5, 11], True, "1+5+5 = 11"),
        ([10, 10], True, "兩個相同的數"),
        ([1, 1, 2], True, "1+1 = 2"),
    ]

    for nums, expected, note in test_set:
        result = c.canPartition(nums)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       input={nums} | expected={expected} | got={result}")
