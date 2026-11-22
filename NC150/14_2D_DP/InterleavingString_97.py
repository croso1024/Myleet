"""
    題意 :
    給定三個字串 s1、s2、s3,判斷 s3 是否由 s1 與 s2「交錯 (interleaving)」組成。

    交錯的定義:
    將 s 切成 n 個非空子字串、t 切成 m 個非空子字串:
        s = s_1 + s_2 + ... + s_n
        t = t_1 + t_2 + ... + t_m
        |n - m| <= 1
    則 s 與 t 的交錯為
        s_1 + t_1 + s_2 + t_2 + ...   或   t_1 + s_1 + t_2 + s_2 + ...
    (a + b 表示字串串接)

    Follow up :
    - 能不能只用 O(s2.length) 的額外空間?

    LeetCode 97 · Medium
    URL : https://leetcode.com/problems/interleaving-string/

    Example :
    s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac" -> True
    s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc" -> False
    s1 = "",      s2 = "",      s3 = ""           -> True

    Constraint :
    0 <= s1.length, s2.length <= 100
    0 <= s3.length <= 200
    s1、s2、s3 皆只含小寫英文字母

    思路 :

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        pass


if __name__ == "__main__":
    c = Solution()

    # (s1, s2, s3, 預期, 說明)
    test_set = [
        ("aabcc", "dbbca", "aadbbcbcac", True, "官方範例:可交錯"),
        ("aabcc", "dbbca", "aadbbbaccc", False, "官方範例:不可交錯"),
        ("", "", "", True, "官方範例:三個都是空字串"),
        ("", "abc", "abc", True, "邊界:s1 為空,s3 等於 s2"),
        ("abc", "", "abc", True, "邊界:s2 為空,s3 等於 s1"),
        ("", "abc", "abd", False, "邊界:s1 為空,s3 與 s2 不同"),
        ("a", "b", "abc", False, "s3 長度大於 s1 + s2"),
        ("abc", "d", "ab", False, "s3 長度小於 s1 + s2"),
        ("a", "b", "ab", True, "最小的交錯:s1 在前"),
        ("a", "b", "ba", True, "最小的交錯:s2 在前"),
        ("ab", "cd", "acdb", True, "s1 的字元被 s2 整段隔開"),
        ("ab", "cd", "adcb", False, "d 出現在 c 之前,違反 s2 內部順序"),
        ("abc", "def", "acbdef", False, "字元組成相同,但 c 出現在 b 之前"),
        ("aa", "bb", "abbb", False, "長度相同,但字元組成與 s1 + s2 不同"),
        ("aa", "bb", "baab", True, "s2 的字元包住 s1 的字元"),
        ("aaa", "aaa", "aaaaaa", True, "所有字元都相同"),
        ("ab", "ac", "acab", True, "兩個字串的開頭字元相同"),
    ]

    for s1, s2, s3, expected, note in test_set:
        result = c.isInterleave(s1, s2, s3)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       s1={s1!r} s2={s2!r} s3={s3!r}")
        print(f"       expected={expected}")
        print(f"       got     ={result}")
