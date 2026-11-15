"""
    題意 :
    給定一個 m x n 的整數矩陣 matrix,
    請依照「順時針螺旋順序 (spiral order)」回傳矩陣中的所有元素。

    LeetCode 54 · Medium
    URL : https://leetcode.com/problems/spiral-matrix/

    Example :
    matrix = [[1,2,3],[4,5,6],[7,8,9]]             -> [1,2,3,6,9,8,7,4,5]
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]    -> [1,2,3,4,8,12,11,10,9,5,6,7]

    Constraint :
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 10
    -100 <= matrix[i][j] <= 100

    思路 :

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        pass


if __name__ == "__main__":
    c = Solution()

    # (matrix, 預期, 說明)
    # 每次呼叫都複製 matrix,實作改到測資本身不會留到下一題
    test_set = [
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [1, 2, 3, 6, 9, 8, 7, 4, 5],
            "官方範例:3x3 方陣",
        ),
        (
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
            "官方範例:3x4 寬矩陣",
        ),
        ([[42]], [42], "邊界:1x1 單一元素"),
        ([[1, 2, 3, 4]], [1, 2, 3, 4], "邊界:1x4 單列,不能重複走回頭路"),
        ([[1], [2], [3], [4]], [1, 2, 3, 4], "邊界:4x1 單欄,不能重複走回頭路"),
        ([[1, 2], [3, 4]], [1, 2, 4, 3], "2x2 偶數方陣"),
        ([[1, 2, 3], [4, 5, 6]], [1, 2, 3, 6, 5, 4], "2x3 兩列寬矩陣"),
        ([[1, 2], [3, 4], [5, 6]], [1, 2, 4, 6, 5, 3], "3x2 兩欄長矩陣"),
        (
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
            [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10],
            "4x4 偶數方陣,兩層完整螺旋",
        ),
        ([[-100, 0], [100, -1]], [-100, 0, -1, 100], "邊界值:含負數與 0"),
    ]

    for matrix, expected, note in test_set:
        result = c.spiralOrder([row[:] for row in matrix])
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       expected={expected}")
        print(f"       got     ={result}")
