"""
    題意 :
    給定一個 m x n 的網格 grid。每個格子是以下三者之一:
    0 代表空格,1 代表新鮮橘子,2 代表腐爛橘子。

    每一分鐘,與腐爛橘子上下左右相鄰的新鮮橘子都會腐爛。
    斜對角不算相鄰。
    回傳直到沒有新鮮橘子為止的最少分鐘數。
    若不可能讓所有新鮮橘子都腐爛,回傳 -1。

    LeetCode 994 · Medium
    URL : https://leetcode.com/problems/rotting-oranges/

    Example :
    grid = [[2,1,1],[1,1,0],[0,1,1]] -> 4
    grid = [[2,1,1],[0,1,1],[1,0,1]] -> -1
    grid = [[0,2]]                   -> 0

    Constraint :
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 10
    grid[i][j] 是 0、1 或 2

    思路 :

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

import copy
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    c = Solution()

    # (grid, 預期, 說明)
    # 每題都複製一份 grid,避免上一題把格子改掉
    test_set = [
        (
            [[2, 1, 1], [1, 1, 0], [0, 1, 1]],
            4,
            "官方範例:從左上角擴散,需要 4 分鐘",
        ),
        (
            [[2, 1, 1], [0, 1, 1], [1, 0, 1]],
            -1,
            "官方範例:左下角的新鮮橘子被空格隔開",
        ),
        ([[0, 2]], 0, "官方範例:沒有新鮮橘子"),
        ([[1]], -1, "邊界:只有一顆新鮮橘子,沒有腐爛源"),
        ([[2]], 0, "邊界:只有一顆腐爛橘子"),
        ([[0]], 0, "邊界:只有空格"),
        ([[1, 2]], 1, "右邊的腐爛橘子一分鐘傳染左邊"),
        ([[2, 0, 1]], -1, "中間空格隔開,右邊永遠不會爛"),
        ([[1, 1, 2]], 2, "只有一列,從右端往左擴散"),
        (
            [[2, 2], [1, 1]],
            1,
            "兩顆新鮮橘子各自鄰接一顆腐爛橘子",
        ),
        (
            [[2, 1, 1], [1, 1, 1], [0, 1, 2]],
            2,
            "兩個腐爛源同時擴散,中心在第 2 分鐘爛掉",
        ),
        ([[1, 1], [1, 1]], -1, "全是新鮮橘子"),
        ([[0, 0], [0, 0]], 0, "全是空格"),
    ]

    for grid, expected, note in test_set:
        result = c.orangesRotting(copy.deepcopy(grid))
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       expected={expected} | got={result}")
