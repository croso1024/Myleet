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
    這一題直覺上就是一個擴散。題目要的是每一個空房間到達最近一扇門的距離。
    而且是要直接修改棋盤格
    沒有辦法到達的就維持原樣. 

    直覺上走分層的BFS , 第一輪從所有門開始走.
    可以往四面八方走,但不能走到已經走過的空房間和牆壁。 
    同時記錄當前BFS的輪數,作為走到空房間時填入步數的標準. 

    複雜度 : 
    走BFS , 時間複雜度為棋盤格總大小 O(N) , 空間複雜度在 worse case (所有房間都是門,第一輪BFS爆滿) 的情況下也為 O(N)

    Trade-off :

"""

import copy
from typing import List
from collections import deque

INF = 2147483647


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        
        DIRS = [(-1,0),(1,0),(0,1),(0,-1)] 
        m , n = len(rooms)  , len(rooms[0])

        queue = deque() 
        visited = set() 
        step = 0 

        # 首先第一輪是把所有門都加入 deque , 再開始走BFS 
        for i in range(m):
            for j in range(n): 
                if rooms[i][j] == 0 : 
                    queue.append((i,j))
                    visited.add((i,j)) 

        # 開始走 BFS , 同時紀錄步數.

        while queue: 

            size = len(queue) 
            step += 1 
            # 這一輪只能走 size 步 
            for _ in range(size): 

                x , y = queue.popleft() 
                # 開始走四面八方,只要是空房間 (INF) 就能加入
                for dx , dy in DIRS : 
                    nx , ny = x + dx , y + dy 
                    # 在不超出棋盤格的情況下,如果走到空房間,就加入 queue 準備走下一輪,同時將當前步數紀錄進去
                    if 0 <= nx < m and 0 <= ny < n and rooms[nx][ny] == INF and (nx,ny) not in visited : 
                        queue.append((nx,ny)) 
                        visited.add((nx,ny)) 
                        rooms[nx][ny] = step 
        
        return 


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
