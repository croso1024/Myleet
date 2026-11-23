"""
    題意 :
    給定一個非負整數,以「整數陣列 digits」表示,digits[i] 是該數的第 i 位數字,
    最高位在最前面(index 0)。整數不含前導 0(除了 0 本身)。

    將這個整數加 1,回傳結果同樣以陣列表示。

    LeetCode 66 · Easy
    URL : https://leetcode.com/problems/plus-one/

    Example :
    digits = [1,2,3]   -> [1,2,4]   (123 + 1 = 124)
    digits = [4,3,2,1] -> [4,3,2,2] (4321 + 1 = 4322)
    digits = [9]       -> [1,0]     (9 + 1 = 10)

    Constraint :
    1 <= digits.length <= 100
    0 <= digits[i] <= 9
    digits 不含前導 0

    思路 :

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        pass


if __name__ == "__main__":
    c = Solution()

    # (digits, 預期, 說明)
    # 每次呼叫都複製 digits,實作若原地修改,不會影響到下一題
    test_set = [
        ([1, 2, 3], [1, 2, 4], "官方範例:末位直接 +1"),
        ([4, 3, 2, 1], [4, 3, 2, 2], "官方範例:末位直接 +1"),
        ([9], [1, 0], "官方範例:單一位數進位,長度 +1"),
        ([0], [1], "邊界:數字 0"),
        ([1, 0, 0], [1, 0, 1], "中間皆為 0,不需進位"),
        ([1, 2, 9], [1, 3, 0], "末位進位,影響到前一位"),
        ([1, 9, 9], [2, 0, 0], "連續進位,但最高位不是 9"),
        ([9, 8, 9], [9, 9, 0], "進位只傳到第二位"),
        ([8, 9, 9, 9], [9, 0, 0, 0], "連續進位直到最高位,但最高位不溢位"),
        ([9, 9, 9], [1, 0, 0, 0], "全部是 9,結果多一位"),
        ([9] * 100, [1] + [0] * 100, "邊界:100 位全 9"),
        ([1] + [0] * 98 + [9], [1] + [0] * 97 + [1, 0], "邊界:100 位,只有末位進位"),
    ]

    for digits, expected, note in test_set:
        result = c.plusOne(digits[:])
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       digits={digits}")
        print(f"       expected={expected}")
        print(f"       got     ={result}")
