"""
    題意 :
    給定一個 m x n 的棋盤 board。格子是 'X' 或 'O'。
    把被 'X' 上下左右圍住的區域裡,所有 'O' 改成 'X'。

    有任何一格貼著棋盤邊界的區域不算被圍住,那些 'O' 留著。
    斜角不算相連。

    直接改 board,不要回傳新的棋盤。

    LeetCode 130 · Medium
    URL : https://leetcode.com/problems/surrounded-regions/

    Example :
    board = [
      ["X","X","X","X"],
      ["X","O","O","X"],
      ["X","X","O","X"],
      ["X","O","X","X"],
    ] -> [
      ["X","X","X","X"],
      ["X","X","X","X"],
      ["X","X","X","X"],
      ["X","O","X","X"],
    ]
    board = [["X"]] -> [["X"]]

    Constraint :
    m == board.length
    n == board[i].length
    1 <= m, n <= 200
    board[i][j] 是 'X' 或 'O'

    思路 :
    這一題應該是標準BFS,在走的過程中紀錄一下目前踩過的點位. 
    如果這一趟BFS走不出棋盤(無法走到邊界),那就要整塊翻"X" ,這一題要求直接改Board,
    所以時間複雜度基本上就是所有格子走一輪O(N),以及在走的過程中儲存的路徑最多也是O(N)

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

import copy
from typing import List,Set,Tuple
from collections import deque 

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m , n = len(board) , len(board[0])
        # 從 i,j 開始走, BFS擴張並記錄走過的"O", 最終回傳boolean說明有沒有碰到邊界 
        def bfs(i,j) -> Tuple[bool, Set[Tuple[int,int]]] :  
            DIRS = [(0,1),(0,-1),(1,0),(-1,0)] 
            is_touch_boundary = False 
            visisted = set() 
            queue = deque()
            queue.append((i,j))
            visisted.add((i,j)) 
            while queue : 

                x,y = queue.popleft()
                # 判斷是否到達邊界 
                if x == 0 or x == m-1  or y == 0 or y == n-1 : is_touch_boundary = True 
                
                for dx , dy in DIRS : 

                    nx = x + dx 
                    ny = y + dy

                    if  0 <= nx < m and 0 <= ny < n and board[nx][ny] == "O" and (nx,ny) not in visisted : 
                        queue.append((nx,ny))
                        visisted.add((nx,ny)) 
            
            return is_touch_boundary , visisted
    
        search_space = set([(i,j) for i in range(m) for j in range(n) if board[i][j] == "O"])
        while search_space : 

            i,j = search_space.pop()
            is_touch_boundary , visisted = bfs(i,j)
            # 沒碰到邊界,那代表這輪visited 的節點都要翻黑
            if not is_touch_boundary : 

                for (x,y) in visisted : 
                    if (x,y) in search_space : search_space.remove((x,y)) 
                    board[x][y] = "X"
            # 如果有碰到邊界 ,這一輪的都不用再拜訪了 , 保留在棋盤上 
            else : 
                for (x,y) in visisted : 
                    if (x,y) in search_space : search_space.remove((x,y)) 
        return 
            
        
        


        




if __name__ == "__main__":
    c = Solution()

    official = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
    official_expected = [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"],
    ]

    # (board, 預期, 說明)
    # 這一題改的是傳進去的棋盤本身,每次都複製一份再比對
    test_set = [
        (official, official_expected, "官方範例:中間的 O 被圍住,底邊的 O 留著"),
        ([["X"]], [["X"]], "官方範例:只有一格 X"),
        ([["O"]], [["O"]], "邊界:只有一格 O,貼著邊界"),
        (
            [["O", "O"], ["O", "O"]],
            [["O", "O"], ["O", "O"]],
            "四格都貼邊界,沒有被圍住的區域",
        ),
        (
            [["X", "X", "X"], ["X", "O", "X"], ["X", "X", "X"]],
            [["X", "X", "X"], ["X", "X", "X"], ["X", "X", "X"]],
            "正中間一格 O 被 X 圍住",
        ),
        (
            [["X", "O", "X"], ["X", "O", "X"], ["X", "O", "X"]],
            [["X", "O", "X"], ["X", "O", "X"], ["X", "O", "X"]],
            "直向的 O 接到上下邊界,整條留著",
        ),
        (
            [["O", "X", "O"], ["X", "O", "X"], ["O", "X", "O"]],
            [["O", "X", "O"], ["X", "X", "X"], ["O", "X", "O"]],
            "正中間的 O 只跟邊界的 O 斜角相鄰,要翻掉",
        ),
        (
            [
                ["X", "X", "X", "X"],
                ["X", "O", "O", "X"],
                ["X", "O", "O", "X"],
                ["X", "X", "X", "X"],
            ],
            [
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
            ],
            "內部 2x2 的 O 整塊被圍住",
        ),
        (
            [
                ["X", "X", "X", "X"],
                ["X", "O", "O", "X"],
                ["X", "O", "O", "O"],
                ["X", "X", "X", "X"],
            ],
            [
                ["X", "X", "X", "X"],
                ["X", "O", "O", "X"],
                ["X", "O", "O", "O"],
                ["X", "X", "X", "X"],
            ],
            "內部的 O 接到右邊邊界,整塊留著",
        ),
        (
            [
                ["X", "O", "X", "X"],
                ["X", "X", "O", "X"],
                ["X", "O", "X", "X"],
                ["X", "X", "X", "O"],
            ],
            [
                ["X", "O", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "X", "X", "O"],
            ],
            "兩格被圍住的 O 翻掉,貼邊的 O 留著",
        ),
    ]

    for board, expected, note in test_set:
        snapshot = copy.deepcopy(board)
        c.solve(snapshot)
        passed = snapshot == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       expected={expected}")
        print(f"       got     ={snapshot}")
