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
    dp[i][j] 定義成「word1 的前 i 個字,變成 word2 的前 j 個字,最少要幾次操作」。
    和 1143 一樣是雙序列的表,差別在格子裡放的是代價,不是長度。

    邊界先填:
    dp[i][0] = i,把 word1 的前 i 個字刪光。
    dp[0][j] = j,從空字串插入 word2 的前 j 個字。

    內部每一格看 word1[i-1] 和 word2[j-1]:
    - 兩個字相同,不用操作,直接沿對角線拿 dp[i-1][j-1]。
    - 不同,三種操作都試一次,取最小再加 1:
      刪掉 word1 這個字 -> dp[i-1][j]
      插入 word2 這個字 -> dp[i][j-1]
      把 word1 這個字換成 word2 的 -> dp[i-1][j-1]

    1143 不相等時是取左、上的 max。
    這裡不相等時是三種操作的 min 再加一;相等時不付代價,只沿對角線。

    複雜度 :
    時間複雜度 O(m * n),表上每一格算一次。
    空間複雜度 O(m * n)。

    Trade-off :
    轉移只看上一列和這一列的左邊,可以壓成兩列,甚至一列加一個對角暫存,
    空間降到 O(min(m, n))。
    這輪先留完整的表,和 1143 的格子對照時比較不會搞混索引。

"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        # dp[i][j]: word1 前 i 個字 -> word2 前 j 個字的最少操作數
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    delete_one = dp[i - 1][j]
                    insert_one = dp[i][j - 1]
                    replace_one = dp[i - 1][j - 1]
                    dp[i][j] = 1 + min(delete_one, insert_one, replace_one)

        return dp[m][n]


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
