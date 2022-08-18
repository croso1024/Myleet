class Solution:
    def isValidSudoku(self, board) -> bool:

        self.board = [ [board[start_x+i][start_y+j] for i in range(3) for j in range(3) ] for start_x in [0,3,6] for start_y in [0,3,6]]
        self.empty = ["." for i in range(9)] 
        self.empty_num = 0 
        
        
        for cell in self.board : 
 
            if cell == self.empty : self.empty_num +=1  
            else: 
                
                if self.isValidCell(cell) : pass 
                else :return False     
                
        
        if not self.empty_num == 9  : 
            for subset in board : 
                if self.isValidCell(subset): pass 
                
                else : 
                    #print("me1 ")
                    return False 
            #transpose 
            board = [ [sub[i] for sub in board ] for i in range(9) ]
            for subset in board: 
                if self.isValidCell(subset):pass 
                else : 
                    #print("me2 ")
                    return False 
                
        else: return True 
    
        return True 
    
    
    def isValidCell(self,cell) : 
        temp = [] 
      
        for element in cell: 
            #print(temp)
            if element == ".": continue 
            if not element in temp  : temp.append(element) 
            else: return False 
        return True
        del temp  
    
    
    
    
board_test = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

board_test2= [[".",".","4",".",".",".","6","3","."],
              [".",".",".",".",".",".",".",".","."],
              ["5",".",".",".",".",".",".","9","."],
              [".",".",".","5","6",".",".",".","."],
              ["4",".","3",".",".",".",".",".","1"],
              [".",".",".","7",".",".",".",".","."],
              [".",".",".","5",".",".",".",".","."],
              [".",".",".",".",".",".",".",".","."],
              [".",".",".",".",".",".",".",".","."]]
SSS = Solution() 
print(SSS.isValidSudoku(board=board_test2))
