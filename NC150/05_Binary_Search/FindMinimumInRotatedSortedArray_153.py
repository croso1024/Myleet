"""
    題意 :
    有一個長度為 n、原本為「升序排列」的陣列,被旋轉了 1 到 n 次。
    例如 nums = [0,1,2,4,5,6,7] 可能變成 :
      - [4,5,6,7,0,1,2]  (旋轉 4 次)
      - [0,1,2,4,5,6,7]  (旋轉 7 次,等於轉回原樣)

    旋轉一次的定義 : [a[0], a[1], ..., a[n-1]] -> [a[n-1], a[0], a[1], ..., a[n-2]]

    給定這個「已排序並旋轉過」且元素皆相異的陣列 nums,回傳其中的最小元素。

    必須寫出 O(log n) 的演算法。

    LeetCode 153 · Medium
    URL : https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

    Example :
    nums = [3,4,5,1,2]     -> 1
    nums = [4,5,6,7,0,1,2] -> 0
    nums = [11,13,15,17]   -> 11

    Constraint :
    n == nums.length
    1 <= n <= 5000
    -5000 <= nums[i] <= 5000
    nums 中所有整數皆相異
    nums 為升序排列後旋轉 1 到 n 次的結果

    思路 :

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        pass


if __name__ == "__main__":
    c = Solution()

    # (輸入參數 tuple, 預期輸出) —— LeetCode 官方範例 + 邊界案例
    test_set = [
        (([3, 4, 5, 1, 2],), 1),
        (([4, 5, 6, 7, 0, 1, 2],), 0),
        (([11, 13, 15, 17],), 11),
        (([1],), 1),                                    # 邊界:單元素
        (([2, 1],), 1),                                 # 邊界:兩元素,有旋轉
        (([1, 2],), 1),                                 # 邊界:兩元素,未旋轉
        (([5, 1, 2, 3, 4],), 1),                        # 最小值落在 index 1
        (([2, 3, 4, 5, 1],), 1),                        # 最小值落在最末端
        (([3, 1, 2],), 1),                              # 奇數長度,最小值在中間
        (([-5000, 5000],), -5000),                      # 邊界:數值上下限
        (([-1, 0, 1, 2, -3, -2],), -3),                 # 全區間含負數
        (([4, 5, 6, 7, 8, 1, 2, 3],), 1),               # 偶數長度,旋轉點偏右
    ]

    for args, expected in test_set:
        result = c.findMin(*args)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={args} | expected={expected} | got={result}")
