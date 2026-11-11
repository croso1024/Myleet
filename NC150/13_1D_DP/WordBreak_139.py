"""
    題意 :
    給定一個字串 s,以及字典 wordDict。
    若 s 可以切成一段以上的字典單字,回傳 True,否則回傳 False。
    字典裡的單字可以重複使用。切分時單字之間不留空字元。

    LeetCode 139 · Medium
    URL : https://leetcode.com/problems/word-break/

    Example :
    s = "leetcode",     wordDict = ["leet","code"]           -> True
    s = "applepenapple", wordDict = ["apple","pen"]          -> True
    s = "catsandog",    wordDict = ["cats","dog","sand","and","cat"] -> False

    Constraint :
    1 <= s.length <= 300
    1 <= wordDict.length <= 1000
    1 <= wordDict[i].length <= 20
    s 與 wordDict[i] 都只含小寫英文字母
    wordDict 裡的單字互不重複

    思路 :
    第一段的想法是展開. 
    先將 wordDict 轉為一個 HashSet, 之後走 remaining 將字串丟進去 , 每一輪逐步減少.並看開頭幾個字是否有任何Match的方式做.
    由於 s.length <= 300 , 遞迴深度最深為300. 

    在紙張上演練一次 , 
    假設題目給的 Dict : lee / leet / code , 而 s = "leetcode" , 走1D DP
    "" -> True ( 空視為可以 Match )
    l -> False
    le -> False
    lee -> True
    leet -> True 
    leetc -> 回頭檢查先前有辦法Match的 , 相當於要找 tc / c 這兩個 ,都沒有 -> False
    leetco -> 回頭檢查先前有辦法Match的 , 相當於要找 tco / co 這兩個 ,都沒有 -> False
    leetcod -> 回頭檢查先前有辦法Match的 , 相當於要找 tcod / cod 這兩個 ,都沒有 -> False
    leetcode -> 回頭檢查先前有辦法Match的 , 相當於要找 tcode / code 這兩個 , 有 code -> True 

    在這個架構下 , 時間複雜度為雙迴圈 O(N^2) ( 假設 N = length(s) ) , 而查表走 HashSet O(1) , 但要付出 O( wordDict x len(wordDict[i]) ) 的空間

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from turtle import back
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordSet = set(wordDict) 

        dp = [False] * (len(s) + 1)
        dp[0] = True

        for index in range(1,len(dp)): 
            for j in range(index): 
                # 從原始字串中去抽
                # 若 dp[j] 為 True , 則檢查字串從 j 開始到當前 index 的範圍是否存在 wordSet 
                if dp[j] and s[j:index] in wordSet : 
                    dp[index] = True 
        
        return dp[-1]


# 解法二 , 按照我的原思路 , 展開
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        word_set = set(wordDict) 
        size = len(s) 
        memo = {}

        # 回傳給定 s[index:] 的範圍內 , 是否可以被 wordDict 全部切完
        def backtracking(index : int , memo :dict[int:bool])-> bool : 
            
            if index == size : return True

            if index in memo : return memo[index] 
            cur = ""
            breakable = False
            for j in range(index , size): 
                cur += s[j] 
                if cur in word_set : 
                    breakable = breakable or backtracking(index+len(cur) , memo)
            memo[index] = breakable
            return breakable
        
        return backtracking(0 ,memo )




if __name__ == "__main__":
    c = Solution()

    # (s, wordDict, 預期, 說明)
    test_set = [
        ("leetcode", ["leet", "code"], True, "官方範例:切成 leet + code"),
        ("applepenapple", ["apple", "pen"], True, "官方範例:apple 用了兩次"),
        (
            "catsandog",
            ["cats", "dog", "sand", "and", "cat"],
            False,
            "官方範例:每種切法最後都剩下 og",
        ),
        ("a", ["a"], True, "邊界:單一字母,字典有這個字"),
        ("a", ["b"], False, "邊界:單一字母,字典沒有"),
        ("cars", ["car", "ca", "rs"], True, "ca + rs,car 接不下去"),
        ("abcd", ["a", "abc", "b", "cd"], True, "a + b + cd"),
        ("aaaaaaa", ["aaaa", "aaa"], True, "4 + 3,字典單字可以湊成 7"),
        ("aaaaaaa", ["aaaa", "aa"], False, "4 和 2 都是偶數,湊不出長度 7"),
        ("bb", ["a", "b", "bbb", "bbbb"], True, "兩個 b 各用一次"),
        ("dogcatcat", ["dog", "cat"], True, "cat 連續使用兩次"),
    ]

    for s, word_dict, expected, note in test_set:
        result = c.wordBreak(s, list(word_dict))
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       s={s!r} | wordDict={word_dict} | expected={expected} | got={result}")
