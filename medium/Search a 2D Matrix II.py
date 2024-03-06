""" 
    題意:
    
        給定一個m x n的matrix包含以下性質:
        - 每一個row都是sort過
        - 每一個column都是sort過
        要找出給定的數值有沒有存在於array
        
    思路: 
        這一題和Search a 2D matrix I不一樣在於,前一題是每個row都有sort過,且 row_i最右邊的值 <= row_i+1 最左邊的值,
        因此可以針對row / column 各自做binary search , 但這一題沒有這樣的屬性
        
        稍微想了一下跟以前離散上課講的一題有點類似,從右上角出發,如果某個數字大於當前數字,那代表他一定在這個數字下方 ,
        如果某個數字小於當前數字,但表他一定在這個數字左方
        用這樣的方式來走,直到找到目標值,
        TC : O(m+n) , MC:O(1)
        
"""
from typing import List 
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        m , n = 0 , len(matrix[0]) -1
        
        cur_x , cur_y = m , n 
        
        while cur_x < len(matrix) and cur_y >= 0 : 
            
            if matrix[cur_x][cur_y] == target : return True 
            
            # target比當前位置更小,往左移
            elif matrix[cur_x][cur_y] > target : 
                cur_y -= 1 
            else :
                cur_x += 1 
        
        return False 