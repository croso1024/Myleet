from typing import List 

# use two hashmap to store the row & column that must be zero
# so overall we can traverse the matrix 2 times , first for hashmap , second to modify
# take O(n+m) space , O(mn) time complexity
class Solution:

    def setZeroes(self, matrix: List[List[int]]) -> None:

        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroRow = set() 
        zeroColumn = set() 
        
        for i in range(len(matrix)):
            
            for j in range(len(matrix[0])) : 
                
                if matrix[i][j] == 0 : 
                    zeroRow.add(i)
                    zeroColumn.add(j) 
        
        for i in range(len(matrix)):
            
            for j in range(len(matrix[0])) : 
                
                if i in zeroRow or j in zeroColumn:
                    matrix[i][j] = 0 
        
        return 

# 要做到constant space complexity , 是透過原始array協助進行儲存來達成
# 我們把遇到有0的改為儲存在first row , first column
# time complexity : O(n) + O(m) + O(nm) + O(nm) + O(n) + O(m) => O(nm)
# O(1) extra space complexity ,
class Solution : 
    
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        firstRowZero = False 
        firstColumnZero = False

        for i in range(len(matrix)): 
            if matrix[i][0] == 0: firstColumnZero = True 
        for i in range(len(matrix[0])): 
            if matrix[0][i] == 0 : firstRowZero = True  
        
        for i in range(1 , len(matrix)): 
            
            for j in range(1 , len(matrix[0])) : 
                
                if matrix[i][j] == 0 : 
                    
                    matrix[i][0] = 0 
                    matrix[0][j] = 0 
        
        for i in range(1 , len(matrix)):   
            
            if matrix[i][0] == 0 : 
                for j in range(1 , len(matrix[0])):matrix[i][j] = 0
        
        for i in range(1 , len(matrix[0])):          
            if matrix[0][i] == 0 :  
                for j in range(1 , len(matrix)): matrix[j][i] = 0  
        
        if firstColumnZero : 
            for i in range(len(matrix)):
                matrix[i][0] = 0 
        
        if firstRowZero : 
            for i in range(len(matrix[0])): 
                matrix[0][i] = 0 
        
        return                              
                    
        