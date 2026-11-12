"""
    題意 :
    給定一個整數陣列 nums。
    找出一個連續子陣列,使它的元素乘積最大,回傳那個乘積。
    子陣列至少要有一個元素。

    LeetCode 152 · Medium
    URL : https://leetcode.com/problems/maximum-product-subarray/

    Example :
    nums = [2,3,-2,4] -> 6
    nums = [-2,0,-1]  -> 0

    Constraint :
    1 <= nums.length <= 2 * 10^4
    -10 <= nums[i] <= 10
    任一子陣列的乘積都落在 32-bit 整數範圍內

    思路 :

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pass


if __name__ == "__main__":
    c = Solution()

    # (nums, 預期, 說明)
    # 每次呼叫都複製 nums,實作改到測資本身不會留到下一題
    test_set = [
        ([2, 3, -2, 4], 6, "官方範例:正數段 [2,3]"),
        ([-2, 0, -1], 0, "官方範例:0 隔開兩個負數,答案是 0"),
        ([-2], -2, "邊界:只有一個負數"),
        ([0], 0, "邊界:只有一個 0"),
        ([2], 2, "邊界:只有一個正數"),
        ([-2, -3], 6, "兩個負數相乘轉正"),
        ([-2, -3, -4], 12, "三個負數,取尾端兩個"),
        ([0, 2], 2, "前導 0,答案在 0 的右邊"),
        ([2, 0, 3], 3, "0 把陣列切開,取較大的那一段"),
        ([3, -1, 4], 4, "跨過負數會變小,答案是單一正數"),
        ([2, -5, -2, -4, 3], 24, "奇數個負數,要丟掉一個負數"),
        ([1, -2, 3, -4], 24, "偶數個負數,整段乘起來最大"),
        ([-1, 0, -2], 0, "負數被 0 隔開,沒有正的乘積"),
        ([2, 3, -2, 4, -1], 48, "尾端再乘一個負數,整段變成最大"),
    ]

    for nums, expected, note in test_set:
        result = c.maxProduct(nums[:])
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       input={nums} | expected={expected} | got={result}")
