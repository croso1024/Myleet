

""" 
    思路 : 
        此題要我們尋訪一個matrix , 一旦遇到0 , 就將該row / column的全部元素in-place的修改成0 
        follow-up希望我們至少能做到O(m+n)的space complxity , 如果可以看能否達到constant space complexity 

        針對第一個希望O(m+n) space complexity的部份 , 蠻直觀看得出來可以用一個hash set紀錄已經都變成0的部份來跳過
        
"""



""" 
    解法一. 
        我原先想的解法 , 就是遇到0後消除整列整行並加入 hash set , 但這會導致實際上可能同一列/行中還有其他0會導致該行/列全消 
        但我這樣子加入hash set的作法會使得他們沒有成功消除 , 被跳過了.
    
"""
from typing import List 
class Solution:

    def setZeroes(self, matrix: List[List[int]]) -> None:

        # 使用hash set來保存走過的row/column , 使用O(m+n)的space complexity 
        row_set = set() 
        column_set = set()
        
        for i in range(len(matrix)) : 


            for j in range(len(matrix[0])) : 
                
                # 當這一行或列的元素已經在hash set , 那就跳過這一行
                if (i in row_set ) or ( j in column_set )  : continue
                
                # 遇到0 , 將該列該行轉為0 
                if matrix[i][j] == 0 : 
                    row_set.add(i) 
                    column_set.add(j) 
                    
                    # 做替換為0的事
                    matrix[i] = [0 for i in range(len(matrix[0]))] 
                    for k in range(len(matrix)) : matrix[k][j] = 0 
        
        return matrix 
    
    
""" 
    解法二 . 
        拆分為兩個step , 第一部份traverse matrix並將0的部份index加入hashset 
        第二部份則是根據兩個set所蒐集到的要消除的行列做操作
"""
class Solution:

    def setZeroes(self, matrix: List[List[int]]) -> None: 
        
        rSet = set() 
        cSet = set()
        for i in range(len(matrix)) : 
            for j in range(len(matrix[0])) : 
                if matrix[i][j] == 0 : 
                    rSet.add(i) 
                    cSet.add(j) 

        # 要消除的列 
        for row in rSet : 
            matrix[row] = [0] * len(matrix[0]) 
        
        # 要消除的行 :
        for column in cSet : 
            
            for k in range(len(matrix)) : 
                matrix[k][column] = 0 
                
        return matrix
    
""" 
    解法三 . 
        稍微優化一下解法二 . 因為實際上第二步的開始消除也能整理進找0點
"""
class Solution:

    def setZeroes(self, matrix: List[List[int]]) -> None: 
        
        cSet = set()
        for i in range(len(matrix)) : 
            delete_row = False 
            for j in range(len(matrix[0])) : 
                if matrix[i][j] == 0 : 
                    cSet.add(j)
                    delete_row = True  
            # 把消除列整合在此
            if delete_row  : 
                matrix[i] = [0] * len(matrix[0]) 
            
        # 要消除的行 :
        for column in cSet : 
            
            for k in range(len(matrix)) : 
                matrix[k][column] = 0 
                
        return matrix