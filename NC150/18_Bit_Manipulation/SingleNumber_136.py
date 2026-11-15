"""
    題意 :
    給定一個非空的整數陣列 nums。
    除了某一個元素只出現一次,其餘每個元素都剛好出現兩次。
    找出那個只出現一次的元素。

    題目要求:時間複雜度為線性,且只使用常數的額外空間。

    LeetCode 136 · Easy
    URL : https://leetcode.com/problems/single-number/

    Example :
    nums = [2,2,1]     -> 1
    nums = [4,1,2,1,2] -> 4
    nums = [1]         -> 1

    Constraint :
    1 <= nums.length <= 3 * 10^4
    -3 * 10^4 <= nums[i] <= 3 * 10^4
    除了一個元素只出現一次,其餘每個元素都剛好出現兩次

    思路 :

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        pass


if __name__ == "__main__":
    c = Solution()

    # (nums, 預期, 說明)
    test_set = [
        ([2, 2, 1], 1, "官方範例"),
        ([4, 1, 2, 1, 2], 4, "官方範例"),
        ([1], 1, "官方範例:邊界,長度 1"),
        ([-1], -1, "長度 1,負數"),
        ([-3, 5, -3], 5, "答案在中間"),
        ([0, 7, 7], 0, "答案是 0"),
        ([0, 0, -5], -5, "答案是負數,0 成對出現"),
        ([6, 6, 9, 9, 8], 8, "答案在最後一個位置"),
        ([10, 20, 30, 20, 10], 30, "成對的元素沒有相鄰"),
        ([30000, -30000, 30000], -30000, "數值上下界"),
    ]

    for nums, expected, note in test_set:
        result = c.singleNumber(nums[:])
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       input={nums} | expected={expected} | got={result}")
