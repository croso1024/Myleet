"""
    題意 :
    給定一個 m x n 的字母盤 board,以及一個單字 word。
    若 word 能由盤面上上下左右相鄰的格子依序拼出來,回傳 True,否則 False。

    同一個格子在一條路徑裡不能重複使用。斜角不相鄰。

    LeetCode 79 · Medium
    URL : https://leetcode.com/problems/word-search/

    Example :
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED" -> True
    word = "SEE"    -> True
    word = "ABCB"   -> False

    Constraint :
    m == board.length
    n == board[i].length
    1 <= m, n <= 6
    1 <= word.length <= 15
    board 與 word 只含大小寫英文字母

    思路 :
    這一題看起來是一個 DFS 展開的問題. 
    "word" 的就是當前還需要被填滿的目標 , 而所在的位置以及已經走過的格子就是Path, 
    因為不能走那些已經走過的格子 , 因此應該要有一個 hashset 去Keep走過的那些格子. 每走到一格就看周圍四格, 有沒有出現在下一個字母但又沒走過的繼續走. 
    如果找到一組解就可以直接Return , 否則False

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List , Set , Tuple 
import copy


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        answer = False
        # Given  1 <= m , n 
        m , n = len(board) , len(board[0])

        reversed_word_list = [ word[i] for i in range(len(word)-1 ,-1,-1)]

        def _backtracking( i : int , j : int , path_set : Set[Tuple[int,int]] , rest : List[str] ) : 
            nonlocal answer 
            # early stop 
            if answer : return 
            if len(rest) == 0  : 
                answer = True 
                return 
            # 檢查周圍這四格有沒有出現字串的尾巴內容 , 有的話繼續展開
            if i + 1  < m  and (i+1,j) not in path_set and board[i+1][j] == rest[-1] :  
                path_set.add((i+1,j)) 
                char = rest.pop() 
                _backtracking( i+1 , j , path_set=path_set , rest = rest) 
                rest.append(char) 
                path_set.remove((i+1,j)) 
            
            if i - 1 >= 0 and (i-1,j) not in path_set and board[i-1][j] == rest[-1] : 
                path_set.add((i-1,j)) 
                char = rest.pop() 
                _backtracking( i-1 , j , path_set=path_set , rest = rest) 
                rest.append(char) 
                path_set.remove((i-1,j))
            
            if j + 1 < n and (i,j+1) not in path_set and board[i][j+1] == rest[-1] : 
                path_set.add((i,j+1)) 
                char = rest.pop() 
                _backtracking( i , j+1 , path_set=path_set , rest = rest) 
                rest.append(char) 
                path_set.remove((i,j+1))
            

            if j - 1 >= 0 and (i,j-1) not in path_set and board[i][j-1] == rest[-1] : 
                path_set.add((i,j-1)) 
                char = rest.pop() 
                _backtracking( i , j-1 , path_set=path_set , rest = rest) 
                rest.append(char) 
                path_set.remove((i,j-1))

        for i in range(m) : 
            for j in range(n): 
                # 只有命中第一格後才開始
                if board[i][j] == reversed_word_list[-1] : 
                    tmp = reversed_word_list.pop()
                    _backtracking(i,j , path_set={(i,j)} , rest=reversed_word_list)
                    reversed_word_list.append(tmp) 
        
        return answer 




if __name__ == "__main__":
    c = Solution()

    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]

    # (board, word, 預期, 說明)
    # 每題都複製一份 board,避免上一題把格子改掉
    test_set = [
        (board, "ABCCED", True, "官方範例,走完整條蛇形"),
        (board, "SEE", True, "官方範例,從中間開始"),
        (board, "ABCB", False, "官方範例,同一個 B 不能用兩次"),
        ([["A"]], "A", True, "邊界:單一格子,命中"),
        ([["A"]], "B", False, "邊界:單一格子,不命中"),
        ([["a"]], "A", False, "大小寫不同"),
        ([["A", "B", "C"]], "ABC", True, "只有一列"),
        ([["A", "B", "C"]], "CBA", True, "只有一列,反向"),
        ([["A", "B", "C"]], "AC", False, "跳過中間格子不算相鄰"),
        ([["A"], ["B"], ["C"]], "ABC", True, "只有一行"),
        ([["A", "A"]], "AA", True, "相鄰的相同字母"),
        ([["A", "A"]], "AAA", False, "格子不夠,不能重複踩"),
        ([["A", "B"], ["C", "D"]], "ABA", False, "回頭會踩到用過的 A"),
        (
            [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]],
            "AAB",
            True,
            "起點很多,要換起點才走得通",
        ),
        (board, "ABCESEEDASFC", True, "字比整張盤的格子還多"),
    ]

    for grid, word, expected, note in test_set:
        result = c.exist(copy.deepcopy(grid), word)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       word={word} | expected={expected} | got={result}")
