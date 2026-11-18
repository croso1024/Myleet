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

    n = 0 0
    n = 1 1
    n = 2 10
    n = 3 11 
    n = 4 100
    n = 5 101
    n = 6 110
    n = 7 111
    n = 8 1000
    n = 9 1001
    n = 10 1010
    n = 11 1011
    n = 12 1100
    n = 13 1101
    n = 14 1110
    n = 15 1111


    Constraint :
    0 <= n <= 10^5

    思路 :
    這題要的是 0 ~ n 每一個數字的二進位表示法有幾個 1 出現. 
    且 n 在 10000 量級內. 

    看起來是可以 1D DP 推上去. 
    假設已知 dp[i] 是數字為 i 的二進位表示法有多少個 1 , 
    那麼 i+1 的二進位表示法有幾個 1 ? 

    列出整張表,看規律, n 在 2 的冪次上必然是1 
    除此之外 , 規則為 : 
    dp[i+1] = dp[i] + 1 if i % 2 == 0 else dp[i] 

    === 上述解法 , 在 n = 12 有錯 , n=12只有2個1 , n=11有3個

    正確的推導狀態應該是 : 
    n = 0 => 0
    n = 1 ,開根號等於 1
    n = 2 , 1
    n = 3  : n:2 + n:1

    n = 8 => 1
    n = 9 => 1001 => n:8 + n:1


    n = 12 => n:8 + n:4 的數量.
    n = 13 => n:8 + n:4 + n:1 = 3 == n:8 + n:5 

    n = 15 => n:8 + n:7

    n = 13 開根號等於 3.x , 等於 8 , 再加上表上一個已經有的值 5
    n = 24 : 11000 = 16 + 8 
    n = 27 : 11011 = 16 + 8 + 3 = 16 + 11  


    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List
from math import log2 , floor


class Solution:
    def countBits(self, n: int) -> List[int]:

        # 填入初始值
        results = [ 0 ]
        if n == 0 : return results 
        results.append(1)
        if n == 1 : return results 

        for i in range(2,n+1):
            if i & (i-1) == 0 : 
                results.append(1)
                continue
            # 將數字先開根號,取整
            k = floor(log2(i)) 
            # print(f"I : {i} , results : {results} , k = {k}")
            # 將 k 與該數字相減就知道要參考那個值
            # k 表達該數字首位在 2 的多少冪次 , 下一步則是從表上去找補數
            cur = results[ pow(2,k) ] + results[i - pow(2,k)] 
            results.append(cur)
        return results


# 優化版 


class Solution:
    def countBits(self, n: int) -> List[int]:

        # 填入初始值
        results = [0]

        # k 表示當前走到的最高位是哪一位. 
        # e.g  n = 3 : 11 , 當前最高位 2  , n = 4 : 100 當前最高位 = 3

        k = 0


        for i in range(1,n+1):
            if i & (i-1) == 0 : 
                results.append(1)
                k += 1 
                continue
            # 將 k 與該數字相減就知道要參考那個值
            # k 表達該數字首位在 2 的多少冪次 , 下一步則是從表上去找補數

            # 每一個數字如果不是 2 的冪次 , 那就是用其當前最高位次 (而且必然為1) , 然後補上差值,差值已經算好
            cur = 1 + results[i - pow(2,k)] 
            results.append(cur)
        return results





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
