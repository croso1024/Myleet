/**
 * @param {character[][]} grid
 * @return {number}
 */


var numIslands = function(grid) {
    
    const direction = [[1,0] , [-1,0],[0,1],[0,-1]] ; 
    // perform the dfs algorithms from coordinate : i,j
    const dfs = (x,y) => {
        for (let i = 0 ; i < 4 ; i++){

            let next_x = x + direction[i][0] ; 
            let next_y = y + direction[i][1] ; 
            
            // check to prevent index out of bound ;
            if (next_x >=0 && next_x < grid.length && next_y >= 0 && next_y < grid[0].length ){
                
                if (grid[next_x][next_y] === "1"){
                    grid[next_x][next_y] = "0" ; 
                    dfs(next_x , next_y) ; 
                }
            }
        }
    }

    let solution = 0 ; 

    for (let i = 0 ; i < grid.length ; i++){

        for (let j = 0 ; j < grid[0].length ; j++){

            if (grid[i][j] === "1"){
                solution += 1 ;
                grid[i][j] = "0" ;
                dfs(i,j) ; 
            }
        }
    }
    return solution ; 
};