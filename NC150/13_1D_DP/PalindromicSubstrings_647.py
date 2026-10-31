"""
    題意 :
    給定一個字串 s。回傳裡面有多少個回文子字串。
    子字串必須是連續的一段。
    單一個字母也算回文。同一段文字出現在不同位置要分開計數。

    LeetCode 647 · Medium
    URL : https://leetcode.com/problems/palindromic-substrings/

    Example :
    s = "abc" -> 3
    s = "aaa" -> 6

    Constraint :
    1 <= s.length <= 1000
    s 由小寫英文字母組成

    思路 :
    以擴散的方式，同時找長度為偶數與奇數的回文. 
    每一輪只要找到的是回文,答案就 +=1 , 一但非回文就中斷即可.

    複雜度 : 

    外層迴圈要走 O(N) 次,
    每一次開始檢查最多 O(N) , 因此時間複雜度為 O(N^2) , 儲存空間上 O(1) 

    Trade-off :

"""

class Solution:
    def countSubstrings(self, s: str) -> int:

        size = len(s)
        count = 0 

        def _count_palindromic(index : int , odd : bool = True) : 
            nonlocal count 
            k1 = index 
            k2 = index if odd else index + 1 
            while k1 >= 0 and k2 < size : 
                if s[k1] == s[k2] : 
                    count += 1 
                else : break 
                k1 -= 1  
                k2 += 1 
            return 
        
        for i in range(size): 
            _count_palindromic(index = i , odd = False) 
            _count_palindromic(index = i , odd = True) 
        
        return count 


if __name__ == "__main__":
    c = Solution()

    # (s, 預期, 說明)
    test_set = [
        ("abc", 3, "官方範例:三個單字母"),
        ("aaa", 6, "官方範例:3 個單字母、2 個 aa、1 個 aaa"),
        ("a", 1, "邊界:只有一個字母"),
        ("aa", 3, "兩個相同字母:兩個單字母加上 aa"),
        ("ab", 2, "兩個不同字母,沒有更長的回文"),
        ("aba", 4, "三個單字母加上 aba"),
        ("abba", 6, "四個單字母、中間的 bb、整段 abba"),
        ("abcba", 7, "五個單字母、bcb、整段 abcba"),
        ("aaaa", 10, "四個相同字母,每一段子字串都是回文"),
        ("aabaa", 9, "五個單字母、兩段 aa、aba、整段 aabaa"),
    ]

    for s, expected, note in test_set:
        result = c.countSubstrings(s)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       input={s} | expected={expected} | got={result}")
