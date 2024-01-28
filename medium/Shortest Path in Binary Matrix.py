"""
    思路:
    
    這一題要在一個binary matrix上尋找從左上到右下的最短路徑 , 
    比較特別的只有這一題可以走8個方向, 意思是雖然是matrix但可以走斜向 , 同時我們只能走在格子為0的點
    路徑長度為整條路上拜訪過的節點數
    
    因為要找最短路徑 , 比較直覺想使用BFS, 這一題我認為可以使用透過把grid轉為1來取代visited table優化空間
    但第一個解還是使用標準queue+visited的BFS
    
"""
from typing import List 

"""
    解法一. 標準BFS , 可以優化的方向有2 :
        1. 我們是在"取出節點時檢查是否到達終點" , 可以改為探尋時就確認這件事情
        2. 我們使用visited set去避免走回頭路 , 但可以直接修改grid來完成這件事
        
        速度還行 , 但空間偏差
"""

from collections import deque 

class Solution:

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0] == 1 : return -1
        n = len(grid)
        queue = deque()
        visited = set() 
        # 拜訪的節點數量即為路徑長度 , 代表至少是1步 , 另外如果起點是1 ,那就代表走不到
        step = 1 
        direction = [ 
            (1,0),(0,1),(-1,0),(0,-1) , (1,1) ,(1,-1) , (-1,1) ,(-1,-1) 
        ]
        
        queue.append((0,0))
        visited.add((0,0))

        while queue : 
            
            size = len(queue) 
            
            for _ in range(size): 
                # 取出現在所在位置 , 接下來要走八方向尋訪
                i,j = queue.popleft() 

                # 如果現在的位置就是終點 , 那就可以return目前累計的步數了
                if (i,j) == (n-1,n-1) : return step 
                
                for dir in direction : 
                    
                    next_i,next_j = i + dir[0] , j+dir[1]
                    # 沒有超出grid ,避免index out of range 
                    if 0<= next_i < n and 0 <= next_j < n : 
                        
                        if grid[next_i][next_j] == 0 and not (next_i,next_j) in visited : 
                            visited.add((next_i,next_j))
                            queue.append((next_i,next_j))
            
            step += 1 
        
        return -1             
        
        
"""
    解法二. 去優化解法一.
        我們改為在尋找的過程中去偵測終點 , 同時改用修改grid取代visited set
        
        速度和空間都極佳
"""
        
        
from collections import deque 

class Solution:

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0] == 1 : return -1 
        n = len(grid) 
        if n==1 : return 1 
        
        
        queue = deque()
        step = 1 
        direction = [ 
            (1,0),(0,1),(-1,0),(0,-1) , (1,1) ,(1,-1) , (-1,1) ,(-1,-1) 
        ]
        queue.append((0,0))

        while queue : 
            
            size = len(queue) 
            for _ in range(size): 

                i,j = queue.popleft() 
                
                for dir in direction : 
                    next_i , next_j = i+dir[0] , j+dir[1] 
                    
                    if 0<= next_i < n and 0<= next_j < n :  
                        # 發現可以走得地方,我們把對於終點的檢查改到這邊
                        if grid[next_i][next_j] == 0 :   
                            
                            if ( next_i,next_j )== (n-1,n-1) : return step +1 
                            # 把該位置加入queue後將此格設置為1 , 避免重複尋訪
                            queue.append((next_i,next_j)) 
                            grid[next_i][next_j] = 1 
                            
            step += 1 
            
        return -1 
                            
                        
                