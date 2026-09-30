"""
    題意 :
    實作一個 Trie(prefix tree),用來存一組字串,並支援插入、完整查詢、前綴查詢。

    實作 Trie class :
      - Trie()                         初始化
      - insert(word: str)              插入 word
      - search(word: str) -> bool      word 必須曾經被完整插入過才回傳 True
      - startsWith(prefix: str) -> bool  只要有任一已插入的字以 prefix 開頭就回傳 True

    LeetCode 208 · Medium
    URL : https://leetcode.com/problems/implement-trie-prefix-tree/

    Example :
    操作   ["Trie","insert","search","search","startsWith","insert","search"]
    參數   [[],    ["apple"],["apple"],["app"], ["app"],     ["app"], ["app"]]
    輸出   [null,  null,    true,    false,   true,       null,    true]

    Constraint :
    1 <= word.length, prefix.length <= 2000
    word 與 prefix 只含小寫英文字母
    insert / search / startsWith 總呼叫次數最多 3 * 10^4

    思路 :

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""


class Trie:
    def __init__(self):
        pass

    def insert(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass

    def startsWith(self, prefix: str) -> bool:
        pass


def run(ops, args):
    trie = None
    output = []
    for op, arg in zip(ops, args):
        if op == "Trie":
            trie = Trie()
            output.append(None)
        elif op == "insert":
            trie.insert(*arg)
            output.append(None)
        elif op == "search":
            output.append(trie.search(*arg))
        elif op == "startsWith":
            output.append(trie.startsWith(*arg))
    return output


if __name__ == "__main__":
    # (操作, 參數, 預期輸出, 說明)
    test_set = [
        (
            ["Trie", "insert", "search", "search", "startsWith", "insert", "search"],
            [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]],
            [None, None, True, False, True, None, True],
            "官方範例:較短的字後來才插入",
        ),
        (
            ["Trie", "search", "startsWith"],
            [[], ["a"], ["a"]],
            [None, False, False],
            "邊界:什麼都還沒插入",
        ),
        (
            ["Trie", "insert", "search", "startsWith", "search", "startsWith"],
            [[], ["a"], ["a"], ["a"], ["b"], ["b"]],
            [None, None, True, True, False, False],
            "邊界:單一字元",
        ),
        (
            ["Trie", "insert", "insert", "search", "search", "startsWith", "search"],
            [[], ["app"], ["apple"], ["app"], ["apple"], ["ap"], ["ap"]],
            [None, None, None, True, True, True, False],
            "先插短字再插長字;前綴本身不是完整單字",
        ),
        (
            ["Trie", "insert", "insert", "search", "startsWith", "startsWith", "search"],
            [[], ["dog"], ["dot"], ["dog"], ["do"], ["dot"], ["doge"]],
            [None, None, None, True, True, True, False],
            "共用前綴後分岔,多出來的字尾不算命中",
        ),
        (
            ["Trie", "insert", "insert", "search", "startsWith"],
            [[], ["cat"], ["car"], ["cat"], ["ca"]],
            [None, None, None, True, True],
            "同前綴、不同結尾",
        ),
        (
            ["Trie", "insert", "insert", "search"],
            [[], ["app"], ["app"], ["app"]],
            [None, None, None, True],
            "同一字插入兩次,仍然只算存在",
        ),
        (
            ["Trie", "insert", "startsWith", "startsWith", "search"],
            [[], ["apple"], ["apple"], ["applea"], ["apple"]],
            [None, None, True, False, True],
            "完整單字是自己的前綴;比它更長的前綴則否",
        ),
    ]

    for ops, args, expected, note in test_set:
        result = run(ops, args)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       expected={expected}")
        print(f"       got     ={result}")
