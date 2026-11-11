"""
    題意 :
    給定一個字串 s,以及字典 wordDict。
    若 s 可以切成一段以上的字典單字,回傳 True,否則回傳 False。
    字典裡的單字可以重複使用。切分時單字之間不留空字元。

    LeetCode 139 · Medium
    URL : https://leetcode.com/problems/word-break/

    Example :
    s = "leetcode",     wordDict = ["leet","code"]           -> True
    s = "applepenapple", wordDict = ["apple","pen"]          -> True
    s = "catsandog",    wordDict = ["cats","dog","sand","and","cat"] -> False

    Constraint :
    1 <= s.length <= 300
    1 <= wordDict.length <= 1000
    1 <= wordDict[i].length <= 20
    s 與 wordDict[i] 都只含小寫英文字母
    wordDict 裡的單字互不重複

    思路 :

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        pass


if __name__ == "__main__":
    c = Solution()

    # (s, wordDict, 預期, 說明)
    test_set = [
        ("leetcode", ["leet", "code"], True, "官方範例:切成 leet + code"),
        ("applepenapple", ["apple", "pen"], True, "官方範例:apple 用了兩次"),
        (
            "catsandog",
            ["cats", "dog", "sand", "and", "cat"],
            False,
            "官方範例:每種切法最後都剩下 og",
        ),
        ("a", ["a"], True, "邊界:單一字母,字典有這個字"),
        ("a", ["b"], False, "邊界:單一字母,字典沒有"),
        ("cars", ["car", "ca", "rs"], True, "ca + rs,car 接不下去"),
        ("abcd", ["a", "abc", "b", "cd"], True, "a + b + cd"),
        ("aaaaaaa", ["aaaa", "aaa"], True, "4 + 3,字典單字可以湊成 7"),
        ("aaaaaaa", ["aaaa", "aa"], False, "4 和 2 都是偶數,湊不出長度 7"),
        ("bb", ["a", "b", "bbb", "bbbb"], True, "兩個 b 各用一次"),
        ("dogcatcat", ["dog", "cat"], True, "cat 連續使用兩次"),
    ]

    for s, word_dict, expected, note in test_set:
        result = c.wordBreak(s, list(word_dict))
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       s={s!r} | wordDict={word_dict} | expected={expected} | got={result}")
