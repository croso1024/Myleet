
""" 
    思路 : 
        這一題是經典的DP題 ,因為要比較兩個字串 ,比較直觀的想法是定義dp table為

        這一題會需要從空字串開始 , 因此table的定義會是  len(text1)+1  x len(text2)+1
        
        dp[i][j] : text1[0:i] 與 text2[0:j] 的Longest common subsequence 
        base case就是  dp[:][0] 和 dp[0][:] 為0 , 因為其中一方是空字串 

        最終 , 本題核心難點在於找狀態轉移方程式 , 我們的目標是要推導到dp-table右下 , 即兩邊都是完整字串的情況       
        
        思考DP狀態轉移的思路 :
        以題目給的例子來說 , 假設我們要找 "ace"和"abcde"的LCS
         
        依據表格形狀和basecase , 我們大概可以知道的有 
        1. "ac"和"abcd"的LCS
        2. "ace"和"abcd"的LCS 
        3. "ac"和"abcde"的LCS   
        
        要找"ace"和"abcde"的LCS  
        看起來如果 text1[i] == text2[j] , 則LCS 會是 case1 + 1 
        但如果不等於的話 , 那就等於上面或左邊的最大值 , 注意值不會超過 min( i , j ) 即較小那個字串的長度
        
        !!! 建議用題目例子的"ace" , "abcde" 加上空字串實際畫在紙上 , 同時填滿表格
        我用了"ace" , "abcde" /  "acb" , "aac" / "abc" , "bca" 三組畫出來測試
        
        
        所推出的狀態轉移方程式 : 

        Case.1 if text1[i] == text2[j] :  
        
            dp[i][j] = 1 + dp[i-1][j-1] (沒有加上他們兩個之前的LCS) 

        Case.2 if text1[i] != text2[j] :           
        
            dp[i][j] = max(dp[i-1][j] , max[i][j-1])
            
        最後走正向尋訪結束
"""



""" 
    解法一. 依照上面的思路 
"""
class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # create table : (len(text1) + 1) x (len(text2) + 1) , fill with zero
        dp =  [   [0  for j in range(len(text2)+1)  ]    for i in range(len(text1)+1)  ]

        # 注意我們的dp-table index的定義和原始字串的偏差 , 接下來對dp-table從dp[1][1]開始正序尋訪
        
        for i in range(1 , len(text1)+1): 
            
            for j in range(1 , len(text2)+1): 
                
                
                if text1[i-1] == text2[j-1] : 
                
                    dp[i][j] = 1 + dp[i-1][j-1] 
                
                else : 
                    # 如果字不相等 , 那dp[i][j]就是左邊或上面的最大值
                    dp[i][j] = max( dp[i-1][j] , dp[i][j-1] )
                    
                    # 書上有提到 , 會進入這個else的情況稱為" 至少有一個字元不屬於LCS "
                    # 因此 dp[i-1][j] 代表了text1[i]不在LCS , dp[i][j-1] 則是text2[j]不在LCS
                    # 有些人會考慮到那會不會有兩者都不在LCS的情況 需要 把dp[i-1][j-1]也納入max
                    # 從問題本身想 , 多了一個字元頂多就是不增加LCS ,
                    # 因此dp[i-1][j-1]一定不會大於dp[i-1][j]或dp[i][j-1]
                    
        
        return dp[len(text1)][len(text2)]

test_case = ["abcde" , "acede"]
S = Solution() 
S.longestCommonSubsequence(*test_case )

""" 
    解法二. 書本上首先示範的 , top-down的邏輯 , 我自己再加入memo 
    速度和空間不如解法一的遞推
"""
class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        memo = dict()

        # 返回 text1[0:i] 和 text2[0:j]的LCS
        # 注意i,j 是開區間 , 如同上面的list slice 
        def dp(i,j,memo): 

            # base case , 有一方是空字串
            if i==0 or j==0 : return 0
            
            elif (i,j) in memo : return memo[(i,j)]
            
            else : 
                if text1[i-1] == text2[j-1] : 
                    result =  1 + dp(i-1, j-1 , memo)
                else : 
                    result = max( dp(i-1,j , memo) , dp(i,j-1,memo)  )

                memo[(i,j)] = result 
                return result
        
        return dp( len(text1) , len(text2) , memo )
                