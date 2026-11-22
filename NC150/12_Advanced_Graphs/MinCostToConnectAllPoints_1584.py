"""
    題意 :
    給定 2D 平面上的 n 個點 points,points[i] = [xi, yi]。
    連接兩點 (xi, yi) 與 (xj, yj) 的成本是它們的曼哈頓距離 |xi - xj| + |yi - yj|。

    回傳讓「所有點彼此連通」的最小總成本。
    連通的定義:任兩點之間「有且只有一條」簡單路徑。

    LeetCode 1584 · Medium
    URL : https://leetcode.com/problems/min-cost-to-connect-all-points/

    Example :
    points = [[0,0],[2,2],[3,10],[5,2],[7,0]] -> 20
    points = [[3,12],[-2,5],[-4,1]]           -> 18

    Constraint :
    1 <= points.length <= 1000
    -10^6 <= xi, yi <= 10^6
    所有點 (xi, yi) 互不重複

    思路 :

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    c = Solution()

    # (points, 預期, 說明)
    # 每次呼叫都複製 points,實作改到測資本身不會留到下一題
    test_set = [
        ([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]], 20, "官方範例:5 個點"),
        ([[3, 12], [-2, 5], [-4, 1]], 18, "官方範例:3 個點,含負座標"),
        ([[0, 0]], 0, "邊界:只有一個點"),
        ([[0, 0], [1, 1]], 2, "邊界:兩個點,只有一條可選的邊"),
        ([[0, 0], [1, 0], [2, 0], [3, 0]], 3, "4 個點共線,間距皆為 1"),
        ([[0, 0], [0, 1], [1, 0], [1, 1]], 3, "單位正方形的 4 個頂點,四條邊長度相同"),
        (
            [[0, 0], [2, 0], [-2, 0], [0, 2], [0, -2]],
            8,
            "原點加上四個方向各距離 2 的點",
        ),
        (
            [[0, 0], [1, 1], [1, 0], [-1, 1], [3, 3]],
            8,
            "5 個點,多條邊的成本相同",
        ),
        (
            [[-1000000, -1000000], [1000000, 1000000]],
            4000000,
            "邊界:座標範圍的兩個對角端點",
        ),
    ]

    for points, expected, note in test_set:
        result = c.minCostConnectPoints([p[:] for p in points])
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       points={points}")
        print(f"       expected={expected}")
        print(f"       got     ={result}")
