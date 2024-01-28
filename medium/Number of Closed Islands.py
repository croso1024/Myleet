""" 
    題意:   
        給定一個2D grid matrix , 0代表島嶼 , 1代表水 ,題目要求有多少 'closed islands' 
        closed island的定義為 一個全部被'1'包圍的島嶼塊 
        看example來說, 就是在邊緣的都絕對不會是'closed island' ,一定要嚴格被1給包圍起來的部份
        
    
    思路 : 
        這一題走DFS/BFS , 我想做修改原始matrix的DFS/BFS,不過有一個小問題就是:
        由於只要是在邊緣的就絕對不可能算是解 ,或著說一旦展開過程遇到邊緣就會讓目前這塊不算數
        
        因此我覺得的作法可能是一個flag keep當前這一塊是否有效 , 同時修改每個走訪過的cell . 
        一旦遇到一個邊緣 , 就修改flag , 最後一round flag結束再來看是否是'closed island'
        
        
"""
from typing import List 



""" 
    解法一. 
        用修改grid的DFS做 , 用一般的雙層尋訪去找展開點 , 並在每次展開的過程開始時maintain一個flag , 修改grid 
        當遇到在邊緣的cell ,代表這整塊都不是close island , 即修改flag 
        當一整塊展開完成後依據flag判斷是否增加closed island . 
        
        整體時間複雜度 O(N)  , 空間 worse case O(N)
    
"""
class Solution:
    
    def closedIsland(self, grid: List[List[int]]) -> int:

        # implement dfs by stack 
        stack = list() 
        height , width = len(grid) , len(grid[0])
        direction = [(0,1) , (1,0) , (-1,0) , (0,-1)]
        closed_island = 0 
        
        
        for i in range(height): 
            for j in range(width): 
                
                if grid[i][j] == 0 :  
                    
                    flag = True  
                    grid[i][j] = 1 
                    stack.append((i,j))
                    
                    
                    while stack : 
                        
                        cur_x , cur_y = stack.pop() 
                        # 如果當前節點是在邊緣或著到達了邊緣 , 代表著這次展開的這塊就不是 closed-island了
                        if cur_x == 0 or cur_x == height-1  or cur_y == 0 or cur_y == width-1 :
                            flag = False 
                        
                        for dir in direction : 
                            
                            next_x = cur_x  + dir[0] 
                            next_y = cur_y  + dir[1]
                            
                            if (not 0 <= next_x < height) or (not 0 <= next_y < width) : continue  
                            
                            if grid[next_x][next_y] == 0  :
                                
                                stack.append( (next_x , next_y) )    
                                grid[next_x][next_y] = 1 
                                
                    closed_island += 1  if flag else 0  
        
        return closed_island 
                                
                                       
                        
                
        
        
        