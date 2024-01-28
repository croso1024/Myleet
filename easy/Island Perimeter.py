from typing import List 
""" 
    給定一個Array row x col , 其中grid[i][j] = 1 代表該處有島嶼
    題目已知只會有一座島嶼 , 要求計算島嶼的邊長多少 , 這一題很直覺使用DFS or BFS 
    每一格島嶼所貢獻的邊長為 4 - 鄰居數 
    
    因此只要找到任何一塊陸地開始走DFS就可以計算整座島嶼的邊長
"""


       
""" 
    解法一. 
        做DFS , 概念是每塊陸地能貢獻的週長為 4-其鄰居數 , 因此就是DFS的框架加上計算鄰居數這一點
        時間的bottleneck在一開始還是透過雙loop去找陸地的起點 , 找到後DFS走O(陸地數) , 但空間上也存O(陸地數) 
"""
class Solution:

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        # 第一步,先找出任何一塊陸地 
        src = None
        for i in range(len(grid)):
            for j in range(len(grid[0])): 
                if grid[i][j] == 1 : 
                    src = (i,j) 
                    break 
            if not src is None : break 
        
        stack = list()
        visited = set() 
        stack.append(src) 
        visited.add(src) 
        direction = [(-1,0),(1,0),(0,1),(0,-1)]

        sol = 0 

        # 從stack裡面拿出陸地 , traverse neighbor加入stack並且計算有幾個neighbor , 最後將邊長加入sol 
        while stack : 
            
            cur_pos = stack.pop()
            neighbors = 0 
            
            for dir in direction :  
                
                neighbor_i = cur_pos[0] + dir[0]
                neighbor_j = cur_pos[1] + dir[1] 
                
                if not 0<=neighbor_i<len(grid) or not 0<= neighbor_j<len(grid[0]) :  continue
                
                if grid[neighbor_i][neighbor_j] == 1 : 
                    neighbors += 1 

                    if not (neighbor_i,neighbor_j) in visited : 
                        visited.add((neighbor_i,neighbor_j))
                        stack.append((neighbor_i,neighbor_j))
                
            sol += (4 - neighbors)
        
        return sol
                    
                    
                    
                
            
            
""" 
    解法二. 看解答區的solution , 既然都要透過O(N^2)去找到第一塊陸地 , 
        那實際上也可以直接計算每一塊陸地有幾個neighbor , 一樣用4-neighbor 這樣就可以直接計算 , code更簡潔
        與解法一相比 , 實際的性能與陸地數有很大關聯
        
        這個解法也是O(N^2)時間 , 但空間減少到只要O(1)
"""


class Solution:

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        direction = [(-1,0),(1,0),(0,1),(0,-1)]
        sol = 0 
        
        for i in range(len(grid)): 
            for  j in range(len(grid[0])): 
                
                if grid[i][j] == 1 : 
                    
                    neighbor = 0 
                    for dir in direction: 
                        
                        if 0<= i+dir[0] < len(grid) and 0 <= j + dir[1] <len(grid[0]) and grid[i+dir[0]][j+dir[1]] == 1  :  
                            neighbor += 1 
                    
                    sol += (4-neighbor)
        
        return sol
                    
                    
                    
                    