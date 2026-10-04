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
    這一題的想法會是BFS去算從爛橘子擴散到所有好橘子的路線. 
    但也可以想成從好橘子到壞橘子的最遠路徑或是其實無法抵達. 
    題目的一個點是在壞橘子可能一開始就有很多顆. 
    所以我的想法是要先蒐集所有壞橘子的位置. 然後一口氣走BFS去模擬所有壞橘子開始擴散的狀況. 
    BFS過程去檢查是不是所有好橘子都已經被汙染. 如果是則結束並回傳時間. 否則就是不會全壞

    edge case : 一開始就沒有好橘子 , 答案就是0 , 一開始就沒有壞橘子 , 答案是 -1 

    複雜度 : 
    - 時間複雜度 : 所有節點走一次O(N) , 
    - 空間 : O(N)
    這一題有個陷阱,就是最終答案的分鐘數, 需要考慮到 
    "最遠的好橘子被汙染的時間為T , 但因為好橘子被汙染因此可以展開下一輪BFS,這會讓最終時間變成T+1"
    故回圈判斷需要多一個好橘子還有,才繼續擴散

    Trade-off :

"""

import copy
from typing import List

from collections import deque 
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # Step.1 蒐集壞橘子和好橘子的位置
        fresh  = set()
        bad  =set()

        m , n = len(grid) , len(grid[0])

        for i in range(m): 
            for j in range(n): 
                if grid[i][j] == 1 : 
                    fresh.add((i,j))
                elif grid[i][j] == 2 : 
                    bad.add((i,j))
        
        if len(fresh) == 0 : return 0 
        if len(bad) == 0 : return -1 


        # Step.2 以所有壞橘子位置為起點,開始走BFS
        queue = deque()
        visited = set()
        for (i,j) in bad : 
            queue.append((i,j)) 
            visited.add((i,j)) 
        
        # 第0分鐘 
        minutes = 0 
        while queue and len(fresh) : 
            # 先記錄下BFS這一輪開始時 , 有幾個爛橘子要出發 
            size = len(queue) 

            for _ in range(size): 

                # 取出一顆壞橘子,開始擴散
                i , j  = queue.popleft()  

                if i + 1 < m and (i+1,j) not in visited : 
                    visited.add((i+1,j))
                    # 若有好橘子則污染,並加入queue
                    if (i+1,j) in fresh :  
                        fresh.remove((i+1,j))
                        queue.append((i+1,j)) 
                
                if i - 1 >= 0 and (i-1,j) not in visited : 
                    visited.add((i-1,j))
                    # 若有好橘子則污染,並加入queue
                    if (i-1,j) in fresh :  
                        fresh.remove((i-1,j))
                        queue.append((i-1,j)) 
                
                if j + 1 < n and (i,j+1) not in visited : 
                    visited.add((i,j+1))
                    # 若有好橘子則污染,並加入queue
                    if (i,j+1) in fresh :  
                        fresh.remove((i,j+1))
                        queue.append((i,j+1)) 
                
                if j - 1 >= 0 and (i,j-1) not in visited : 
                    visited.add((i,j-1))
                    # 若有好橘子則污染,並加入queue
                    if (i,j-1) in fresh :  
                        fresh.remove((i,j-1))
                        queue.append((i,j-1)) 
            
            minutes += 1 

        # BFS 結束後,如果好橘子還存在就是 -1 , 不存在則回傳分鐘數 

        if len(fresh) > 0 : return -1 
        return minutes 


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
