
from typing import List 
class Solution:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        m , n =  len(matrix),len(matrix[0]) 
        
        # 策略就是去維護寬度與高度的範圍 ,作為traverse的區間 
        height = [0,m-1] 
        width = [0,n-1] 
        
        sol = list() 
        
        while len(sol) < ( m * n ): 
            print(sol)
            # 把最上排的加入
            if height[0] <= height[1] : 
                for column in range(width[0] , width[1]+1) : 
                    sol.append( matrix[height[0]][column]  )
                height[0] += 1 
            
            # 把右邊加入
            if width[1] >= width[0] :  
                for row in range(height[0] , height[1]+1) : 
                    sol.append(  matrix[row][width[1]] ) 
                width[1] -=1 

            # 底層加入
            if height[1] >= height[0] : 
                for column in range( width[1] , width[0] -1 , -1  ): 
                    sol.append( matrix[height[1]][column])  
                height[1] -=1 
                
            # 把左邊加入
            if width[0] <= width[1] :  
                for row in range(height[1] , height[0] -1 , -1) : 
                    sol.append(  matrix[row][width[0]]) 
                width[0] += 1 
        
        return sol

S = Solution()
S.spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]])