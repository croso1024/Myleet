"""
    題意 :
    給定一個 m x n 的字母盤 board,以及一組單字 words。
    回傳所有能在盤面上拼出來的單字。

    每個單字必須由上下左右相鄰的格子依序拼出。斜角不相鄰。
    同一個格子在一條路徑裡不能重複使用。
    words 裡的單字彼此不重複。盤面上出現多次的單字,答案裡只留一次。

    回傳順序不限。

    LeetCode 212 · Hard
    URL : https://leetcode.com/problems/word-search-ii/

    Example :
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words = ["oath","pea","eat","rain"] -> ["eat","oath"]

    board = [["a","b"],["c","d"]]
    words = ["abcb"] -> []

    Constraint :
    m == board.length
    n == board[i].length
    1 <= m, n <= 12
    board[i][j] 是小寫英文字母
    1 <= words.length <= 3 * 10^4
    1 <= words[i].length <= 10
    words[i] 由小寫英文字母組成
    words 中的字串互異

    思路 :

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

import copy
from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        pass


def canon(words):
    """單字的回傳順序不影響對錯。"""
    if words is None:
        return None
    return sorted(words)


if __name__ == "__main__":
    c = Solution()

    official = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ]

    # (board, words, 預期, 說明)
    # 每次呼叫都複製 board,上一題改過的格子不會留到下一題
    test_set = [
        (
            official,
            ["oath", "pea", "eat", "rain"],
            ["eat", "oath"],
            "官方範例:pea 不在盤上,rain 的字母不相鄰",
        ),
        (
            [["a", "b"], ["c", "d"]],
            ["abcb"],
            [],
            "官方範例:路徑走不回去",
        ),
        ([["a"]], ["a"], ["a"], "邊界:單一格子,命中"),
        ([["a"]], ["b"], [], "邊界:單一格子,不命中"),
        ([["a", "a"]], ["aa"], ["aa"], "相鄰的相同字母"),
        ([["a", "a"]], ["aaa"], [], "格子不夠,同一個格子不能踩兩次"),
        (
            [["a", "b"], ["c", "d"]],
            ["ad"],
            [],
            "斜角不算相鄰",
        ),
        (
            [["a", "b"], ["c", "d"]],
            ["ab", "abc"],
            ["ab"],
            "較短的字在盤上,多出來的字母接不下去",
        ),
        (
            [["o", "a"], ["h", "t"]],
            ["oa", "oat", "oath"],
            ["oa", "oat", "oath"],
            "同一個前綴的三個字都在盤上:o-a-t-h",
        ),
        (
            [["a", "b", "c"]],
            ["ac", "abc", "cba"],
            ["abc", "cba"],
            "只有一列:相鄰的字可以正向或反向,跳格不行",
        ),
        (
            [["a", "b", "a"], ["b", "a", "b"]],
            ["aba"],
            ["aba"],
            "盤上有多條路徑,答案只留一次",
        ),
        (
            [
                ["a", "b", "c"],
                ["d", "e", "f"],
                ["g", "h", "i"],
            ],
            ["abeh", "abcf", "xyz"],
            ["abeh", "abcf"],
            "兩個字都找得到,第三個字完全不在盤上",
        ),
    ]

    for board, words, expected, note in test_set:
        result = c.findWords(copy.deepcopy(board), list(words))
        passed = canon(result) == canon(expected)
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       words={words}")
        print(f"       expected={expected}")
        print(f"       got     ={result}")
