"""
    題意 :
    有一個 m 列 n 行的格子。機器人從左上角出發,每次只能往右或往下走一步。
    要走到右下角。回傳一共有幾條不同的路徑。

    LeetCode 62 · Medium
    URL : https://leetcode.com/problems/unique-paths/

    Example :
    m = 3, n = 7 -> 28
    m = 3, n = 2 -> 3

    Constraint :
    1 <= m, n <= 100

    思路 :
    Naive的DP題目 ,可以走Top-down遞迴也可以Bottom up填表. 
    已知 1 <= m , n <= 100 , 因為只能往右或著往下走. 
    因此粗抓最多200步內,不會導致遞迴炸裂

    複雜度 : 
    第一種解法,每一格只會算一次, 時間複雜度O(m x n) , 空間複雜度 O(m x n) 儲存所有解的答案
    第二種解法,時間複雜度與空間複雜度概念上等同第一種,但實際情況更優

    Trade-off :

"""
from typing import Tuple , Dict 

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        #　儲存到達 (i,j) 格有幾種做法. 
        lookup_table :Dict[Tuple[int,int] , int] = {}
        
        # Given , 到達 i,j 格的方法數 : 到達 i-1,j 格的方法數 + 到達 i,j-1 格的方法數
        def dp(i,j) -> int : 

            if (i,j) in lookup_table : return lookup_table[(i,j)] 

            # 特殊情況是在第一列或第一行
            if i == 1 and j == 1 : 
                step = 1 
            elif i == 1 : 
                step =  dp(i,j-1)
            elif j == 1 : 
                step = dp(i-1,j) 

            # 常規情況就是到達左側的方法數 + 到達上方的方法數
            else : 
                step = dp(i-1,j) + dp(i,j-1) 
            
            # 紀錄寫進lookup table,後面遞迴可以直接走. 
            lookup_table[(i,j)] = step 
            return step 

        return dp(m,n) 

# 解法二,就走建表的方式
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # 建立二維表格
        table = [ [None for j in range(n)] for i in range(m) ]

        # 開始填充所有格子 , 照一般雙層迴圈順序,先走訪同一列的每一行,再換下一列即可

        for i in range(m) : 
            for j in range(n) : 

                # 只要是在第一行or第一列 ,都只有一種方法 
                if i == 0 or j == 0  : 
                    table[i][j] = 1 
                
                # 剩餘的,按照走訪順序填充即可 
                # Given i >= 1 and j >= 1 , 走訪迴圈順序不會爆炸
                else : 
                    table[i][j] = table[i-1][j] + table[i][j-1] 
        

        return table[m-1][n-1] 





if __name__ == "__main__":
    c = Solution()

    # (m, n, 預期, 說明)
    test_set = [
        (3, 7, 28, "官方範例:3x7"),
        (3, 2, 3, "官方範例:3x2,三條路"),
        (1, 1, 1, "邊界:已經在終點"),
        (1, 3, 1, "只有一列,只能一直往右"),
        (3, 1, 1, "只有一行,只能一直往下"),
        (2, 2, 2, "先右再下,或先下再右"),
        (2, 3, 3, "2x3"),
        (3, 3, 6, "3x3"),
        (7, 3, 28, "與 3x7 對稱"),
    ]

    for m, n, expected, note in test_set:
        result = c.uniquePaths(m, n)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       m={m} n={n} | expected={expected} | got={result}")
