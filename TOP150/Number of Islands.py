
class Solution:

    # BFS or DFS is ok  , i use DFS 
    def numIslands(self, grid: List[List[str]]) -> int:
        
        direction = [(-1,0) , (1,0) , (0,1) , (0,-1)] 
        height , width = len(grid) , len(grid[0]) 
        islands = 0 
        for i in range(height) : 

            for j in range(width) : 

                if grid[i][j] == "1": 
                    dfs(i,j)
                    islands += 1 

    
        def dfs( i ,  j ) : 

            stack = []
            stack.append((i,j)) 
            grid[i][j] = "0" 

            while stack : 

                cur_i , cur_j = stack.pop() 

                for dir in direction : 

                    next_i = cur_i + dir[0]
                    next_j = cur_j + dir[1] 

                    if not (0<= next_i < height) or not (0 <= next_j < width) : continue 

                    if grid[next_i][next_j] == "1" : 
                        grid[next_i][next_j] = "0" 
                        stack.append( (next_i , next_j ) )

        return islands