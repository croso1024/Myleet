"""
    題意 :
    給定一個字串 s。回傳其中最長的回文子字串。
    子字串必須是連續的一段。
    若有多個同樣長的答案,回傳任一個即可。

    LeetCode 5 · Medium
    URL : https://leetcode.com/problems/longest-palindromic-substring/

    Example :
    s = "babad" -> "bab"
    s = "cbbd"  -> "bb"

    Constraint :
    1 <= s.length <= 1000
    s 只含數字與英文字母

    思路 :

    Given s.length <= 1000 , 
    一次評估回文最多 O(S) , 如果雙迴圈就是 O(S^2) 不可行.
    雙指標動態掃,因為回文的關係也無法確認縮小與放大的時間點. 
    走DP , 1D DP去掃,那該如何記憶狀態!? ,

    先走 Naive Solution , 擴散的方式,時間複雜度 O(S^2) , 空間 O(C)


    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""


class Solution:
    def longestPalindrome(self, s: str) -> str:

        longest_palindrome = ""

        def check_and_update_longest_palindrome( k : int , odd : bool = True ): 
            # 先確認回文的長度是偶數還是奇數, 依據 odd : bool 
            nonlocal longest_palindrome 
            k1 = k 
            k2 = k if odd else k + 1 
            i = 0 

            while k1 - i >= 0 and  k2 + i < len(s) : 
                if s[k1-i] != s[k2+i] : break 
                i += 1 
            
            # 當跳出的時候,代表目前回文走到邊界外,要馬就是回文不成立了.
            # 量長度,更新答案. 子字串為 k1 - i + 1 ~ k2 + i 的範圍
            substring = s[(k1-i+1):(k2+i)] 
            if len(substring) > len(longest_palindrome) : 
                longest_palindrome = substring
            return 
        
        for i in range(len(s)): 
            check_and_update_longest_palindrome(i, False)
            check_and_update_longest_palindrome(i, True)
        
        return longest_palindrome







if __name__ == "__main__":
    c = Solution()

    # (s, 預期, 說明)
    # 預期若是 tuple,裡面任一個都算對
    test_set = [
        ("babad", ("bab", "aba"), "官方範例:bab 與 aba 一樣長"),
        ("cbbd", "bb", "官方範例:偶數長度的回文"),
        ("a", "a", "邊界:只有一個字母"),
        ("ac", ("a", "c"), "兩個不同字母,任一單字都是最長"),
        ("aa", "aa", "兩個相同字母"),
        ("aaa", "aaa", "三個相同字母,整段都是回文"),
        ("abba", "abba", "偶數回文蓋住整段"),
        ("abcba", "abcba", "奇數回文蓋住整段"),
        ("bananas", "anana", "最長回文在中間"),
        ("aacabdkacaa", "aca", "官方另一組:長度 3 的 aca"),
    ]

    for s, expected, note in test_set:
        result = c.longestPalindrome(s)
        if isinstance(expected, tuple):
            passed = result in expected
        else:
            passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       input={s} | expected={expected} | got={result}")
