"""
    題意 :
    給定一個 m x n 的整數矩陣 matrix,它具有以下兩個性質 :
      - 每一列(row)由左至右為非遞減排序。
      - 每一列的第一個整數,都大於前一列的最後一個整數。

    再給定一個整數 target,若 target 存在於 matrix 中回傳 True,否則回傳 False。

    必須寫出 O(log(m*n)) 的演算法。

    LeetCode 74 · Medium
    URL : https://leetcode.com/problems/search-a-2d-matrix/

    Example :
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3  -> True
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13 -> False

    Constraint :
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 100
    -10^4 <= matrix[i][j], target <= 10^4

    思路 :

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        pass


if __name__ == "__main__":
    c = Solution()

    M = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]

    # (輸入參數 tuple, 預期輸出) —— LeetCode 官方範例 + 邊界案例
    test_set = [
        ((M, 3), True),
        ((M, 13), False),
        ((M, 1), True),                                 # 命中整個矩陣的最小值
        ((M, 60), True),                                # 命中整個矩陣的最大值
        ((M, 7), True),                                 # 命中某列的最後一格
        ((M, 10), True),                                # 命中某列的第一格
        ((M, 0), False),                                # target 小於所有元素
        ((M, 61), False),                               # target 大於所有元素
        (([[1]], 1), True),                             # 邊界:1x1 命中
        (([[1]], 2), False),                            # 邊界:1x1 未命中
        (([[1, 3, 5]], 5), True),                       # 邊界:單列
        (([[1, 3, 5]], 4), False),
        (([[1], [3], [5]], 3), True),                   # 邊界:單行
        (([[1], [3], [5]], 4), False),
        (([[-10, -5], [0, 7]], -5), True),              # 含負數
        (([[-10, -5], [0, 7]], -7), False),
    ]

    for args, expected in test_set:
        result = c.searchMatrix(*args)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={args} | expected={expected} | got={result}")
