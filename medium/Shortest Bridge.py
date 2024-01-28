""" 
    思路: 
        題目給定一個n x n binary grid , 當中1代表地面 , 0代表水 , 
        這個grid一定好像有兩個島嶼(相連的一群地面) ,求我們最少需要把幾格0換成1 ,
        才可以把兩做島嶼連接在一起 . 
        
        這題想一下 , 感覺是需要兩邊一起做BFS , 交替擴張兩個島嶼!? 
        
        整理一下 , 我認為應該從其中一座島嶼開始做BFS , 把第一島嶼的地面都放進一個set中 , 
        
        接下來找到另外一座島嶼 , 先將其全部放進Queue , 再開始擴張 , 紀錄這個擴張的step數 , 一旦碰到另一做島嶼的任何一塊地就是答案
        
        即: 
        step1 . 雙迴圈找到某一塊島嶼地面後跳出 , 
        step2. 針對找到的島嶼 , BFS , 把該島嶼所有地面加入Set  
        
        step3. 雙迴圈找另外一塊島嶼, 
        step4. 找到另外一塊島嶼 , BFS 但這次是要全部放進一個Qeueu ( 撇除執行BFS本身的queue , 另外一個queue)
        step5. 從這個Queue開始BFS ,紀錄step數 , 直到遇見另外一個島嶼
        
        
        # 再提煉一下 , 上面的5個step能夠再節省一些
        step1. 雙迴圈找到某塊島嶼地面 , 
        step2. 針對找到的島嶼 , 執行BFS , 將所有島嶼全部加入Queue和visited , 
        
        step3. 從這個Queue開始BFS,紀錄step直到看到另一座島嶼        
"""


""" 
    解法一. follow上述提煉版的想法 
        時間和空間都是O(N)
"""
from typing import List 

from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        # step1. 雙迴圈找其中一塊島嶼的地面 ,把他放進islandQueue就可跳出了
        n = len(grid) 
        islandQueue = deque() 
        visited = set() 
        direction =[ [ -1,0 ] , [1,0] , [0,-1] , [0,1] ]
        find = False 
        
        # 包成一個函數 , 這樣跳出雙loop比較簡單
        def findGroud(grid): 
            for i in range(n): 
                for j in range(n): 
                    if grid[i][j] == 1 : 
                        return i , j 
        i , j = findGroud(grid)
        islandQueue.append( (i,j) )
        visited.add((i,j)) 
                
                     
            
        # step.2 透過islandQueue , 把第一座島嶼完全找出來並加入ExpandQueue
        ExpandQueue = deque() 
        while islandQueue : 
            
            cell_i , cell_j = islandQueue.popleft() 
            print(cell_i , cell_j)
            # 放進擴展Queue , 這是待會要用來擴展大地的
            ExpandQueue.append((cell_i,cell_j))
            for dir in direction : 
                
                next_i = cell_i + dir[0]
                next_j = cell_j + dir[1] 
                
                if not 0 <= next_i < n : continue 
                if not 0 <= next_j < n : continue 
                
                if grid[next_i][next_j] == 1 and not (next_i,next_j) in visited : 
                    islandQueue.append((next_i,next_j))
                    visited.add((next_i,next_j))
        
        # step.3 我們已經完全找到了第一座島嶼 , 把其所有格子都放在ExpandQueue ,
        # 接下來就透過ExpandQueue 去BFS , 找到第一個不在visited的地面就是另一座島嶼 
        sol = 0 
        while ExpandQueue : 
            
            size = len(ExpandQueue) 
            
            for _ in range(size): 
            
                cell_i , cell_j = ExpandQueue.popleft() 
                
                for dir in direction : 
                    
                    next_i = cell_i + dir[0]
                    next_j = cell_j + dir[1] 
                    
                    if not 0 <= next_i < n : continue 
                    if not 0 <= next_j < n : continue 

                    # 這一段的邏輯就不一樣 , 如果碰到不在visited的島嶼 , 那就可以return sol 了 
                    # 否則這一段我們正在擴張 , 因此可以走0 , 只要不在visited就可 
                    
                    if grid[next_i][next_j] == 1 and not (next_i,next_j) in visited:
                        return sol 
                    
                    if not (next_i , next_j) in visited : 
                        ExpandQueue.append((next_i ,next_j)) 
                        visited.add((next_i,next_j)) 
            
            # 擴張完一整輪沒有遇到陸地 , sol +=1 (如果下一輪碰到了 , 那代表只要蓋一格的橋樑)
            sol += 1       
        
        return -1 

test = [[0,1],[1,0]]
S = Solution()
print(S.shortestBridge(test))