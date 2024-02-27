from typing import List 
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
        # step.1 檢查每個Row 
        for row in board : 
            temp = set() 
            for item in row : 
                if item == "." : pass 
                else : 
                    if item in temp : return False 
                    else : temp.add(item) 
        
        # step.2 檢查每一個column 
        for column in range(9) :  
            temp = set() 
            for i in range(9):  
                if board[i][column] == "." : pass 
                else : 
                    if board[i][column] in temp : return False 
                    else : temp.add(board[i][column])
        
        # step.3 檢查每一個Block 
        
        # 每個3x3的Block , 一共九塊
        for i in range(0 , 9 , 3): 
            for j in range(0, 9 , 3 ):  
                # 內部的3x3 block 
                temp = set() 
                for x in range(i , i+3): 
                    for y in range(j , j +3) :
                        if board[x][y] =="." : pass 
                        else : 
                            if board[x][y] in temp : return False 
                            else : temp.add(board[x][y])
        
        return True 