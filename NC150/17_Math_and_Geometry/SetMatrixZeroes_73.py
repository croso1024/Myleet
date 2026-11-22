"""
    題意 :
    給定一個 m x n 的整數矩陣 matrix。
    若某個元素為 0,就把它所在的「整列」與「整行」全部設為 0。
    必須 in-place 修改,不要回傳任何東西。

    Follow up :
    - 直接用 O(mn) 額外空間的做法通常不是好主意。
    - 用 O(m + n) 額外空間有改善,但仍不是最好的。
    - 能不能只用 O(1) 額外空間?

    LeetCode 73 · Medium
    URL : https://leetcode.com/problems/set-matrix-zeroes/

    Example :
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
        -> [[1,0,1],[0,0,0],[1,0,1]]
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
        -> [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

    Constraint :
    m == matrix.length
    n == matrix[0].length
    1 <= m, n <= 200
    -2^31 <= matrix[i][j] <= 2^31 - 1

    思路 :
    用 O(m+n) 的方案,我的理解是走訪一次之後紀錄下來那些列 / 行需要被改0 , 這樣只有 O(m+n) 空間就可以.
    但這一提的 Follow up 是需要能走 O(1) 空間. 
    直覺的作法就是 , 一旦遇到0就做一次展開歸0即可. 但直接這樣做會導致後面需要不斷展開歸 0 
    我的一個想法是 , 遇到 0 , 不馬上展開但在原始陣列上做標記 , 這樣就可以達到真的 O(1) 空間 ,　也不需要瘋狂展開歸0 ,
    時間複雜度上 , 需要做一次 matrix 掃描 , 每次展開也要 O(m+n) 操作. 但展開不會重複做.因此極端情況應該只有斜角個要展開 O( max(m,n) ) 要展開
    所以, 最終時間複雜度是 O(m x n) 掃描 + O( max(m,n) * (m+n) ) + 替換 O(m x n) , 空間複雜度 O(1) 
    

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List

# Solution : 1 ( 走 O(m+n) , 也就是在走訪過程去紀錄那些列/行要改 ) ) 
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m , n = len(matrix ) , len(matrix[0])

        zero_r = set()
        zero_c = set()
        # step.1 捕捉要改的
        for i in range( m ) : 
            for j in range(n): 
                if matrix[i][j] == 0 : 
                    zero_c.add(j) 
                    zero_r.add(i) 

        # step.2 Inplace 修改 
        for r in zero_r :  
            for j in range(n): 
                matrix[r][j] = 0 
        
        for c in zero_c : 
            for i in range(m): 
                matrix[i][c] = 0 
        
        return 

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m , n = len(matrix) , len(matrix[0])

        def _mark(r:int,c:int):  

            # mark the r-th row and c-th column until next "0" 
            for i in range(n): 

                if matrix[r][i] == 0: continue 
                else : matrix[r][i] = "m"
                
            for i in range(m): 

                if matrix[i][c] == 0 : continue 
                else : matrix[i][c] = "m"

        # Step.1 Mark 
        for i in range(m):
            for j in range(n) : 
                if matrix[i][j] == 0 : _mark(i,j) 
        
        # Step.2 In-Place : 
        for i in range(m):
            for j in range(n) : 
                if matrix[i][j] == "m" : matrix[i][j] = 0 

        return                 
            


if __name__ == "__main__":
    c = Solution()

    # (matrix, 預期修改後的 matrix, 說明)
    # 每次呼叫都複製 matrix,實作改到測資本身不會留到下一題
    test_set = [
        (
            [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
            [[1, 0, 1], [0, 0, 0], [1, 0, 1]],
            "官方範例:中心一個 0",
        ),
        (
            [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
            [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]],
            "官方範例:第一列有兩個 0",
        ),
        ([[1, 2], [3, 4]], [[1, 2], [3, 4]], "沒有任何 0,矩陣不變"),
        ([[0, 0], [0, 0]], [[0, 0], [0, 0]], "全部都是 0"),
        ([[0]], [[0]], "邊界:1x1 且為 0"),
        ([[5]], [[5]], "邊界:1x1 且非 0"),
        ([[1, 0, 3]], [[0, 0, 0]], "邊界:單一列,中間有 0"),
        ([[1], [0], [3]], [[0], [0], [0]], "邊界:單一行,中間有 0"),
        (
            [[0, 1, 1], [1, 1, 1], [1, 1, 1]],
            [[0, 0, 0], [0, 1, 1], [0, 1, 1]],
            "只有左上角 (0,0) 是 0",
        ),
        (
            [[1, 0, 1], [1, 1, 1], [1, 1, 1]],
            [[0, 0, 0], [1, 0, 1], [1, 0, 1]],
            "唯一的 0 在第一列,但不在第一行",
        ),
        (
            [[1, 1, 1], [0, 1, 1], [1, 1, 1]],
            [[0, 1, 1], [0, 0, 0], [0, 1, 1]],
            "唯一的 0 在第一行,但不在第一列",
        ),
        (
            [[1, 0, 1], [1, 1, 1], [0, 1, 1]],
            [[0, 0, 0], [0, 0, 1], [0, 0, 0]],
            "兩個 0 分別落在不同的列與行",
        ),
        (
            [[-1, 2], [3, 0]],
            [[-1, 0], [0, 0]],
            "含負數,只有值恰為 0 的格子會觸發",
        ),
        (
            [[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]],
            [[0, 0, 3, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
            "4x4,三個 0 分散在不同位置",
        ),
    ]

    for matrix, expected, note in test_set:
        actual = [row[:] for row in matrix]
        c.setZeroes(actual)
        passed = actual == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       input   ={matrix}")
        print(f"       expected={expected}")
        print(f"       got     ={actual}")
