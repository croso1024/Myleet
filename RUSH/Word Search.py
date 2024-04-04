from typing import List 


#  backtrack algorithms
class Solution:
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        sol = False 
        direction = [(0,1),(1,0),(-1,0),(0,-1)]
        
        
        def backtrack( startIndex , path : set , cur_i,cur_j ):
            nonlocal sol 
            if startIndex == len(word):
                sol = True 
                return 
            
            for dir in direction :
                
                next_i = cur_i +dir[0]
                next_j = cur_j +dir[1]

                if 0 <= next_i < len(board) and 0 <= next_j < len(board[0]) : 
                    
                    if (next_i,next_j) in path : continue 
                    
                    if board[next_i][next_j] == word[startIndex] : 
                        path.add((next_i,next_j))
                        backtrack( startIndex+1 , path , next_i , next_j )
                        path.remove((next_i,next_j))


        for i in range(len(board)): 
            for j in range(len(board[0])) :  
                if sol : return sol 
                if board[i][j] == word[0] : 
                    backtrack(1 , {(i,j)} , i , j )                     
                
        return sol
            
            
            