from typing import List 
""" 
    題意: 
        給定兩個 M x N的島嶼grid1,grid2 , 並定義所謂的sub-island, 
        指的是grid2中的島嶼,如果這個島嶼的全部陸地在grid1也都是陸地的範圍 ,則稱為sub-island 
        求grid2中有多少的sub-island
        
    思路: 
        這題雖然給了兩個grid , 但實際上grid1只是作為grid2的條件判斷所使用,如果grid2的島嶼不在grid1對應位置上
        則我們可以直接跳過這座島嶼 ,使用BFS加上直接修改grid2的方式來代替visited set 
        
        這一題比較細節的地方在於如何正確地處理將grid2的格子轉為1以及檢查grid1中相同位置的操作 , 
        例如我們在拜訪neighbor的時候進行修改 , 會導致如果在queue取節點出來時grid1沒有相應內容而break出去 ,
        那些原本已經在queue內的位置就失效了 
        
"""
from collections import deque 

""" 
    解法一. 就是BFS思路 , 
        完整去遍瀝島嶼,同時在遍瀝過程中檢查如果島嶼2有陸地是不存在於島嶼1的,就將valid flag設置為False 
        當遍瀝完一座島嶼 , 如果valid仍為True說明其sub-island 

        原本我是將valid也作為While loop的條件,但這樣會導致解錯誤,仔細想也是因為這樣會導致仍然在queue中已經被修改的元素丟失
        所以最後還是乖乖老實遍瀝完成島嶼 
        
        不過這個解的時間複雜度基本上是O(MxN) , 空間也同樣 
        實際測試在速度與空間都超優
"""

class Solution:

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        queue = deque() 
        sub_island = 0 
        direction = [(-1,0),(1,0),(0,-1),(0,1)]
        m , n = len(grid1) , len(grid1[0])
        # 使用雙迴圈去找到陸地後開始
        for i in range(m) : 

            for j in range(n): 
                
                if grid2[i][j] == 1 and grid1[i][j] == 1 :  
                    
                    grid2[i][j] = 0 
                    queue.append((i,j)) 
                    valid = True 
                    
                    while queue  : 
                        
                        cur_i,cur_j = queue.popleft() 
                        
                        for dir in direction : 
                            
                            next_i , next_j = cur_i + dir[0] , cur_j + dir[1]  
                            
                            if 0 <= next_i < m and 0 <= next_j < n : 
                                
                                if grid2[next_i][next_j]  == 1 :  
                                    
                                    if grid1[next_i][next_j] == 1 : 
                                        
                                        grid2[next_i][next_j] = 0   
                                        queue.append((next_i,next_j))
                                        
                                    else : valid = False 
                                    
                    if valid : sub_island += 1 
                    
                    
        return sub_island            
                                
                        
        
grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]]
grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
S = Solution()
S.countSubIslands(grid1,grid2)

                                
                        