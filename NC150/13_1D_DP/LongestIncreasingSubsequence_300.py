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

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        pass


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
