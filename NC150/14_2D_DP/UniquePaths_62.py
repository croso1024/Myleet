"""
    題意 :
    有一個 m 列 n 行的格子。機器人從左上角出發,每次只能往右或往下走一步。
    要走到右下角。回傳一共有幾條不同的路徑。

    LeetCode 62 · Medium
    URL : https://leetcode.com/problems/unique-paths/

    Example :
    m = 3, n = 7 -> 28
    m = 3, n = 2 -> 3

    Constraint :
    1 <= m, n <= 100

    思路 :

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        pass


if __name__ == "__main__":
    c = Solution()

    # (m, n, 預期, 說明)
    test_set = [
        (3, 7, 28, "官方範例:3x7"),
        (3, 2, 3, "官方範例:3x2,三條路"),
        (1, 1, 1, "邊界:已經在終點"),
        (1, 3, 1, "只有一列,只能一直往右"),
        (3, 1, 1, "只有一行,只能一直往下"),
        (2, 2, 2, "先右再下,或先下再右"),
        (2, 3, 3, "2x3"),
        (3, 3, 6, "3x3"),
        (7, 3, 28, "與 3x7 對稱"),
    ]

    for m, n, expected, note in test_set:
        result = c.uniquePaths(m, n)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       m={m} n={n} | expected={expected} | got={result}")
