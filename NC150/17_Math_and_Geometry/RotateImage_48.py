"""
    題意 :
    給定一個 n x n 的 2D 矩陣 matrix,代表一張影像。
    請將影像「順時針旋轉 90 度」。

    必須「原地 (in-place)」修改輸入的矩陣,
    不可以另外配置一個 2D 矩陣來做旋轉。函式不需回傳值。

    LeetCode 48 · Medium
    URL : https://leetcode.com/problems/rotate-image/

    Example :
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
        -> [[7,4,1],[8,5,2],[9,6,3]]
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        -> [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

    Constraint :
    n == matrix.length == matrix[i].length
    1 <= n <= 20
    -1000 <= matrix[i][j] <= 1000

    思路 :
    這一題應該是在考旋轉的鏡射操作 , 先做矩陣轉置 ,接著再看要順時針或是逆時針轉.
    做不同操作 : 
    順時針轉 : 把每一個單列內的元素做反轉 
    逆時針轉 : 把列的順序反轉 : e.g. 第0列變為最後一列 

    時間複雜度 : 對每個元素的操作 O(MxN) 
    空間複雜度 : IN-place 操作 , 沒有額外空間

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        

        # Step.1 轉置 : 
        m = len(matrix)

        for i in range(1 , m) : 
            for j in range(i) :
                matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]
        
        # Step.2 , 反轉每一個 row 

        for i in range(m) : 

            # 拿出一個 row
            row = matrix[i] 
            l , r = 0 , m - 1 

            while l < r : 

                row[l] , row[r] = row[r] , row[l]
                l += 1 
                r -= 1 

            # # 反轉該 row 
            # for j in range(m // 2) : 
            #     row[j] , row[ m - j - 1] = row[m-j - 1]  , row[j]
        
        return 



if __name__ == "__main__":
    c = Solution()

    # (matrix, 預期旋轉後的 matrix, 說明)
    # 本題是原地修改:每次複製一份 matrix 傳入,呼叫後直接檢查那份複本
    test_set = [
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[7, 4, 1], [8, 5, 2], [9, 6, 3]],
            "官方範例:3x3 方陣",
        ),
        (
            [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
            [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]],
            "官方範例:4x4 方陣",
        ),
        ([[1]], [[1]], "邊界:1x1,旋轉後不變"),
        ([[1, 2], [3, 4]], [[3, 1], [4, 2]], "2x2:只有一層,一次四格交換"),
        (
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
            [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]],
            "4x4 偶數邊長:兩層,沒有中心格",
        ),
        (
            [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [21, 16, 11, 6, 1],
                [22, 17, 12, 7, 2],
                [23, 18, 13, 8, 3],
                [24, 19, 14, 9, 4],
                [25, 20, 15, 10, 5],
            ],
            "5x5 奇數邊長:兩層加中心格,中心 13 不動",
        ),
        ([[1, 1], [2, 2]], [[2, 1], [2, 1]], "含重複值,不能靠數值判斷位置"),
        (
            [[-1000, 1000], [0, -1]],
            [[0, -1000], [-1, 1000]],
            "邊界值:數值上下限與負數",
        ),
    ]

    for matrix, expected, note in test_set:
        working = [row[:] for row in matrix]
        returned = c.rotate(working)
        passed = working == expected and returned is None
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       expected={expected}")
        print(f"       got     ={working}")
        if returned is not None:
            print(f"       注意:題目要求不回傳值,但回傳了 {returned!r}")
