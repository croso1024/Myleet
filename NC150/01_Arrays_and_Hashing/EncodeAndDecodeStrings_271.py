"""
    題意 :
    設計一組演算法,能把「字串陣列」編碼成「單一字串」,並在網路上傳輸後,
    還原回原本的字串陣列。

    實作兩個方法 :
      - encode(strs: List[str]) -> str   將字串陣列編碼成一個字串
      - decode(s: str) -> List[str]      將編碼後的字串還原成原陣列

    你不需要處理實際的網路傳輸,只要保證 decode(encode(strs)) == strs 即可。
    不得使用任何序列化函式庫(如 eval / pickle / json)。

    LeetCode 271 · Medium 🔒
    URL : https://leetcode.com/problems/encode-and-decode-strings/
    ※ 此題在 LeetCode 為 Premium 鎖定題,免費帳號看不到題面。
      上面的題意採用 NeetCode / LintCode 659 的通用敘述(兩者為同一題)。
    免費可練 : https://neetcode.io/problems/string-encode-and-decode

    Example :
    strs = ["neet","code","love","you"] -> encode -> 某個字串 -> decode -> ["neet","code","love","you"]
    strs = ["we","say",":","yes"]       -> encode -> 某個字串 -> decode -> ["we","say",":","yes"]

    Constraint :
    0 <= strs.length < 100
    0 <= strs[i].length < 200
    strs[i] 由任意 UTF-8 字元組成

    思路 :

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        pass

    def decode(self, s: str) -> List[str]:
        pass


if __name__ == "__main__":
    c = Solution()

    # 本題驗的是「round-trip」:decode(encode(strs)) 必須等於原本的 strs
    # (輸入的字串陣列, 說明)
    test_set = [
        (["neet", "code", "love", "you"], "官方範例"),
        (["we", "say", ":", "yes"], "官方範例,含冒號"),
        ([], "邊界:空陣列"),
        ([""], "邊界:單一空字串 —— 與空陣列必須能被區分開"),
        (["", ""], "邊界:兩個空字串 —— 長度資訊不能遺失"),
        (["#", "##", "###"], "資料本身就長得像分隔符"),
        (["4#abc", "3#de"], "資料本身就長得像『長度#內容』的編碼格式"),
        ([":", ";", ":;:"], "各種標點"),
        (["a" * 199], "邊界:接近長度上限的單一字串"),
        (["中文", "🙂", "a\nb"], "UTF-8 多位元組字元與換行"),
    ]

    for strs, note in test_set:
        encoded = c.encode(strs)
        result = c.decode(encoded)
        passed = result == strs
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       input  ={strs}")
        print(f"       encoded={encoded!r}")
        print(f"       decoded={result}")
