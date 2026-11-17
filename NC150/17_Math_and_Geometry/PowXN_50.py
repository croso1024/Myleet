"""
    題意 :
    實作 pow(x, n),也就是計算 x 的 n 次方 (x^n)。
    n 可能是負數,此時 x^n = 1 / x^(-n)。

    LeetCode 50 · Medium
    URL : https://leetcode.com/problems/powx-n/

    Example :
    x = 2.00000, n = 10  -> 1024.00000
    x = 2.10000, n = 3   -> 9.26100
    x = 2.00000, n = -2  -> 0.25000

    Constraint :
    -100.0 < x < 100.0
    -2^31 <= n <= 2^31 - 1
    n 是整數
    x 不為 0,或 n > 0
    -10^4 <= x^n <= 10^4

    思路 :
    想法上,是要實做自己的 power 函數!? 
    看起來 n 可以非常巨大. 直接裸乘不太可能. 
    n = 2^31 , 那應該可以走 Divide and Conquer 去拆. 不用拆非常多層
    補用一個 memo table 作為快取即可

    時間複雜度 O(logN) (每一次都拆一半)
    空間複雜度 O(logN) ,實際存的子問題數量級 , 遞迴深度也大概是 O(LogN) 


    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

import math


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0 : return 1 
        memo = {1 : x}
        def _pow(x :float , n:int): 
            if n not in memo :
                result =  _pow(x , n // 2) * _pow(x , n - (n//2) )
                memo[n] = result 
            return memo[n]

        if n > 0 : 
            return _pow(x,n) 
        else :
            return 1 / _pow(x , -1*n)
        

if __name__ == "__main__":
    c = Solution()

    INT_MAX = 2**31 - 1
    INT_MIN = -(2**31)

    # (x, n, 預期, 說明)
    # 浮點數比對:容許誤差到小數點後 5 位(與 LeetCode 判定一致)
    test_set = [
        (2.0, 10, 1024.0, "官方範例:正次方"),
        (2.1, 3, 9.261, "官方範例:非整數底數"),
        (2.0, -2, 0.25, "官方範例:負次方取倒數"),
        (5.0, 0, 1.0, "邊界:n = 0,任何非零底數都是 1"),
        (2.0, 1, 2.0, "邊界:n = 1"),
        (0.0, 5, 0.0, "邊界:x = 0 且 n > 0"),
        (-2.0, 3, -8.0, "負底數 + 奇數次方,結果為負"),
        (-2.0, 4, 16.0, "負底數 + 偶數次方,結果為正"),
        (0.5, -3, 8.0, "小於 1 的底數取負次方,結果變大"),
        (1.0, INT_MAX, 1.0, "陷阱:n = 2^31 - 1,逐次相乘會跑太久"),
        (-1.0, INT_MAX, -1.0, "陷阱:n 極大且為奇數,符號要保留"),
        (1.0, INT_MIN, 1.0, "陷阱:n = -2^31,取 -n 在 Java 會 overflow"),
        (-1.0, INT_MIN, 1.0, "陷阱:n = -2^31 是偶數,結果為正"),
        (2.0, INT_MIN, 0.0, "陷阱:n = -2^31,結果極小趨近 0"),
    ]

    for x, n, expected, note in test_set:
        result = c.myPow(x, n)
        passed = isinstance(result, (int, float)) and math.isclose(
            result, expected, rel_tol=1e-9, abs_tol=1e-5
        )
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       x={x} n={n} | expected={expected} | got={result}")
