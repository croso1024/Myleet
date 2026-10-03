"""
    題意 :
    給定一個 m x n 的網格 grid。每個格子是 '1'(陸地) 或 '0'(水)。
    回傳島嶼的數量。

    一座島由上下左右相鄰的陸地連成。斜對角不算相鄰。
    網格四邊的外側都視為水。

    LeetCode 200 · Medium
    URL : https://leetcode.com/problems/number-of-islands/

    Example :
    grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"],
    ] -> 1
    grid = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"],
    ] -> 3

    Constraint :
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] 是 '0' 或 '1'

    思路 :
    這一題是標準的Graph展開, 中間用 seen 去儲存看過的位置.
    每一次走到一個島嶼就展開 , 展開到看過島嶼上所有陸地位置. 
    全部掃一輪看走過幾次沒見過的島嶼就是答案 

    複雜度 : 
    - 每一個島嶼一定會走過一次 O(m x n) , 空間上有個 seen 儲存看過的島嶼 O(m x n) 

    Trade-off :

"""

import copy
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        # Given 1 <= m,n <= 300 
        m , n = len(grid) , len(grid[0])
        seen = set() 
        islands = 0 

        # Traverse island by depth-first search
        def _traverse_island( i,j ): 
            stack = []
            stack.append((i,j)) 
            while stack : 

                node = stack.pop() 
                cur_x , cur_y = node 

                if cur_x + 1 < m and grid[cur_x+1][cur_y] == "1" and (cur_x+1,cur_y) not in seen : 
                    stack.append((cur_x+1,cur_y)) 
                    seen.add((cur_x+1,cur_y))
                
                if cur_x - 1 >= 0 and grid[cur_x+-1][cur_y] == "1" and (cur_x-1,cur_y) not in seen : 
                    stack.append((cur_x-1,cur_y)) 
                    seen.add((cur_x-1,cur_y))

                if cur_y + 1 < n  and grid[cur_x][cur_y+1] == "1" and (cur_x,cur_y+1) not in seen : 
                    stack.append((cur_x , cur_y+1))
                    seen.add((cur_x,cur_y+1))

                if cur_y - 1 >= 0  and grid[cur_x][cur_y-1] == "1" and (cur_x,cur_y-1) not in seen : 
                    stack.append((cur_x , cur_y-1))
                    seen.add((cur_x,cur_y-1))


        for i in range(m): 
            for j in range(n): 
                if grid[i][j] == "1" and (i,j) not in seen : 
                    islands += 1 
                    _traverse_island(i,j) 
        
        return islands






if __name__ == "__main__":
    c = Solution()

    # (grid, 預期, 說明)
    # 每題都複製一份 grid,避免上一題把格子改掉
    test_set = [
        (
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ],
            1,
            "官方範例:整片陸地連成一座島",
        ),
        (
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ],
            3,
            "官方範例:三座分開的島",
        ),
        ([["1"]], 1, "邊界:單一陸地"),
        ([["0"]], 0, "邊界:單一水域"),
        (
            [["1", "0"], ["0", "1"]],
            2,
            "斜對角不算相鄰",
        ),
        ([["1", "0", "1", "0", "1"]], 3, "只有一列,陸地被水隔開"),
        ([["1"], ["0"], ["1"]], 2, "只有一行,陸地被水隔開"),
        ([["1", "1"], ["1", "1"]], 1, "2x2 全是陸地,連成一座"),
        ([["0", "0"], ["0", "0"]], 0, "2x2 全是水"),
        (
            [
                ["1", "1", "1"],
                ["1", "0", "1"],
                ["1", "1", "1"],
            ],
            1,
            "中間是水,外圈仍然相連",
        ),
        (
            [
                ["1", "0", "1"],
                ["1", "0", "1"],
                ["0", "0", "0"],
            ],
            2,
            "中間一條水把左右切開",
        ),
        (
            [["1", "1", "0"], ["0", "0", "1"]],
            2,
            "兩列,斜對角的陸地分開計算",
        ),
    ]

    for grid, expected, note in test_set:
        result = c.numIslands(copy.deepcopy(grid))
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       expected={expected} | got={result}")
