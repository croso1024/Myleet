"""
    題意 :
    有一座 m x n 的島。左邊與上邊緊鄰太平洋,右邊與下邊緊鄰大西洋。
    heights[r][c] 是格子 (r, c) 的高度。

    雨水只能往上下左右流,而且只能流進高度小於或等於自己的鄰居。
    靠海的格子可以直接把水送進那一邊的海。

    回傳所有雨水能同時流到兩片海的座標 [r, c]。
    回傳順序不限。

    LeetCode 417 · Medium
    URL : https://leetcode.com/problems/pacific-atlantic-water-flow/

    Example :
    heights = [
      [1,2,2,3,5],
      [3,2,3,4,4],
      [2,4,5,3,1],
      [6,7,1,4,5],
      [5,1,1,2,4],
    ] -> [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
    heights = [[1]] -> [[0,0]]

    Constraint :
    m == heights.length
    n == heights[r].length
    1 <= m, n <= 200
    0 <= heights[r][c] <= 10^5

    思路 :
    這一題要找出哪些格子的水可以順著高度留入太平洋與大西洋.
    Naive的解決方案就是每一格嘗試往下流,看看能不能碰到兩個邊. 
    一個 Grid[i][j] 是否屬於某一個洋 : 
    Pacific Ocean : i=0 or j=0  
    Atlantic Ocean : i=m-1 or j=n-1

    最Naive Solution, 就是N個格字每一個格子都展開一次BFS, 每一次展開最多走N格. 
    因此時間複雜度為 O(N^2) , 這一題的 N 是 200x200 = 40000 = 4 * 10^4, N^2可能會炸掉. 
    所以不能每一組答案都走過一次. 
    一個失敗的組裡面,走過的格子是否必然失敗!? 
    
    思考過程中冒出來的另一個想法. 
    我們從所有大西洋的塊長出去,看看大西洋往上流可以擴張到哪些格子. 
    再做一次同樣的流程從太平洋做一次. 最後 , 大西洋和太平洋往上流能交集到的格子就是答案. 

    複雜度 : 
    大西洋,太平洋分別都只需要做一輪BFS, 走最多N格並儲存, 
    完成後取交集最多也是O(N)
    因此時間複雜度空間複雜度都是 O(N)

    Trade-off :

"""

import copy
from typing import List , Literal, Set , Tuple
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m , n = len(heights) , len(heights[0])
        DIRS = [(0,1),(0,-1),(1,0),(-1,0)]

        def collect_reachable_cells(ocean : Literal["pacific","atlantic"] )-> Set[Tuple[int,int]] : 
            visited = set() 
            queue = deque()
            if ocean == "pacific": 
                for i in range(1,m):queue.append((i,0)) 
                for j in range(1,n):queue.append((0,j))
                queue.append((0,0)) 
            elif ocean == "atlantic" : 
                for i in range(m-1):queue.append((i,n-1))
                for j in range(n-1):queue.append((m-1,j)) 
                queue.append((m-1,n-1)) 
            
            for (x,y) in queue: visited.add((x,y))
            
            while queue : 

                x,y = queue.popleft() 
                for dx , dy in DIRS : 
                    nx , ny = x+dx , y+dy 
                    # 要能流過去的條件就是 , 下一個高度>=當前高度: 
                    if  0 <= nx < m and  0 <= ny < n and (nx,ny) not in visited and heights[nx][ny] >= heights[x][y]: 
                        queue.append((nx,ny)) 
                        visited.add((nx,ny)) 
            # 全部走完之後, 回傳從這片海洋出發可以經過的cells 
            return visited 
        
        visited_from_pacific = collect_reachable_cells(ocean="pacific") 
        visited_from_atlanic = collect_reachable_cells(ocean="atlantic")

        return list( visited_from_pacific.intersection(visited_from_atlanic ))



                    
                    
                
                


        



def canon(cells):
    """座標的回傳順序不影響對錯。"""
    if cells is None:
        return None
    return sorted(tuple(cell) for cell in cells)


if __name__ == "__main__":
    c = Solution()

    official = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]

    # (heights, 預期, 說明)
    # 每次呼叫都複製 heights,實作若改到格子不會留到下一題
    test_set = [
        (
            official,
            [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]],
            "官方範例:雨水從高處分向兩片海",
        ),
        ([[1]], [[0, 0]], "官方範例:單一格子同時靠兩片海"),
        ([[0]], [[0, 0]], "邊界:高度是 0 的單一格子"),
        (
            [[1, 2, 3]],
            [[0, 0], [0, 1], [0, 2]],
            "只有一列,每一格同時靠太平洋與大西洋",
        ),
        (
            [[1], [2], [3]],
            [[0, 0], [1, 0], [2, 0]],
            "只有一行,每一格同時靠左右兩片海",
        ),
        (
            [[1, 1], [1, 1]],
            [[0, 0], [0, 1], [1, 0], [1, 1]],
            "高度全相同,水可以平流到任何一邊",
        ),
        (
            [[1, 3], [2, 2]],
            [[0, 1], [1, 0], [1, 1]],
            "左上角四周較高,水流不出去",
        ),
        (
            [[5, 5], [5, 1]],
            [[0, 0], [0, 1], [1, 0]],
            "右下角是洼地,只靠得到大西洋",
        ),
        (
            [[2, 1], [1, 2]],
            [[0, 0], [0, 1], [1, 0], [1, 1]],
            "對角較高,四格都能到兩片海",
        ),
        (
            [[10, 10, 10], [10, 1, 10], [10, 10, 10]],
            [
                [0, 0], [0, 1], [0, 2],
                [1, 0], [1, 2],
                [2, 0], [2, 1], [2, 2],
            ],
            "正中間被較高的格子圍住,水出不去",
        ),
    ]

    for heights, expected, note in test_set:
        result = c.pacificAtlantic(copy.deepcopy(heights))
        passed = canon(result) == canon(expected)
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       expected={expected}")
        print(f"       got     ={result}")
