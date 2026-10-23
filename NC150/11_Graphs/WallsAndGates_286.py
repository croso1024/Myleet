"""
    題意 :
    給定一個 m x n 的網格 rooms。每個格子是以下三者之一:
    -1 代表牆,0 代表門,2147483647(2^31 - 1)代表空房間。
    空房間到門的距離保證小於 2147483647。

    把每個空房間填成它到最近一扇門的距離。
    走得到的方向只有上下左右。到不了任何門的空房間維持 2147483647。
    牆與門本身不要改。

    直接改 rooms,不要回傳新的網格。

    LeetCode 286 · Medium
    URL : https://leetcode.com/problems/walls-and-gates/

    Example :
    INF = 2147483647
    rooms = [
      [INF,-1,0,INF],
      [INF,INF,INF,-1],
      [INF,-1,INF,-1],
      [0,-1,INF,INF],
    ] -> [
      [3,-1,0,1],
      [2,2,1,-1],
      [1,-1,2,-1],
      [0,-1,3,4],
    ]
    rooms = [[-1]] -> [[-1]]

    Constraint :
    m == rooms.length
    n == rooms[i].length
    1 <= m, n <= 250
    rooms[i][j] 是 -1、0 或 2^31 - 1

    思路 :

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

import copy
from typing import List


INF = 2147483647


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        pass


if __name__ == "__main__":
    c = Solution()

    official = [
        [INF, -1, 0, INF],
        [INF, INF, INF, -1],
        [INF, -1, INF, -1],
        [0, -1, INF, INF],
    ]
    official_expected = [
        [3, -1, 0, 1],
        [2, 2, 1, -1],
        [1, -1, 2, -1],
        [0, -1, 3, 4],
    ]

    # (rooms, 預期, 說明)
    # 這一題改的是傳進去的網格本身,每次都複製一份再比對
    test_set = [
        (official, official_expected, "官方範例:兩扇門同時往外量距離"),
        ([[-1]], [[-1]], "官方範例:只有一面牆"),
        ([[0]], [[0]], "邊界:只有一扇門"),
        ([[INF]], [[INF]], "只有一間空房,沒有門"),
        ([[0, INF]], [[0, 1]], "門的右邊一格"),
        ([[INF, -1, 0]], [[INF, -1, 0]], "牆擋住,左邊的空房到不了門"),
        (
            [[INF, INF], [INF, 0]],
            [[2, 1], [1, 0]],
            "門在右下角,距離沿兩條路展開",
        ),
        ([[0, INF, 0]], [[0, 1, 0]], "兩扇門中間那格,距離取較近的 1"),
        (
            [[-1, INF, -1], [-1, -1, -1]],
            [[-1, INF, -1], [-1, -1, -1]],
            "空房被牆圍住,維持 INF",
        ),
        (
            [[0, -1], [INF, INF]],
            [[0, -1], [1, 2]],
            "只能繞過牆,往下再往右",
        ),
    ]

    for rooms, expected, note in test_set:
        snapshot = copy.deepcopy(rooms)
        c.wallsAndGates(snapshot)
        passed = snapshot == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       expected={expected}")
        print(f"       got     ={snapshot}")
