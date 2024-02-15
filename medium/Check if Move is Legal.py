""" 
    題意:
        
        給定一個8x8的棋盤board , 其中board[r][c]包含以下幾種情況
        - board[r][c] = "." 代表該格是free
        - board[r][c] = "W" 代表該格是white
        - board[r][c] = "B" 代表該格是black       
        
        Good line的條件: 一條至少有3個以上cell的vertical / horizontal / diagonal 其中兩個端點是相同顏色 , 
        而除了端點以外在中間的顏色都是與端點相反的顏色 
        
        現在給定一個位置R,C , 以及我方的顏色 , 要確認我方的顏色作用在該位置後是否為legal move , 
        legal move指的是當這格子顏色根據指定顏色改變後 , 他會變成good line的end point
        
    思路:

        題目問的是在指定格子著上指定顏色之後,該格子是否符合good line的定義 . 
        而good line的定義就是由端點包圍其他與端點相反的顏色 . 尤其題目又是問是否成為end point ,
        意味著我們要從8方向去尋找是否至少作為某一條good line的端點 
        
        
        8方向這部份好解決 , 因為只要檢查8方向,所以我認為甚至不需要做BFS , 基本上就是往該方向走,
        因為要作為端點 ,  所以出發點開始後的下一格至少要是相反顏色,之後就持續做檢查 , 如果走到與自己相同顏色,
        則該點不應該在該方向還往下延伸 
        ------------------------------------------
        -- 我送出之後發現 , 我好像有點過度延伸題意, good line只要至少有3格 , 而題目的legal move則是要求該格是一個end point ,
        在 B W B之後 ,繼續接B也不影響一開始的BWB是good line  
        
"""

""" 
    解法一. 算是簡單的題目 , 單純往8方展開 . 只是題目敘述略為抽象,又或著我今天有點太睏了

        TC:O(N) (8方向展開) , MC:O(C) 只有存recursion stack ,
"""

from typing import List 
class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        
        direction = [
            (1,0) , (1,1) , (1,-1) , (0,1),(0,-1) , (-1,0) , (-1,1) , (-1,-1) 
        ]
        
        # before we find out at least one legal line , 
        legal = False 
        
        def straigtExpand(dir,x,y, sourceColor , step ): 
            nonlocal legal 
            
            if board[x][y] == sourceColor   : 
                
                if step == 0 : return 
                else : 
                    legal = True 
                    return       
                # # 如果該方向在下一格就是空的, 那就是一條good line 
                # # 又或著當前格是在邊緣 ,也是ok 
                # if 0 <= x + dir[0] < 8 and 0 <= y + dir[1] < 8 :
                
                #     if  board[x+dir[0]][y+dir[1]] == "." : 

                #         legal = True 
                    
                # elif (dir[0] == -1  and  x ==0 ) or (dir[0] == 1 and x ==7 ) : 
                    
                #     legal = True                 
                    
                # elif (dir[1] == -1  and y == 0 ) or (dir[1] == 1 and y ==7 ) : 
                #     legal = True 
                    
                # return                 
                
            
            # encounter the free cell , is mean the cell is not the part of a line 
            elif board[x][y] == "." : 
                return 
                
            # encounter converse color , just still find in same direction 
            else : 
                
                if 0 <= x + dir[0] < 8 and 0 <= y + dir[1] < 8 : 
                    straigtExpand( dir , x+dir[0] , y+dir[1] , sourceColor , step + 1   )
                
                            
        
        for dir in direction : 
            
            if 0 <= rMove + dir[0] < 8 and 0 <= cMove + dir[1] < 8 : 

                straigtExpand(  dir , rMove + dir[0] , cMove + dir[1] , color , step = 0    )
            
            if legal : return True 
        
        return False 
    
    
[[".",".","W",".","B","W","W","B"],
 ["B","W",".","W",".","W","B","B"],
 [".","W","B","W","W",".","W","W"],
 ["W","W",".","W",".",".","B","B"],
 ["B","W","B","B","W","W","B","."],
 ["W",".","W",".",".","B","W","W"],
 ["B",".","B","B",".",".","B","B"],
 [".","W",".","W",".","W",".","W"]]