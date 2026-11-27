"""
    題意 :
    一段只含字母 A-Z 的訊息,依下列對應編碼成數字字串:
        'A' -> "1"
        'B' -> "2"
        ...
        'Z' -> "26"

    解碼時,要把數字字串切分成若干段,每一段都必須對應到上表中的某個字母。
    例如 "11106" 可以解成:
        "AAJF" (1 1 10 6)
        "KJF"  (11 10 6)
    但切成 (1 11 06) 不合法,因為 "06" 不在對應表中("6" 才是)。

    給定只含數字的字串 s,回傳解碼方式的總數。
    若完全無法解碼,回傳 0。

    測資保證答案落在 32-bit 整數範圍內。

    LeetCode 91 · Medium
    URL : https://leetcode.com/problems/decode-ways/

    Example :
    s = "12"  -> 2  ("AB" (1 2)、"L" (12))
    s = "226" -> 3  ("BZ" (2 26)、"VF" (22 6)、"BBF" (2 2 6))
    s = "06"  -> 0  ("06" 不在對應表中)

    Constraint :
    1 <= s.length <= 100
    s 只含數字,且可能有前導 0

    思路 :

    可以參與解碼的數字必然在 1 ~ 26 , 而且沒有前導0 , 因此遇到0必然只能和前一個數值結合被解讀為 10 / 20 , 遇到 30 就是有問題不用再往下看.
    這看起來走 1D - DP ,關鍵在狀態轉移. 

    定義 dp[i] 是指使用到 s[i] 的情況下可以組出多少數字 , 

    dp[0] == 1 if s[0] in [1~9] , 
    dp[i] == dp[i-2] + dp[i-1] ( 如果 s[i] 可以和 s[i-1] 組合 , 且 s[i] != 0 , i >= 2 ) 
    dp[i] == 1 + dp[i-1] ( 如果 s[i] 可以和 s[i-1] 組合 , 且 s[i] != 0 , i == 1 ) 
    dp[i] == dp[i-1] ( 如果 s[i] 不能和 s[i-1] 組合 且 s[i] != 0 )
    異常 ( 如果 s[i] 不能和 s[i-1] 組合 且 s[i] == 0  )

    時間複雜度為 O(N) , 空間為 O(N) , 經過空間壓縮可以 O(C)

    複雜度 : Time O(?) / Space O(?)

    Trade-off :
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        
        # 初始 Case 
        get_digit = lambda i : int(s[i]) 

        dp = [None for i in range(len(s))]
        if get_digit(0) == 0 : return 0
        else : dp[0] = 1 

        for i in range(1 , len(s)): 

            cur_digit = get_digit(i)        
            prev_digit = get_digit(i-1) 
            # 檢查 digit 是否可以與前一個數字合併
            
            # 處理這一格是0的特殊情況
            if cur_digit == 0 : 
                # 如果和前一格可以合併
                if prev_digit in [1,2] : 
                    dp[i] = dp[i-2] if i >= 2 else 1 
                    continue 
                else : 
                    return 0 
            # 處理前一格是0的特殊情況,當前這格也是0上面處理過了
            if prev_digit == 0 : 
                dp[i] = dp[i-1]
                continue
            
            # 剩下情況就可以檢查組合 , cur/prev都不為0
            # 檢查是否可組合 : prev_digit * 10 + cur_digit 
            
            # Case.1 可組合
            if 10 * prev_digit + cur_digit <= 26 : 
                dp[i] = dp[i-1] + dp[i-2] if i >= 2 else dp[i-1] + 1 

            # Case.2 不可組合 
            else : 
                dp[i] = dp[i-1]
        return dp[-1]


if __name__ == "__main__":
    c = Solution()

    # (s, 預期, 說明)
    test_set = [
        ("12", 2, "官方範例"),
        ("226", 3, "官方範例"),
        ("06", 0, "官方範例:前導 0"),
        ("11106", 2, "題意中的範例"),
        ("1", 1, "邊界:單一非 0 數字"),
        ("0", 0, "邊界:單一 '0'"),
        ("00", 0, "連續兩個 0"),
        ("10", 1, "兩位數:10"),
        ("20", 1, "兩位數:20"),
        ("30", 0, "兩位數:30"),
        ("26", 2, "兩位數:26"),
        ("27", 1, "兩位數:27"),
        ("100", 0, "100"),
        ("101", 1, "101"),
        ("110", 1, "110"),
        ("230", 0, "結尾為 30"),
        ("2101", 1, "0 出現在中間"),
        ("1123", 5, "全部數字皆為 1~3"),
        ("1201234", 3, "較長字串,含一個 0"),
        ("2611055971756562", 4, "較長字串,含一個 0 與多個大於 2 的數字"),
        ("1111111111", 89, "10 個 1"),
        ("1" * 40, 165580141, "40 個 1"),
    ]

    for s, expected, note in test_set:
        result = c.numDecodings(s)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       s={s!r}")
        print(f"       expected={expected}")
        print(f"       got     ={result}")
