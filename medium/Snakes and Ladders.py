""" 
    思路 :

        這一題算是我刷題到現在 , exhaustive的題目 ,因為要考慮的狀態與動作分支有點複雜
    
        BFS , 但需要先把棋盤攤平 , 然後從起點開始走 , 
        先往前走,再檢查說走到的位置是不是特殊位置且沒有走到過 , 這樣應該可以避免連續的電鰻或升天電梯
"""


from typing import List 
from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        
        def flattenBoard(board): 
            container = list()  
            alternative = False 
            for row in board[::-1] : 
                container.extend(row) if not alternative else container.extend(reversed(row)) 
                alternative = False if alternative else True 
            return container 
                    
        
        # 取得一個攤平的棋盤後 , 我們還要紀錄一下升天電梯或電鰻的位置
        # key為起始位置,代表特殊事件格子的起點 , value則是他到達的位置 
        board = flattenBoard(board) 
        special_pos = { src:dst-1 for src,dst in enumerate(board) if dst != -1 }
        # 開始走BFS , 我們用index代表位置 
        # 透過visited array去紀錄每個棋盤位置的最短距離
        
        Queue = deque()
        visited = dict() 
        
        Queue.append(0) 
        visited[0] = 0 
        step = 1 
        # 執行BFS
        while Queue : 
            
            # 表示這一步可以到達的位置 
            size = len(Queue) 
            for i in range(size): 
                Cur_pos = Queue.popleft() 
                # 可以走得就是接下來的六格 , 我們就是走上去 , 如果那一格有特殊事件 , 我們實際上就是到達特殊事件引導的格子
                for j in range(1,7): 
                    # 先要確保往前走不會超出範圍 
                    if Cur_pos + j < len(board) and not Cur_pos+j in visited : 
                        
                        # 如果走到了特殊格子 , 那我們是不會停在那一格的 , 
                        # 另一方面是我們要保證不會有連續電鰻或升天電梯的情況  ,
                        if Cur_pos+j in special_pos: 
                            
                            # 檢查是不是已經到了 , 到了就結束return  
                            if special_pos[Cur_pos+j] == len(board)-1 : return step 
                            
                            
                            # 如果還沒到,就是將我們傳送抵達的位置加入Queue , 同時標籤我們已經走到過Cur_pos+j (下次走來也是被傳送)
                            Queue.append(    special_pos[Cur_pos+j]   )
                            visited[Cur_pos+j] = step 
                            
                            
                            # 如果傳送過去的新位置是special的 ,那代表如果我是用一般走法到達,可以去搭該位置的電鰻或電梯
                            # , 因此先不把該位置放進visited
                            # 反過來,如果傳送到的位置是普通的,那就把他加入visited , 反正正常走來也跟我傳過來一樣
                            if special_pos[Cur_pos+j] in special_pos : 
                                pass 
                            else : 
                                visited[special_pos[Cur_pos+j]] = step 
                                
                            
                        else : 
                            
                            # 檢查是不是已經到了 , 到了就結束return  
                            if Cur_pos+j == len(board)-1 : return step 
                            
                            Queue.append(Cur_pos+j) 
                            visited[Cur_pos+j] = step  
                    
                    # 剩下的情況就是超出範圍或著是之後才走到這一格 , 但之後才走到這一格的步數一定是更高的 , 那就丟掉 
                
            # 特定的一步所能到達的所有位置都更新好了 , 我們才更新step . 
            step += 1       
                            
        if len(board)-1 in visited : 
            return visited[len(board)-1] 
        else : 
            return -1 
            


""" 
    解法二: 實際上不需要存special pos , 稍微優化一下結構
"""

from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        
        def flattenBoard(board): 
            container = list()  
            alternative = False 
            for row in board[::-1] : 
                container.extend(row) if not alternative else container.extend(reversed(row)) 
                alternative = False if alternative else True 
            return container 
                    
        board = [None] + flattenBoard(board) 
        Queue = deque()
        visited = dict() 
        
        Queue.append(1) 
        visited[1] = 0 
        step = 1 
        while Queue : 
            
            size = len(Queue) 
            for i in range(size): 
                Cur_pos =   Queue.popleft() 
                for j in range(1,7): 
                    
                    if Cur_pos + j < len(board) and not Cur_pos+j in visited : 
                        
                        if board[Cur_pos+j] != -1: 
                            
                            if (board[Cur_pos+j]) == len(board) - 1: return step 
                            
                            Queue.append(    board[Cur_pos+j]   )
                            visited[Cur_pos+j] = step 
                            
                            if board[(board[Cur_pos+j])] != -1 : 
                                pass 
                            else : 
                                visited[(board[Cur_pos+j])] = step 
                                
                        else : 
                            if Cur_pos+j == len(board) - 1 : return step 
                            
                            Queue.append(Cur_pos+j) 
                            visited[Cur_pos+j] = step  
                    
            step += 1       
                            
        return -1 

test = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
S = Solution()
print(S.snakesAndLadders(test))