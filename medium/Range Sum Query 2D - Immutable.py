""" 
    題意:
        我們要實現一個class ,在給定一個matrix進行初始化後
        提供一個界面 , 讓我們可以快速取得從指定左上角到右下角範圍內的元素和 
        
    思路:
        最naive當然是O(N)解法 , 比較好一點就是 single dimension prefix sum , 這樣可以使用O(N)來得到解
        但這一題顯然是要讓我們做 2D prefix sum , 題目也要求O(1) TC
        
        2D prefix sum , 那我們要以左上角為基準 , 再要計算任何一塊時 , 我們可以將目標方塊的右下角與matrix左上角一併納入
        最後變成四個部份 , 以右下部份為我們的答案

        - 在計算從左上角到 (i,j) 的 range sum的時候,我們需要 :
        
            左上角到 (i-1,j) 的 range sum + 左上角到 (i,j-1)的range sum - 左上角到(i-1,j-1)的rangeSum + matrix[i][j]
          
        - 有了所有格子的 range sum後(都是以左上為基準) , 快速計算特定範圍range sum ex. (i1,j1,i2,j2) 
        
            rangeSum(i2,j2) - rangeSum( i1-1 , j2 ) - rangeSum( i2 , j1-1 ) + rangeSum( i1-1 , j1-1 ) 
        

"""
from typing import List 

""" 
    解法一. Follow 上述思路 , 時間空間都很不錯
"""
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        self.M = len(matrix) 
        self.N = len(matrix[0])
        # Create rangeSum matrix : M X N 
        self.rangeSum = [ [None for i in range(self.N) ] for j in range(self.M) ]

        # 第一步驟, 建立rangeSum矩陣 

        # 對於第一列與第一行來說 , 就只是一維prefix sum , 我把他們單獨建立出來方便待會用單一規則建立整體的rangeSum
        prefix_sum = 0 
        for i in range(self.N): 
            prefix_sum += matrix[0][i] 
            self.rangeSum[0][i] = prefix_sum 
        
        prefix_sum = 0 
        for i in range(self.M): 
            prefix_sum += matrix[i][0] 
            self.rangeSum[i][0] = prefix_sum 
            
        # 計算 左上角到 (i,j)的rangeSum : 
        # 左上角到 (i-1,j) 的 range sum + 左上角到 (i,j-1)的range sum - 左上角到(i-1,j-1)的rangeSum + matrix[i][j]
        for i in range(1 , self.M): 
            
            for j in range(1,self.N): 
                
                self.rangeSum[i][j] = self.rangeSum[i-1][j] + self.rangeSum[i][j-1] - self.rangeSum[i-1][j-1] + matrix[i][j]
        
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        
        if row1 == 0 and col1 == 0 :  
            
            return self.rangeSum[row2][col2]
        
        elif row1 == 0 : 
            
            return self.rangeSum[row2][col2] - self.rangeSum[row2][col1-1]
            
        elif col1 == 0 : 
            
            return self.rangeSum[row2][col2] - self.rangeSum[row1-1][col2]
        
        else : 
        
            return self.rangeSum[row2][col2] - self.rangeSum[row1-1][col2]- self.rangeSum[row2][col1-1] + self.rangeSum[row1-1][col1-1]
        
        
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)