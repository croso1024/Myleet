"""
    題意 :
    給定一個 m x n 的整數矩陣 matrix,
    請依照「順時針螺旋順序 (spiral order)」回傳矩陣中的所有元素。

    LeetCode 54 · Medium
    URL : https://leetcode.com/problems/spiral-matrix/

    Example :
    matrix = [[1,2,3],[4,5,6],[7,8,9]]             -> [1,2,3,6,9,8,7,4,5]
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]    -> [1,2,3,4,8,12,11,10,9,5,6,7]

    Constraint :
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 10
    -100 <= matrix[i][j] <= 100

    思路 :

    這一題用筆在紙上演練 , 可以劃出 , 給定 m x n 的矩陣. 

    === 以下為第一版想法 , 但實作時有點卡 ===
    第一步驟是向右 (0,1) 走 n 步 ,
    接著向下 (1,0) , 走 m-1 步 , 
    再來向左 (0,-1) , 走 n-1 步 ,
    最後向上 (-1,0) , 走 m - 2 步,  回到往右繼續迭代. 

    所以陣列是 [ n , m - 1 , n - 1 , m - 2 ... ] 一直到扣成0 
    即使給定陣列是寬/直的也相同. 
    所以先寫出這個陣列 step , 再按照右->下->左->上 , 的順序遍歷 step[i] 步即可.
    === 

    第二版的想法 , 不是看這一輪抓進幾個元素 , 而是看"跳幾格" , 
    這樣解決的是 , 起始位置算不算該輪要加入的位置這件事 , 因為算進去的話 , 那每一條邊都會有重複元素. 
    因此改為想 "跳幾格" , 就不會有重複.
    matrix[0][0] 直接先加入答案 , 之後 , 第一列要跳的格數 = n-1 , 最後一行要跳 m - 1 , 

    跳格的陣列變為 [ n-1 , m-1 , n-1 , m-2 , .... ] 扣到 0 表示不用跳

    時間複雜度 : 
        建立 Step 陣列 O( min(M,N) ) , 
        走訪 : O(MxN) 
    空間複雜度 : 
        Step 陣列 O( min(M,N)) , 
        用來做答案的輔助空間 O(MxN)




    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m , n = len(matrix) , len(matrix[0])
        results = [ matrix[0][0] ] 

        steps = [n-1] 
        for i in range(1, min(m,n)+1 ) :
            steps.append( m - i ) 
            steps.append( n - i ) 
        # 得到步數陣列. 
        # 接著開始走 Dir 
        DIR = [(0,1) , (1,0) , (0,-1) , (-1,0)] 

        # 每一輪沿著  DIR[ count % 4 ]   開始走 step[i] 步 , 到了就換一個方向
        count = 0 
        cx , cy  = 0,0 
        for step in steps :
            
            dx , dy = DIR[count % 4]
            # 這一輪走 step 步
            for i in range(step): 
                cx = cx + dx 
                cy = cy + dy
                results.append(matrix[cx][cy]) 
                
            # 把最後一格拆掉
            count += 1 
            if len(results ) == m * n : break 
        return results



if __name__ == "__main__":
    c = Solution()

    # (matrix, 預期, 說明)
    # 每次呼叫都複製 matrix,實作改到測資本身不會留到下一題
    test_set = [
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [1, 2, 3, 6, 9, 8, 7, 4, 5],
            "官方範例:3x3 方陣",
        ),
        (
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
            "官方範例:3x4 寬矩陣",
        ),
        ([[42]], [42], "邊界:1x1 單一元素"),
        ([[1, 2, 3, 4]], [1, 2, 3, 4], "邊界:1x4 單列,不能重複走回頭路"),
        ([[1], [2], [3], [4]], [1, 2, 3, 4], "邊界:4x1 單欄,不能重複走回頭路"),
        ([[1, 2], [3, 4]], [1, 2, 4, 3], "2x2 偶數方陣"),
        ([[1, 2, 3], [4, 5, 6]], [1, 2, 3, 6, 5, 4], "2x3 兩列寬矩陣"),
        ([[1, 2], [3, 4], [5, 6]], [1, 2, 4, 6, 5, 3], "3x2 兩欄長矩陣"),
        (
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
            [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10],
            "4x4 偶數方陣,兩層完整螺旋",
        ),
        ([[-100, 0], [100, -1]], [-100, 0, -1, 100], "邊界值:含負數與 0"),
    ]

    for matrix, expected, note in test_set:
        result = c.spiralOrder([row[:] for row in matrix])
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       expected={expected}")
        print(f"       got     ={result}")
