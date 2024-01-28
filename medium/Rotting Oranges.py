""" 
    思路 :
        爛掉的橘子每過一分鐘會讓 上下左右四個方向的橘子(如果有)也變成腐爛的 , 
        求需要花幾分鐘可以讓場上所有橘子都腐爛掉,如果無法就是-1 
        
        滿直觀使用BFS直接推進 , 以分鐘為單位這樣 ,
        
        大概步驟: 
        1. 一個set加入所有新鮮橘子的位置 , 同時把所有爛掉橘子加入Queue , 這是第0分鐘的狀況
        2. 走BFS , 一旦有新鮮橘子被感染 , 就從set移除 , 並加入Queue等待下一輪傳撥 , 
        
        走完BFS後檢查新鮮橘子的set是否還有         

"""


from typing import List 
from collections import deque

class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        Queue = deque() 
        fresh_orange = set() 
        
        time_consume = 0 
        
        Four_direction = [  [-1,0] , [1,0] , [0,-1] , [0,1]  ]
        m,n = len(grid) , len(grid[0])         
        
        # 0 : empty / 1 : fresh orange / 2: rotten orange
        for i in range(m): 
            for j in range(n): 
                
                if grid[i][j] == 1 : 
                    fresh_orange.add((i,j))  
                elif grid[i][j] == 2 : 
                    Queue.append( (i,j) ) 
        
        # 可能根本就沒有爛橘子 , 如果真的沒有不會進入Queue 
        
        if len(fresh_orange) == 0 : return 0 
        # 只要還有爛掉的orange還沒傳傳撥
        while Queue : 
            # size: 這一輪要傳的腐爛橘子數量
            size = len(Queue)
            
            for _ in range(size) :  
                
                cur_i , cur_j  = Queue.popleft() 
                
                for dir in Four_direction : 
                    
                    next_i = cur_i + dir[0] 
                    next_j = cur_j + dir[1] 
                    
                    if not next_i >=0  or not next_i < m : continue
                    if not next_j >=0  or not next_j < n : continue
                    
                    
                    if grid[next_i][next_j] == 1 :  

                        grid[next_i][next_j] = 2 
                        Queue.append( (next_i , next_j) )
                        # if (next_i,next_j) in fresh_orange : 
                        fresh_orange.remove((next_i,next_j))
                        
                    
            time_consume += 1 
            if len(fresh_orange) == 0 : return time_consume
        
        return -1

grid = [[2,1,1],[1,1,0],[0,1,1]]
S = Solution()
print(S.orangesRotting(grid) )