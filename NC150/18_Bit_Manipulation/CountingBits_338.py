"""
    題意 :
    給定一個整數 n,回傳一個長度為 n + 1 的陣列 ans,
    其中 ans[i] 是 i 的二進位表示中 1 的個數 (0 <= i <= n)。

    Follow up :
    - O(n log n) 的解法很直覺,能不能做到 O(n) 一次掃描?
    - 能不能不用任何內建函式(例如 bin(i).count("1")、__builtin_popcount)?

    LeetCode 338 · Easy
    URL : https://leetcode.com/problems/counting-bits/

    Example :
    n = 2 -> [0,1,1]
    n = 5 -> [0,1,1,2,1,2]

    Constraint :
    0 <= n <= 10^5

    思路 :

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        pass


def first_mismatch(result, expected):
    """長陣列不整段印出來,只回報第一個不一樣的位置。"""
    if not isinstance(result, list):
        return f"回傳型別錯誤:{type(result).__name__}"
    if len(result) != len(expected):
        return f"長度不符:expected={len(expected)} got={len(result)}"
    for i, (got, want) in enumerate(zip(result, expected)):
        if got != want:
            return f"第一個錯誤在 i={i}:expected={want} got={got}"
    return None


if __name__ == "__main__":
    c = Solution()

    # 大量測資的預期值用內建 bin().count 產生,只用來驗證,實作請不要用它
    large_n = 10**5
    large_expected = [bin(i).count("1") for i in range(large_n + 1)]

    # (n, 預期, 說明)
    test_set = [
        (2, [0, 1, 1], "官方範例"),
        (5, [0, 1, 1, 2, 1, 2], "官方範例"),
        (0, [0], "邊界:n = 0,只有一個元素"),
        (1, [0, 1], "邊界:n = 1"),
        (
            8,
            [0, 1, 1, 2, 1, 2, 2, 3, 1],
            "遇到 2 的冪次 (8),1 的個數重置為 1",
        ),
        (
            15,
            [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4],
            "結尾是全 1 的 15 (1111)",
        ),
        (
            16,
            [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1],
            "跨過 2 的冪次:15 -> 16 從 4 掉回 1",
        ),
        (large_n, large_expected, "邊界:n = 10^5,檢查效率與長度"),
    ]

    for n, expected, note in test_set:
        result = c.countBits(n)
        mismatch = first_mismatch(result, expected)
        status = "Pass" if mismatch is None else "Failed"
        print(f"{status} | n={n} | {note}")
        if mismatch is not None:
            print(f"       {mismatch}")
