"""
    題意 :
    給定長度為 n 的整數陣列 height，height[i] 代表在座標 i 處有一條垂直線，
    兩端點為 (i, 0) 與 (i, height[i])。從中選兩條線，與 x 軸構成一個容器，
    求這個容器能裝的最大水量（面積 = 兩線中較短的高度 x 兩線之間的水平距離）。

    Constraint :
    n == height.length
    2 <= n <= 10^5
    0 <= height[i] <= 10^4

    思路 :

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        pass


if __name__ == "__main__":
    c = Solution()

    # (輸入參數 tuple, 預期輸出) —— LeetCode 官方範例
    test_set = [
        (([1, 8, 6, 2, 5, 4, 8, 3, 7],), 49),
        (([1, 1],), 1),
    ]

    for args, expected in test_set:
        result = c.maxArea(*args)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={args} | expected={expected} | got={result}")
