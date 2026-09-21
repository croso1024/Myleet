"""
    題意 :
    有一個「升序排列」且元素皆相異的整數陣列 nums。
    在傳入函式之前,它可能已在某個未知的樞紐(pivot)index k(1 <= k < nums.length)被旋轉,
    使得結果變成 :
        [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]

    例如 [0,1,2,4,5,6,7] 在 pivot index 3 旋轉後,會變成 [4,5,6,7,0,1,2]。

    給定旋轉後的 nums 與整數 target,若 target 存在於 nums 中回傳其 index,否則回傳 -1。

    必須寫出 O(log n) 的演算法。

    LeetCode 33 · Medium
    URL : https://leetcode.com/problems/search-in-rotated-sorted-array/

    Example :
    nums = [4,5,6,7,0,1,2], target = 0 -> 4
    nums = [4,5,6,7,0,1,2], target = 3 -> -1
    nums = [1],             target = 0 -> -1

    Constraint :
    1 <= nums.length <= 5000
    -10^4 <= nums[i] <= 10^4
    nums 中所有整數皆相異
    nums 為升序排列,且「可能」被旋轉過(也可能沒有)
    -10^4 <= target <= 10^4

    思路 :

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pass


if __name__ == "__main__":
    c = Solution()

    R = [4, 5, 6, 7, 0, 1, 2]

    # (輸入參數 tuple, 預期輸出) —— LeetCode 官方範例 + 邊界案例
    test_set = [
        ((R, 0), 4),
        ((R, 3), -1),
        (([1], 0), -1),                                 # 邊界:單元素未命中
        (([1], 1), 0),                                  # 邊界:單元素命中
        ((R, 4), 0),                                    # 命中陣列最左端
        ((R, 2), 6),                                    # 命中陣列最右端
        ((R, 7), 3),                                    # 命中旋轉交界的左側
        ((R, 8), -1),                                   # target 大於所有元素
        ((R, -1), -1),                                  # target 小於所有元素
        (([3, 1], 1), 1),                               # 邊界:兩元素,有旋轉
        (([3, 1], 3), 0),
        (([1, 3], 3), 1),                               # 邊界:兩元素,未旋轉
        (([1, 2, 3, 4, 5], 4), 3),                      # 完全未旋轉
        (([5, 1, 2, 3, 4], 5), 0),                      # 旋轉點只差一格
        (([6, 7, 8, 1, 2, 3, 4, 5], 8), 2),             # 偶數長度,命中左半段
        (([6, 7, 8, 1, 2, 3, 4, 5], 5), 7),             # 偶數長度,命中右半段末端
    ]

    for args, expected in test_set:
        result = c.search(*args)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={args} | expected={expected} | got={result}")
