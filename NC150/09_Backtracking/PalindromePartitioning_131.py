"""
    題意 :
    給定一個字串 s,把它切成若干段,使每一段都是迴文。
    回傳所有這樣的切法。

    每一種切法裡,片段的順序就是它們在原字串裡的順序。
    切法之間的順序不限。

    LeetCode 131 · Medium
    URL : https://leetcode.com/problems/palindrome-partitioning/

    Example :
    s = "aab" -> [["a","a","b"],["aa","b"]]
    s = "a"   -> [["a"]]

    Constraint :
    1 <= s.length <= 16
    s 只含小寫英文字母

    思路 :

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        pass


def canon(parts: List[List[str]]):
    """切法之間的順序不影響對錯;每一種切法內部的片段順序要保留。"""
    if parts is None:
        return None
    return sorted(tuple(group) for group in parts)


if __name__ == "__main__":
    c = Solution()

    # (輸入, 預期輸出, 說明) —— 只忽略切法彼此的順序
    test_set = [
        ("aab", [["a", "a", "b"], ["aa", "b"]], "官方範例"),
        ("a", [["a"]], "官方範例:單一字母"),
        ("aa", [["a", "a"], ["aa"]], "兩種切法,整段也是迴文"),
        ("ab", [["a", "b"]], "整段不是迴文,只能逐字切"),
        ("aba", [["a", "b", "a"], ["aba"]], "奇數長度的整段迴文"),
        (
            "aaa",
            [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]],
            "每個子字串都是迴文",
        ),
        (
            "abba",
            [["a", "b", "b", "a"], ["a", "bb", "a"], ["abba"]],
            "中間兩字成段,或整段",
        ),
        ("abc", [["a", "b", "c"]], "沒有任何更長的迴文片段"),
        ("bb", [["b", "b"], ["bb"]], "兩個相同字母"),
        (
            "aaaa",
            [
                ["a", "a", "a", "a"],
                ["a", "a", "aa"],
                ["a", "aa", "a"],
                ["aa", "a", "a"],
                ["a", "aaa"],
                ["aaa", "a"],
                ["aa", "aa"],
                ["aaaa"],
            ],
            "四個相同字母,每一種子字串都是迴文",
        ),
    ]

    for s, expected, note in test_set:
        result = c.partition(s)
        passed = canon(result) == canon(expected)
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       input={s!r}")
        print(f"       expected={expected}")
        print(f"       got     ={result}")
