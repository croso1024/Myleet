"""
    題意 :
    給定兩個字串 text1 與 text2。回傳最長公共子序列的長度。
    子序列不必連續,但留下的字母必須保持原本的相對順序。
    沒有公共子序列就回傳 0。

    LeetCode 1143 · Medium
    URL : https://leetcode.com/problems/longest-common-subsequence/

    Example :
    text1 = "abcde", text2 = "ace" -> 3
    text1 = "abc",   text2 = "abc" -> 3
    text1 = "abc",   text2 = "def" -> 0

    Constraint :
    1 <= text1.length, text2.length <= 1000
    text1 與 text2 只含小寫英文字母

    思路 :
    這一題直接想不好思考,需要紙筆繪製出2D DP的狀態轉移圖.
    以題目給定的作為例子來繪製就很明瞭.

      a b c d e 
    a 1 1 1 1 1 
    c 1 1 2 2 2
    e 1 1 2 2 3
    
    表格中 (i,j) 格的解, 就依據 text2 的第i個字 , 是否與 text1 的第 j 個字相符來分岔.
    舉例 (1,2) 這格 , text2 的 c 和 text1 的 c match, 則此時 (1,2) 的值等於 1+ (1-1 , 2-1) 
    因為此時相當 text1,text2都取在不考慮c的情況下,能有的LCS. 

    如果沒有Match,例如 (2,2) 這格 c和e 不match. 
    則 (2.2) 這格所代表的 abc v.s. ace , 各退一格就是
    [abc] v.s. [ac] & [ab] v.s. [ace] , 需要從 (1,2) 和 (2,1) 去看最大LCS
    
    總結上述兩條規則,每一格要參考的,就是左上,上方,左方三格. 
    而針對第一排,第一列的計算,可以預先算好

    複雜度 : 
    時間複雜度為O(s1 x s2) , 棋盤每一格都要走一次
    空間複雜度也為 O(s1 x s2) , 每一格儲存一個值, 極端情況就是做壓縮. 

    Trade-off :

"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        s1 , s2 = len(text1) , len(text2) 
        dp = [ [None for _ in range(s1)] for _ in range(s2)] 

        # 處理第一列/第一行
        c = 0 
        for i in range(s1) : 
            if text2[0] == text1[i] : c = c+1  
            dp[0][i] = min(1,c) 
        
        c = 0 
        for j in range(s2) : 
            if text1[0] == text2[j] : c += 1 
            dp[j][0] = min(1,c) 
        
        # 完成初始化,接著走填表.
        # 每一格要參考的就是左上/左/上 , 因此走正常雙層 loop 即可
        for i in range(1 , s2 ) : 
            for j in range(1 , s1 ) : 

                # 先比較 text1[j] 和 text2[i] , 命中就是 1 + 內縮一格
                if text1[j] == text2[i] : 
                    dp[i][j] = 1 + dp[i-1][j-1] 
                else : 
                    dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
        
        return dp[s2-1][s1-1]
                    
                    





if __name__ == "__main__":
    c = Solution()

    # (text1, text2, 預期, 說明)
    test_set = [
        ("abcde", "ace", 3, "官方範例:ace"),
        ("abc", "abc", 3, "官方範例:兩串相同"),
        ("abc", "def", 0, "官方範例:沒有共同字母"),
        ("a", "a", 1, "邊界:單字母相同"),
        ("a", "b", 0, "邊界:單字母不同"),
        ("abc", "c", 1, "共同字母在尾端"),
        ("abc", "ac", 2, "跳過中間的 b"),
        ("aggtab", "gxtxayb", 4, "gtab"),
        ("bsbininm", "jmjkbkjkv", 1, "只能取一個 b 或一個 m"),
    ]

    for text1, text2, expected, note in test_set:
        result = c.longestCommonSubsequence(text1, text2)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       text1={text1} text2={text2} | expected={expected} | got={result}")
