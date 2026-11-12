"""
    題意 :
    給定一個只含小寫英文字母的字串 s。
    把 s 切成盡量多段,使得每個字母最多只出現在其中一段。
    各段依原順序接回去必須還原成 s。

    回傳每一段的長度。

    LeetCode 763 · Medium
    URL : https://leetcode.com/problems/partition-labels/

    Example :
    s = "ababcbacadefegdehijhklij" -> [9,7,8]
    s = "eccbbbbdec"               -> [10]

    Constraint :
    1 <= s.length <= 500
    s 只含小寫英文字母

    思路 :

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        pass


if __name__ == "__main__":
    c = Solution()

    # (s, 預期, 說明)
    test_set = [
        (
            "ababcbacadefegdehijhklij",
            [9, 7, 8],
            "官方範例:ababcbaca / defegde / hijhklij",
        ),
        ("eccbbbbdec", [10], "官方範例:e 與 c 都延伸到尾端,不能切"),
        ("a", [1], "邊界:單一字元"),
        ("abc", [1, 1, 1], "每個字母只出現一次"),
        ("aaa", [3], "同一個字母貫穿整段"),
        ("aa", [2], "兩個相同字母"),
        ("abac", [3, 1], "a 在開頭和中段各出現一次,c 落在後面"),
        ("caab", [1, 2, 1], "第一個字母只出現一次,後面才是重複"),
        ("abab", [4], "a 與 b 互相交錯,整段不能切"),
        ("abcabc", [6], "三個字母都在後半再次出現"),
        ("abaccbde", [6, 1, 1], "b 把第一段拉到中段,d 與 e 各成一段"),
        ("vwxvw", [5], "v 與 w 的最後出現位置在尾端"),
    ]

    for s, expected, note in test_set:
        result = c.partitionLabels(s)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       input={s!r} | expected={expected} | got={result}")
