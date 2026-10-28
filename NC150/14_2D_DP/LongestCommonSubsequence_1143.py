"""
    題意 :
    給定兩個字串 text1 與 text2。回傳最長公共子序列的長度。
    子序列不必連續,但留下的字母必須保持原本的相對順序。
    沒有公共子序列就回傳 0。

    LeetCode 1143 · Medium
    URL : https://leetcode.com/problems/longest-common-subsequence/

    Example :
    text1 = "abcde", text2 = "ace" -> 3
    text1 = "abc",   text2 = "abc" -> 3
    text1 = "abc",   text2 = "def" -> 0

    Constraint :
    1 <= text1.length, text2.length <= 1000
    text1 與 text2 只含小寫英文字母

    思路 :

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        pass


if __name__ == "__main__":
    c = Solution()

    # (text1, text2, 預期, 說明)
    test_set = [
        ("abcde", "ace", 3, "官方範例:ace"),
        ("abc", "abc", 3, "官方範例:兩串相同"),
        ("abc", "def", 0, "官方範例:沒有共同字母"),
        ("a", "a", 1, "邊界:單字母相同"),
        ("a", "b", 0, "邊界:單字母不同"),
        ("abc", "c", 1, "共同字母在尾端"),
        ("abc", "ac", 2, "跳過中間的 b"),
        ("aggtab", "gxtxayb", 4, "gtab"),
        ("bsbininm", "jmjkbkjkv", 1, "只能取一個 b 或一個 m"),
    ]

    for text1, text2, expected, note in test_set:
        result = c.longestCommonSubsequence(text1, text2)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       text1={text1} text2={text2} | expected={expected} | got={result}")
