
""" 
    思路: 
        這一題要我們依照他給定的shift規則, 對一個array執行k次shift 
        最naive的思路其實就是複製一個array容器 , 針對shift規則執行 
        shift 規則 :
        
        - 每一行往右邊移動一格
        - 在最後一行的值 , 往右移動後還要往下移動一格 
        - 這一條實際上就是前面兩條的延伸 , 即右下角的元素shift完成要在左上
"""


""" 
    解法一. naive 解法 , 複製容器
"""
from typing import List 
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        m = len(grid) 
        n = len(grid[0])

        def shift(array): 
            nonlocal m , n 
            # create container 
            temp =[ [None for i in range(n)] for j in range(m) ]
            for i in range(m) :
                for j in range(n): 
                    
                    if j == n-1  : 
                        if i == m-1 : 
                            temp[0][0] = array[i][j] 
                        else : 
                            temp[i+1][0] = array[i][j]
                    else : 
                        temp[i][j+1] = array[i][j]
            return temp
        
        sol = grid 
        for i in range(k) : 
            sol = shift(sol)
        return sol 




""" 
    解法二. 找規律來加速一次shift的速度
"""
from typing import List 
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        m = len(grid)
        n = len(grid[0]) 
        
        
        # 其實shift 就只是每一行往右平移 , 接著針對第一個行往下輪轉一次而已 
        def shift(array): 
            
            sol = [] 
            # 平移行
            for row in array : 
                sol.append(  [row[-1]] + row[:-1] )
            print(sol)
            # 輪轉第一行
            for i in range(m) :
                sol[ (i+1) % m   ][0] = array[i][-1]
            
            return sol             

        sol = grid 
        for i in range(k): 
            sol = shift(sol) 
        
        return sol 