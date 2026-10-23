"""
    題意 :
    給定一個 m x n 的二進位網格 grid。
    一座島由上下左右相鄰的 1(陸地)連成。斜對角不算相鄰。
    網格四邊的外側都視為水。

    島的面積是這座島上 1 的格子數。
    回傳最大的島面積。沒有島就回傳 0。

    LeetCode 695 · Medium
    URL : https://leetcode.com/problems/max-area-of-island/

    Example :
    grid = [
      [0,0,1,0,0,0,0,1,0,0,0,0,0],
      [0,0,0,0,0,0,0,1,1,1,0,0,0],
      [0,1,1,0,1,0,0,0,0,0,0,0,0],
      [0,1,0,0,1,1,0,0,1,0,1,0,0],
      [0,1,0,0,1,1,0,0,1,1,1,0,0],
      [0,0,0,0,0,0,0,0,0,0,1,0,0],
      [0,0,0,0,0,0,0,1,1,1,0,0,0],
      [0,0,0,0,0,0,0,1,1,0,0,0,0],
    ] -> 6
    grid = [[0,0,0,0,0,0,0,0]] -> 0

    Constraint :
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 50
    grid[i][j] 是 0 或 1

    思路 :
    蠻直覺就是走BFS , 順便在BFS的過程中算最大的島嶼面積. 
    時間複雜度 O(N), 需要每一個格子走一次, 空間複雜度 Worse Case O(N),需要儲存踏上的島嶼以及後續要拜訪的島嶼

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

import copy
from typing import List , Set , Tuple 
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m , n = len(grid) , len(grid[0])

        def breath_first_search(i,j,visited : Set[Tuple[int,int]]): 
            nonlocal maximum_area
            DIRS = ((-1,0),(1,0),(0,-1),(0,1)) 
            area = 0
            queue = deque()
            queue.append((i,j))  
            visited.add((i,j)) 
            while queue : 
                r,c = queue.popleft() 

                for dr , dc in DIRS : 
                    nr , nc = r + dr , c + dc 
                    if 0 <= nr < m and 0 <= nc <= n and grid[nr][nc] == 1 and (nr,nc) not in visited :
                        queue.append((nr,nc)) 
                        visited.add((nr,nc))

                area += 1 
            maximum_area = max(maximum_area , area) 
        visited : Set[Tuple[int,int]] = set()  
        maximum_area = 0
        for i in range(m):
            for j in range(n) : 
                if grid[i][j] == 1 and (i,j) not in visited : 
                    breath_first_search(i,j,visited)
        
        return maximum_area


# 嘗試DFS一組,每次展開一輪DFS就開始累加Counter , 直到外層後歸零
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m , n = len(grid) , len(grid[0])
        maximum_area = 0 
        area_counter = 0 
        visited : Set[Tuple[int,int]] = set() 
        DIRS = ((-1,0),(1,0),(0,-1),(0,1)) 

        def dfs(r,c,visited : Set[Tuple[int,int]])  : 
            nonlocal area_counter 
            area_counter += 1 
            for dr , dc in DIRS : 
                nr , nc = r + dr , c + dc 
                if (0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1) and \
                    (nr,nc) not in visited :
                    visited.add((nr,nc))
                    dfs(nr,nc ,visited=visited)
        
        for i in range(m):
            for j in range(n): 

                if grid[i][j] == 1 and (i,j) not in visited  : 
                    visited.add((i,j)) 
                    dfs(i,j,visited=visited) 
                    maximum_area = max(maximum_area , area_counter)
                    # Reset 
                    area_counter = 0 

        return maximum_area
            


if __name__ == "__main__":
    c = Solution()

    official = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ]

    # (grid, 預期, 說明)
    # 每次呼叫都複製 grid,實作若改到格子不會留到下一題
    test_set = [
        (official, 6, "官方範例:右邊那座島面積 6"),
        ([[0, 0, 0, 0, 0, 0, 0, 0]], 0, "官方範例:整列都是水"),
        ([[0]], 0, "邊界:單一格子是水"),
        ([[1]], 1, "邊界:單一格子是陸地"),
        ([[0, 0], [0, 0]], 0, "沒有陸地"),
        ([[1, 1], [1, 1]], 4, "四格連成一座島"),
        ([[1, 0], [0, 1]], 1, "斜對角不算相鄰,兩座面積都是 1"),
        ([[1, 1, 0, 1, 1, 1]], 3, "同一列被水切開,取較長的那座"),
        (
            [[1, 1, 0, 0], [1, 0, 0, 1], [0, 0, 1, 1]],
            3,
            "左右兩座島面積相同",
        ),
        (
            [[1, 0, 1], [1, 1, 1], [0, 1, 0]],
            6,
            "中間連通,六格都在同一座島",
        ),
    ]

    for grid, expected, note in test_set:
        result = c.maxAreaOfIsland(copy.deepcopy(grid))
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       expected={expected}")
        print(f"       got     ={result}")
