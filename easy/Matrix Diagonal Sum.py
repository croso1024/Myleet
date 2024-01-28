from typing import List 

""" 
    思路: 
        給定一個array , 這題要計算array的對角線加總 
        比較直覺的作法就是分兩段loop做加總 , 如果array的size為奇數,那中間的值會被加到兩次需要扣掉
        
        速度不好,但空間不錯 , 不過這個解法就是O(N)了
        
"""

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        size = len(mat) 
        sol = 0 
        # primary diagonal sum and secondary diagonal sum: 

        for i in range(size): 
            sol +=  (mat[i][i]  + mat[i][size-1-i] ) 
        
        # 如果size是奇數 , 還需要再減去重複計算的part
        if size % 2 == 1 : 
            sol -= mat[size//2][size//2] 
            
        return sol 
            
    