from typing import List 


""" 
        這一題我是先用javascript來寫 , 但js就是有許多語法小細節問題出現有點麻煩 , 實際思路可以看js版本
"""


from collections import deque 

class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
    
        queue = deque() 
        island = 0 
        
        for i in range(len(grid)) : 
            
            for j in range(len(grid[0])) :  
                
                
                if (grid[i][j] == "1") : 
                    queue.append([i,j])  
                    grid[i][j] = "0" 
                    
                    while len(queue) > 0 : 
                        
                        cur_i , cur_j = queue.popleft() 
                        
                        if (cur_i-1 >=0) and (grid[cur_i-1][cur_j] == "1") :
                            queue.append([cur_i-1 , cur_j]) 
                            grid[cur_i-1][cur_j] = "0"
                            
                        if (cur_j-1 >=0) and (grid[cur_i][cur_j-1] == "1") :
                            queue.append([cur_i , cur_j-1]) 
                            grid[cur_i][cur_j-1] = "0"
                            
                        if (cur_i+1 < len(grid) ) and (grid[cur_i+1][cur_j] == "1") :
                            queue.append([cur_i+1 , cur_j]) 
                            grid[cur_i+1][cur_j] = "0"
                            
                        if (cur_j+1 < len(grid[0]) ) and (grid[cur_i][cur_j+1] == "1") :
                            queue.append([cur_i , cur_j+1]) 
                            grid[cur_i][cur_j+1] = "0"
                    
                    island += 1 
                                
        
        return island 