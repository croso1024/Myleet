"""
    題意 :
    設計一個字典,支援加入單字,以及查詢某個 pattern 是否能對上已加入的單字。

    實作 WordDictionary class :
      - WordDictionary()              初始化
      - addWord(word: str)            加入 word
      - search(word: str) -> bool     若存在某個已加入的單字能對上 word,回傳 True

    search 的 word 可以含 '.';每個 '.' 可以對上任意一個英文字母,而且只對上一個字元。
    長度必須完全一致。只是前綴、或中間差一個字,都不算命中。

    LeetCode 211 · Medium
    URL : https://leetcode.com/problems/design-add-and-search-words-data-structure/

    Example :
    操作   ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
    參數   [[],              ["bad"],  ["dad"],  ["mad"],  ["pad"],  ["bad"],  [".ad"],  ["b.."]]
    輸出   [null,            null,     null,     null,     false,    true,     true,     true]

    Constraint :
    1 <= word.length <= 25
    addWord 的 word 只含小寫英文字母
    search 的 word 只含 '.' 或小寫英文字母
    每次 search 的 word 最多 2 個 '.'
    addWord / search 總呼叫次數最多 10^4

    思路 :

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""


class WordDictionary:
    def __init__(self):
        pass

    def addWord(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass


def run(ops, args):
    dictionary = None
    output = []
    for op, arg in zip(ops, args):
        if op == "WordDictionary":
            dictionary = WordDictionary()
            output.append(None)
        elif op == "addWord":
            dictionary.addWord(*arg)
            output.append(None)
        elif op == "search":
            output.append(dictionary.search(*arg))
    return output


if __name__ == "__main__":
    # (操作, 參數, 預期輸出, 說明)
    test_set = [
        (
            ["WordDictionary", "addWord", "addWord", "addWord", "search", "search", "search", "search"],
            [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]],
            [None, None, None, None, False, True, True, True],
            "官方範例:'.' 可對任意一字,長度必須相同",
        ),
        (
            ["WordDictionary", "search", "search"],
            [[], ["a"], ["."]],
            [None, False, False],
            "邊界:什麼都還沒加入",
        ),
        (
            ["WordDictionary", "addWord", "search", "search", "search"],
            [[], ["a"], ["a"], ["."], ["b"]],
            [None, None, True, True, False],
            "邊界:單一字元,'.' 對上它",
        ),
        (
            ["WordDictionary", "addWord", "search", "search", "search", "search", "search"],
            [[], ["apple"], ["apple"], ["app"], ["app.."], ["ap.le"], ["ap.l"]],
            [None, None, True, False, True, True, False],
            "前綴本身不是完整單字;長度差一的 pattern 對不上",
        ),
        (
            ["WordDictionary", "addWord", "search", "search", "search", "search"],
            [[], ["ab"], ["a"], ["."], [".."], ["a."]],
            [None, None, False, False, True, True],
            "'.' 只吃一個字元,較短的 pattern 對不上較長的字",
        ),
        (
            ["WordDictionary", "addWord", "addWord", "search", "search", "search", "search"],
            [[], ["a"], ["ab"], ["a"], ["."], [".."], ["a."]],
            [None, None, None, True, True, True, True],
            "短字與長字同時存在,兩種長度都要能查到",
        ),
        (
            ["WordDictionary", "addWord", "addWord", "search", "search", "search", "search"],
            [[], ["bad"], ["bed"], ["b.d"], ["b.t"], [".e."], ["..d"]],
            [None, None, None, True, False, True, True],
            "同長度分岔,'.' 放在開頭、中間、結尾",
        ),
        (
            ["WordDictionary", "addWord", "addWord", "search", "search", "search"],
            [[], ["cat"], ["car"], ["c.t"], ["ca."], [".a."]],
            [None, None, None, True, True, True],
            "共用前綴後分岔",
        ),
        (
            ["WordDictionary", "addWord", "addWord", "search"],
            [[], ["app"], ["app"], ["app"]],
            [None, None, None, True],
            "同一字加入兩次,仍然只算存在",
        ),
    ]

    for ops, args, expected, note in test_set:
        result = run(ops, args)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       expected={expected}")
        print(f"       got     ={result}")
