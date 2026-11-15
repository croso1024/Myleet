"""
    題意 :
    從 beginWord 變到 endWord。每一次只能改一個字母,
    改完的字必須在 wordList 裡。beginWord 本身不必在 wordList。

    回傳最短變換序列的單字數,起點與終點都要算進去。
    變不到 endWord 就回傳 0。

    LeetCode 127 · Hard
    URL : https://leetcode.com/problems/word-ladder/

    Example :
    beginWord = "hit", endWord = "cog",
    wordList = ["hot","dot","dog","lot","log","cog"] -> 5
    beginWord = "hit", endWord = "cog",
    wordList = ["hot","dot","dog","lot","log"] -> 0

    Constraint :
    1 <= beginWord.length <= 10
    endWord.length == beginWord.length
    1 <= wordList.length <= 5000
    wordList[i].length == beginWord.length
    beginWord、endWord、wordList[i] 都是小寫英文字母
    beginWord != endWord
    wordList 裡的字互不重複

    思路 :

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        pass


if __name__ == "__main__":
    c = Solution()

    # (beginWord, endWord, wordList, 預期, 說明)
    # 每次呼叫都複製 wordList,實作若改到清單不會留到下一題
    test_set = [
        (
            "hit",
            "cog",
            ["hot", "dot", "dog", "lot", "log", "cog"],
            5,
            "官方範例:hit -> hot -> dot -> dog -> cog",
        ),
        (
            "hit",
            "cog",
            ["hot", "dot", "dog", "lot", "log"],
            0,
            "官方範例:字典裡沒有終點 cog",
        ),
        (
            "hit",
            "hot",
            ["hot"],
            2,
            "改一個字母就到,beginWord 不在字典裡",
        ),
        (
            "a",
            "c",
            ["a", "b", "c"],
            2,
            "單字母可以直接跳到終點,不必繞路",
        ),
        (
            "a",
            "c",
            ["b", "c"],
            2,
            "終點與起點只差一個字母",
        ),
        (
            "hot",
            "dog",
            ["hot", "dog"],
            0,
            "兩個字差兩個字母,中間沒有跳板",
        ),
        (
            "hit",
            "cog",
            ["cog"],
            0,
            "字典只有終點,但一次改不完",
        ),
        (
            "hit",
            "cog",
            ["hot", "cot", "cog", "dot", "dog", "lot", "log"],
            4,
            "有較短路 hit -> hot -> cot -> cog,不能走長的那條",
        ),
        (
            "abc",
            "def",
            ["aec", "dec", "def"],
            4,
            "abc -> aec -> dec -> def,每步只改一個字母",
        ),
        (
            "red",
            "tax",
            ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"],
            4,
            "red -> ted -> tad -> tax,字典裡有用不到的字",
        ),
    ]

    for begin, end, words, expected, note in test_set:
        result = c.ladderLength(begin, end, list(words))
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       begin={begin} end={end} wordList={words}")
        print(f"       expected={expected}")
        print(f"       got     ={result}")
