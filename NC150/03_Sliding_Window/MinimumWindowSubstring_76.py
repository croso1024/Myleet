"""
    題意 :
    給定字串 s (長度 m) 與 t (長度 n),回傳 s 中「最小的子字串(substring,需連續)」,
    使該窗口包含 t 的所有字元(含重複次數)。若不存在則回傳空字串 ""。
    題目保證答案唯一。

    LeetCode 76 · Hard

    Example :
    s = "ADOBECODEBANC", t = "ABC" -> "BANC"
    s = "a",             t = "a"   -> "a"
    s = "a",             t = "aa"  -> ""     (s 只有一個 'a',湊不出兩個)

    Constraint :
    m == s.length , n == t.length
    1 <= m, n <= 10^5
    s 與 t 由大小寫英文字母組成 (大小寫視為不同字元)

    Follow up : 能否做到 O(m + n)?

    思路 :
    會打算使用 Sliding Window , 持續 maintain 是不是所有的字元都有出現在當前窗口. 
    持續往右擴展,直到納入所有字元 , 一但納入所有字元,就Evaluate + 縮小. 一但不完整納入就繼續擴張


    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        letter_map = {} 

        for char in t : 
            if char in letter_map : 
                letter_map[char] += 1 
            else : 
                letter_map[char] = 1 
        
        left , right = 0 , 0 
        missing = len(t) 
        shortest_substring_size = float("inf")
        shortest_substring_range = None 

        while right < len(s) :

            letter = s[right] 

            if letter in letter_map : 
                if letter_map[letter] > 0 : 
                    missing -= 1 
                letter_map[letter] -= 1 
                
            while missing == 0   : 

                if  (right - left) + 1  < shortest_substring_size : 
                    shortest_substring_size =  (right - left) + 1 
                    shortest_substring_range = (left , right+1)  
                letter = s[left] 
                if letter in letter_map : 
                    if letter_map[letter] >= 0 :
                        missing += 1 
                    letter_map[letter] += 1 
                left += 1 
            
            right += 1 
        
        if shortest_substring_range : 
            return s[shortest_substring_range[0]:shortest_substring_range[1]]
        else : 
            return ""


if __name__ == "__main__":
    c = Solution()

    # (輸入參數 tuple, 預期輸出) —— LeetCode 官方範例 + 邊界案例
    test_set = [
        (("ADOBECODEBANC", "ABC"), "BANC"),
        (("a", "a"), "a"),
        (("a", "aa"), ""),                  # 邊界:t 的重複次數不足
        (("ab", "b"), "b"),                 # 答案在尾端
        (("bba", "ab"), "ba"),              # 答案在尾端且需縮左界
        (("aa", "aa"), "aa"),               # 整個 s 就是答案
        (("ADOBECODEBANC", "ABCC"), "CODEBANC"),  # t 含重複字元(s 剛好有兩個 C)
        (("ADOBECODEBANC", "ABCCC"), ""),         # t 重複次數超過 s 所有,無解
        (("aAbBcC", "Ab"), "Ab"),           # 大小寫視為不同字元
        (("cabwefgewcwaefgcf", "cae"), "cwae"),
    ]

    for args, expected in test_set:
        result = c.minWindow(*args)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={args} | expected={expected!r} | got={result!r}")
