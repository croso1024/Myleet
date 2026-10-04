"""
    題意 :
    給定一個字串 s,把它切成若干段,使每一段都是迴文。
    回傳所有這樣的切法。

    每一種切法裡,片段的順序就是它們在原字串裡的順序。
    切法之間的順序不限。

    LeetCode 131 · Medium
    URL : https://leetcode.com/problems/palindrome-partitioning/

    Example :
    s = "aab" -> [["a","a","b"],["aa","b"]]
    s = "a"   -> [["a"]]

    Constraint :
    1 <= s.length <= 16
    s 只含小寫英文字母

    思路 :
    這一題不看題型會覺得是Array,但思考一下會導向Backtracking, 
    題目中一個額外的思考點是該如何快速判斷回文. 考量到已知這題最大長度為16, 
    先用一個Naive作法去判斷回文. 將演算法重心放在如何做 Backtraking. 
    回溯樹展開,只要保持回文就繼續展,直到非回文中斷

    上述解法完全想錯,我誤解了題目意思. 但也讓這一題變得很難.
    要切出不同片段來讓解答每一段都是回文.問題變成要切幾刀 , 切在哪.
    和 Agent 討論一下這一題. 關鍵在調整切開的範圍. 
    給定 "aab" , 能切的範圍有 1. 切一個字 / 2. 切兩個字 / 3. 切三個字....
    前兩者切完後還能繼續往下展開 , 展開又能再 1. 切一個字/2.切兩個字
    因此這一題追蹤用的軌跡應該是 List[str]
    
    這一題我認為很精華,思考方式需要繞一層

    複雜度 : 
    - 每一次 Evaluate 回文 , O(S) 
    - 展開的層數, 在最大情況下每一層只切一個字的話就是往下切16層. 
    - 空間複雜度 , 最多往下切16層, 每一層攜帶長度最多為S的字串 , 空間複雜度為 O(S^2)
    
    Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        results = [] 

        def is_palindrome(string:str): 
            left , right = 0 , len(string) - 1 
            while left < right : 
                if string[left] == string[right] : 
                    left += 1
                    right -= 1 
                else : return False 
            return True 

        def _backtracking( rest:str , path : List[str] ):  

            # 剛好走完,就代表這一路上所有的都是迴文,可以加入答案
            if len(rest) == 0 : 
                results.append(path[:])
                return 
            
            # 依據剩餘字串的長度,分出不同切法
            for i in range(len(rest)) : 
                
                # 開始切,切完如果是切出迴文才繼續. 
                partition = rest[:i+1] 
                if is_palindrome(partition) :
                    path.append(partition)
                    _backtracking( rest = rest[i+1:] , path = path)
                    path.pop()
            

        _backtracking(rest = s , path = [])
        return results 
            
            


def canon(parts: List[List[str]]):
    """切法之間的順序不影響對錯;每一種切法內部的片段順序要保留。"""
    if parts is None:
        return None
    return sorted(tuple(group) for group in parts)


if __name__ == "__main__":
    c = Solution()

    # (輸入, 預期輸出, 說明) —— 只忽略切法彼此的順序
    test_set = [
        ("aab", [["a", "a", "b"], ["aa", "b"]], "官方範例"),
        ("a", [["a"]], "官方範例:單一字母"),
        ("aa", [["a", "a"], ["aa"]], "兩種切法,整段也是迴文"),
        ("ab", [["a", "b"]], "整段不是迴文,只能逐字切"),
        ("aba", [["a", "b", "a"], ["aba"]], "奇數長度的整段迴文"),
        (
            "aaa",
            [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]],
            "每個子字串都是迴文",
        ),
        (
            "abba",
            [["a", "b", "b", "a"], ["a", "bb", "a"], ["abba"]],
            "中間兩字成段,或整段",
        ),
        ("abc", [["a", "b", "c"]], "沒有任何更長的迴文片段"),
        ("bb", [["b", "b"], ["bb"]], "兩個相同字母"),
        (
            "aaaa",
            [
                ["a", "a", "a", "a"],
                ["a", "a", "aa"],
                ["a", "aa", "a"],
                ["aa", "a", "a"],
                ["a", "aaa"],
                ["aaa", "a"],
                ["aa", "aa"],
                ["aaaa"],
            ],
            "四個相同字母,每一種子字串都是迴文",
        ),
    ]

    for s, expected, note in test_set:
        result = c.partition(s)
        passed = canon(result) == canon(expected)
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       input={s!r}")
        print(f"       expected={expected}")
        print(f"       got     ={result}")
