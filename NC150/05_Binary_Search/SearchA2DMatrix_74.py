"""
    題意 :
    給定一個 m x n 的整數矩陣 matrix,它具有以下兩個性質 :
      - 每一列(row)由左至右為非遞減排序。
      - 每一列的第一個整數,都大於前一列的最後一個整數。

    再給定一個整數 target,若 target 存在於 matrix 中回傳 True,否則回傳 False。

    必須寫出 O(log(m*n)) 的演算法。

    LeetCode 74 · Medium
    URL : https://leetcode.com/problems/search-a-2d-matrix/

    Example :
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3  -> True
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13 -> False

    Constraint :
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 100
    -10^4 <= matrix[i][j], target <= 10^4

    思路 :

    很標準的2D Binary Search. 
    每一列都是非遞減排序, 
    第二列任何元素都大於下一列元素. ( 不是大於等於 , 是大於 ) 
    現在要問 , 給訂一個整數 , 確認這個整數是否在這個2D陣列中. 

    把列攤開來可能像是 : 
    [(a_1,...,a_n) , (b_1,...,b_n) , (c_1,...c_n) ] , 其中  b_1 > a_n , c_1 > b_n 
    第一個 Binary Search用來找到是否有落盤在這些區間. 若沒有可以直接回False , 有就往下找 O(LogM)
    第二個 Binary Search用來找是否在區間內

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m , n = len(matrix) , len(matrix[0]) 

        # First diemension 
        left , right = 0 , m - 1 

        while left <= right : 

            mid = (right+left)//2 

            row = matrix[mid] 

            if row[0] == target or row[-1] == target : return True 
            # 進入第二層的Binary Search, 這裡找不到就是無解 
            elif row[0] < target < row[-1] : 

                inner_left , inner_right = 0 , n-1 
                
                while inner_left <= inner_right : 

                    inner_mid = (inner_right+inner_left)//2 
                    value = row[inner_mid] 

                    if value == target : return True 
                    elif value > target : inner_right = inner_mid - 1 
                    elif value < target : inner_left = inner_mid + 1 
                
                return False 

            # 若此列第一個元素 > target , 代表 target 在更上的Row 
            elif row[0] > target : 
                right = mid - 1 
            # 若 target大於此列最後一個元素 , 代表 target 在更往下的 Row 
            elif row[-1] < target : 
                left = mid + 1 
        
        return False 



if __name__ == "__main__":
    c = Solution()

    M = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]

    # (輸入參數 tuple, 預期輸出) —— LeetCode 官方範例 + 邊界案例
    test_set = [
        ((M, 3), True),
        ((M, 13), False),
        ((M, 1), True),                                 # 命中整個矩陣的最小值
        ((M, 60), True),                                # 命中整個矩陣的最大值
        ((M, 7), True),                                 # 命中某列的最後一格
        ((M, 10), True),                                # 命中某列的第一格
        ((M, 0), False),                                # target 小於所有元素
        ((M, 61), False),                               # target 大於所有元素
        (([[1]], 1), True),                             # 邊界:1x1 命中
        (([[1]], 2), False),                            # 邊界:1x1 未命中
        (([[1, 3, 5]], 5), True),                       # 邊界:單列
        (([[1, 3, 5]], 4), False),
        (([[1], [3], [5]], 3), True),                   # 邊界:單行
        (([[1], [3], [5]], 4), False),
        (([[-10, -5], [0, 7]], -5), True),              # 含負數
        (([[-10, -5], [0, 7]], -7), False),
    ]

    for args, expected in test_set:
        result = c.searchMatrix(*args)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={args} | expected={expected} | got={result}")
