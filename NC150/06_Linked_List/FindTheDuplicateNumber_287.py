"""
    題意 :
    給定一個整數陣列 nums,其中包含 n + 1 個整數,每個整數都落在 [1, n]。
    陣列裡只有一個數字會重複出現(至少兩次),其餘數字最多出現一次。
    回傳這個重複的數字。

    不得修改 nums,且只能使用常數額外空間。

    LeetCode 287 · Medium
    URL : https://leetcode.com/problems/find-the-duplicate-number/

    Example :
    nums = [1,3,4,2,2] -> 2
    nums = [3,1,3,4,2] -> 3
    nums = [3,3,3,3,3] -> 3

    Constraint :
    1 <= n <= 10^5
    nums.length == n + 1
    1 <= nums[i] <= n
    nums 中除了恰好一個數字會出現兩次以上,其餘數字都只出現一次

    思路 :

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        pass


if __name__ == "__main__":
    c = Solution()

    # (nums, 預期輸出) —— LeetCode 官方範例 + 邊界案例
    # 另檢查呼叫後 nums 沒有被改動
    test_set = [
        ([1, 3, 4, 2, 2], 2),
        ([3, 1, 3, 4, 2], 3),
        ([3, 3, 3, 3, 3], 3),                         # 同一個數字重複填滿
        ([1, 1], 1),                                  # 邊界:n = 1
        ([1, 3, 4, 2, 1], 1),                         # 重複值在頭尾
        ([2, 2, 2, 2, 2], 2),
        ([1, 4, 4, 2, 3], 4),                         # 重複值在中間
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 5], 5),          # 較長,重複一次
    ]

    for nums, expected in test_set:
        given = list(nums)
        result = c.findDuplicate(given)
        unchanged = given == nums
        passed = result == expected and unchanged
        status = "Pass" if passed else "Failed"
        print(
            f"{status} | input={nums} | expected={expected} | got={result} | unchanged={unchanged}"
        )
