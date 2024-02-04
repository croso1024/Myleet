""" 
    題意 :
        給定一個MxN matrix , 其中matrix[i][j] = 0 or 1  , 題目要求我們返回一個MxN array
        array[i][j]代表在原始matrix中 , matrix[i][j]離最近的0的距離為多少(採用曼哈頓距離)
        p.s 至少會有一個0在matrix中
        
    思路 :
        這一題最naive的解法就是在每個cell進行BFS展開 , 這樣的worse case是 N^2 ( N = m x n ) 
        但剖析來想 , 一個cell距離0的距離有幾種情況 , 以下周圍指的是4-adjency
        - 其本身是0 , 則距離為0
        - 其周圍是0 , 則距離為1 
        - 本身周圍都沒有0 , 則距離等於 1+ min(周圍cell到0的最短距離)
        
        我打算用一個類似priority queue的概念 , 先將所有離cell只有0格的加入queue , 同時紀錄他們的距離到答案array
        接下來把所有這些cell的鄰居加入 , 他們就會是距離為1的那些cell , 如此往復
    
"""

""" 
    解法一. follow上述思路 , 階層BFS , 利用解答array做為visited set避免重複尋訪問題
    
    答案的速度空間都很不錯
"""
from typing import List 

from collections import deque

class Solution:

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        # 初始化解答array,queue
        m , n = len(mat) , len(mat[0]) 
        array =[ [-1 for i in range(n)] for j in range(m) ]  
        queue = deque()
        direction = [(-1,0),(1,0),(0,1),(0,-1)]
        
        
        # 我們先把值為"0"的位置加入queue , 同時也更新這些部份的array
        for i in range(m) : 
            for j in range(n): 
                
                if mat[i][j] == 0 : 
                    queue.append((i,j)) 
                    array[i][j] = 0 


        distance = 0    
        # 至此開始展開        
        while queue :
            
            # 這些是距離為distance的節點數量
            size = len(queue) 
            
            for _ in range(size):
                # 取出來的i,j也代表距離為distance的座標位置
                i,j = queue.popleft()
                
                for dir in direction: 

                    next_i , next_j  = i + dir[0] , j + dir[1] 

                    # 超出邊界就是continue
                    if not (0<=next_i <m) or not (0<=next_j < n) : continue               
                    
                    # 如果等於-1 , 代表這一格子是還沒有被探索過的 , 而他們距離0的距離等於當前走到此的distance + 1 
                    if array[next_i][next_j] == -1 : 
                        
                        queue.append((next_i,next_j)) 
                        array[next_i][next_j] = distance + 1 
            
            distance += 1 
        
        return array