"""
    題意 :
    給定兩個字串 word1 與 word2。
    把 word1 變成 word2,每次可以插入、刪除或替換一個字母。
    回傳最少需要幾次操作。

    LeetCode 72 · Medium
    URL : https://leetcode.com/problems/edit-distance/

    Example :
    word1 = "horse",     word2 = "ros"       -> 3
    word1 = "intention", word2 = "execution" -> 5

    Constraint :
    0 <= word1.length, word2.length <= 500
    word1 與 word2 只含小寫英文字母

    思路 :

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        pass


if __name__ == "__main__":
    c = Solution()

    # (word1, word2, 預期, 說明)
    test_set = [
        ("horse", "ros", 3, "官方範例:horse -> ros"),
        ("intention", "execution", 5, "官方範例:intention -> execution"),
        ("", "", 0, "邊界:兩串都是空的"),
        ("a", "", 1, "刪掉唯一的字母"),
        ("", "a", 1, "插入一個字母"),
        ("a", "a", 0, "已經相同"),
        ("a", "b", 1, "替換一個字母"),
        ("abc", "abc", 0, "整串相同"),
        ("kitten", "sitting", 3, "替換、替換、插入"),
        ("sea", "eat", 2, "刪掉 s,插入 t"),
    ]

    for word1, word2, expected, note in test_set:
        result = c.minDistance(word1, word2)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       word1={word1} word2={word2} | expected={expected} | got={result}")
