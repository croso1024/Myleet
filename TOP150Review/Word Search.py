# backtrack 
class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        
        height , width = len(board) , len(board[0])

        direction = [(-1,0) , (1,0) , (0,1) , (0,-1)]

        solution = False 


        # Given the pos i,j and rest charaters , then search the neighbor 
        def backtrack( i , j,   res ,  visited  ): 
            nonlocal solution 
            if len(res) == 0 : 
                solution = True   
                return 
            for dir in direction : 

                next_i = i + dir[0] 
                next_j = j + dir[1] 

                if not (0 <= next_i < height) or not (0 <= next_j < width) : continue 

                if board[next_i][next_j] == res[0] and not (next_i,next_j) in visited:  
                    visited.add( (next_i , next_j ) ) 
                    backtrack(next_i , next_j , res[1:] , visited) 
                    visited.remove( (next_i , next_j) ) 
        

        for i in range(height) : 
            for j in range(width) : 
                
                if board[i][j] == word[0] : 
                    visited = {(i,j)}  
                    backtrack(i,j , word[1:] , visited) 

                if solution : return True 

        return False 



