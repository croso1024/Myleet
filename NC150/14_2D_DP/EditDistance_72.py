"""
    題意 :
    給定兩個字串 word1 與 word2。
    把 word1 變成 word2,每次可以插入、刪除或替換一個字母。
    回傳最少需要幾次操作。

    LeetCode 72 · Medium
    URL : https://leetcode.com/problems/edit-distance/

    Example :
    word1 = "horse",     word2 = "ros"       -> 3
    word1 = "intention", word2 = "execution" -> 5

    Constraint :
    0 <= word1.length, word2.length <= 500
    word1 與 word2 只含小寫英文字母

    思路 :
        這題看的出來示標準 2D DP , 需要拿題目的範例在紙上演示一次流程
      h o r s e 
    r 1 2 2 3 4 
    o 2 1 2 3 4 
    s 3 2 3 2 3

    題目要的是 , 最少需要幾次操作 (新增/刪除/修改) , 能把兩個字轉成一模一樣, 採用dp的想法. 
    那就是 dp[i][j] 代表 word1[:i+1] 和 word2[:j+1] 這兩個子字串要轉為一樣的最小步數 , dp陣列的右下角就是題目要的答案. 

    而 dp[i][j] 的情況可以分為
    
    1. word1[i] == word2[j] , 則相當於兩個子字串在 i / j 這組字上不用做任何替換,可以直接等價各縮一格的子字串 (也就是矩陣左上角) 的最小移動步數.
    2. word1[i] != word2[j] , 則這一格鐵定要做一次變換了 , 相當於去比較 word1[:i] 與 word2[:j+1] 這組 v.s. word1[:i+1] 與 word2[:j] 這組配對誰更小再 +1 
    實際例子用題目的 horse / ros ,在 dp 右下角 , dp[2][4] , 其實就是比較 horse & ro 的步數與 hors & ros 的步數誰少,然後再+1 (處理新增的那個字)

    因此 dp[i][j] 的來源,源自 dp[i-1][j] / dp[i][j-1] / dp[i-1][j-1]  其中之一.
    針對第一列/第一欄 , 沒有甚麼特殊規則,只需要處理邊界情況即可. 因此可以順順雙迴圈掃過整個棋盤格 

    複雜度 : 
    時間複雜度 , 因為要掃過一輪 , 設 len(word1) = m , len(word2) = n , 
    時間複雜度為 O(m x n) , 空間複雜度也示 O(m x n) , 但如果做狀態壓縮, 可以壓到 O( min(m,n) )

    Trade-off :


"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        m , n = len(word1) , len(word2) 
        if m == 0 or n == 0 : 
            return max(m,n)

        dp = [ [None for _ in range(n)] for _ in range(m) ]
        dp[0][0] = 0 if word1[0] == word2[0] else 1
        hit = bool(dp[0][0] == 0)

        # 先填好第一列與第一行,迴圈內比較乾淨 
        for i in range(1,n) : 
            if word1[0] == word2[i] and not hit : 
                dp[0][i] = dp[0][i-1] 
                hit = True 
            else : 
                dp[0][i] = 1 + dp[0][i-1]
        
        hit = bool(dp[0][0] == 0)
        for i in range(1,m): 
            if word1[i] == word2[0] and not hit : 
                dp[i][0] = dp[i-1][0] 
                hit = True 
            else : 
                dp[i][0] = 1 + dp[i-1][0]


        for i in range(1,m) :
            for j in range(1,n) : 

                if word1[i] == word2[j] : dp[i][j] = dp[i-1][j-1] 
                else : 
                    dp[i][j] = 1 + min(
                        dp[i-1][j],
                        dp[i][j-1],
                        dp[i-1][j-1]
                    )

        return dp[m-1][n-1]                    

if __name__ == "__main__":
    c = Solution()

    # (word1, word2, 預期, 說明)
    test_set = [
        ("horse", "ros", 3, "官方範例:horse -> ros"),
        ("intention", "execution", 5, "官方範例:intention -> execution"),
        ("", "", 0, "邊界:兩串都是空的"),
        ("a", "", 1, "刪掉唯一的字母"),
        ("", "a", 1, "插入一個字母"),
        ("a", "a", 0, "已經相同"),
        ("a", "b", 1, "替換一個字母"),
        ("abc", "abc", 0, "整串相同"),
        ("kitten", "sitting", 3, "替換、替換、插入"),
        ("sea", "eat", 2, "刪掉 s,插入 t"),
    ]

    for word1, word2, expected, note in test_set:
        result = c.minDistance(word1, word2)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       word1={word1} word2={word2} | expected={expected} | got={result}")
