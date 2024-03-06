""" 
    題意:
        給定一個grid map m x n , 當中grid[i][j] = 0 代表海洋,1代表陸地.
        定義'move' , 是指從陸地走向四周圍的陸地或著超出邊界.(不能走向海洋)
        
        此題要求我們計算出grid中有多少個陸地cell是"不可以"走到邊界的
        
    思路:
        看起來就是BFS/DFS的基本題型 ,我打算使用BFS來解 , 有兩個思路:
        1. 走 BFS + 翻格子 , 一旦這一次展開的陸地有任何一塊走到邊界之外,則這次尋訪過程的所有陸地都是可以走到邊界的陸地
        2. 從邊界遇到的陸地開始展開BFS , 以此展開的BFS全部都是可以走到邊界的陸地cell
        
        --- 
        解完後發現這題要的是'不可以'走到邊界的cell數,所以第一個解法直接在最終判斷這次展開是否到達邊界並修正sol的條件式加一個反轉
        而第二種解法,可以單純的用DFS修改完所有cell後再計算一次剩餘的1的數量
        
"""

""" 
    解法一. 使用BFS + 翻格子
"""
from typing import List 
from collections import deque

class Solution:

    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        m , n = len(grid) , len(grid[0]) 
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        # record the land cell that can reach the boundary
        sol = 0 

        def BFS(i,j): 
            nonlocal sol
            # temp用來儲存這次展開到底經過多少塊陸地
            # escape 說明這次展開的陸地是否可以碰到boundary
            
            queue = deque() 
            queue.append((i,j))
            grid[i][j] = 0 
            temp = 1  
            escape = False 
            
            while queue : 
                
                size = len(queue)
                
                for _ in range(size): 
                    
                    cur_x , cur_y = queue.popleft() 
                    
                    for dir in directions : 

                        next_x , next_y = cur_x + dir[0] , cur_y + dir[1]
                        
                        # this condition make the search process in the boundary
                        if not 0 <= next_x < m or  not 0 <= next_y < n :  
                            # 這塊陸地是可以離開boundary
                            escape = True 
                            continue 
                        
                        if grid[next_x][next_y] == 1 : 
                            grid[next_x][next_y] = 0 
                            queue.append((next_x ,next_y)) 
                            temp += 1 
            if not escape : sol += temp 
            return 
        
        for i in range(m): 
            for j in range(n): 
                # 從看到陸地開始做BFS
                if grid[i][j] == 1 : BFS(i,j) 
                    
        return sol

""" 
    解法二. DFS從邊界展開 再計算剩餘的1的數量
        這個解法的TC達到 98% , MC也有87% ,
        大致上可以理解為這個作法並不會展開到內部那些真的無法走到邊界的land cell,
        因此進行展開的範圍較少
"""


class Solution:

    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        m , n = len(grid) , len(grid[0]) 
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        def DFS( i , j ): 
            
            if grid[i][j] == 0 : return 
            stack = [] 
            stack.append( (i,j) )
            grid[i][j] = 0 
            
            while stack : 
                
                cur_x , cur_y = stack.pop() 
                
                for dir in directions : 
                    next_x , next_y = cur_x + dir[0] , cur_y + dir[1] 
                    if not 0 <= next_x < m or not 0 <= next_y < n : continue
                    
                    if grid[next_x][next_y] == 1 : 
                        grid[next_x][next_y] = 0 
                        stack.append((next_x,next_y))  
        
        
        for i in range(m): 
            DFS( i , 0 )
            DFS( i , n-1 ) 
            
        for i in range(n): 
            DFS( 0 , i ) 
            DFS( m-1 , i ) 
        
        sol = 0 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 : sol += 1 
        return sol 