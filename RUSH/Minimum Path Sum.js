/**
 * @param {number[][]} grid
 * @return {number}
 */

// create 2D dp-table represent the minimum cost to arrive (i,j) ; 
var minPathSum = function(grid) {
    
    let dp = Array.from( new Array( grid.length ) , () => new Array(grid[0].length) ) ; 
    dp[0][0] = grid[0][0] ; 

    for (let i = 0 ; i < grid.length ; i++){

        for (let j = 0 ; j < grid[0].length ; j++){

            if (i===0 && j===0){
                dp[i][j] = grid[i][j] ; 
            }
            else if(i===0){ 
                dp[0][j] = grid[i][j] + dp[0][j-1] ; 
            }
            else if (j===0){
                dp[i][j]  = grid[i][j] + dp[i-1][j] ; 
            }
            else{
                dp[i][j] = grid[i][j] + Math.min(dp[i-1][j] , dp[i][j-1]) ; 
            }
        }
    }
    return dp[grid.length-1][grid[0].length-1]; 
};


// create 2D dp-table represent the minimum cost to arrive (i,j) ; 
// extreme state compress solution 
var minPathSum = function(grid) {

    let prevRow = new Array(grid.length) ; 

    prevRow[0] = grid[0][0] ; 
    // calculate first row 
    for (let j = 1 ; j < grid[0].length ; j++){ prevRow[j] = grid[0][j] + prevRow[j-1]  }


    for (let i = 1 ; i < grid.length ; i++){

        let leftElement = null ; 

        for (let j = 0 ; j < grid[0].length ; j++){

            if (leftElement === null){
                prevRow[j] = grid[i][j] + prevRow[j] ;                 
                leftElement = prevRow[j] ; 
            }
            else{
                prevRow[j] = grid[i][j] + Math.min( prevRow[j-1] , prevRow[j] )
                leftElement = prevRow[j] ; 
            }
        }
    }

    return prevRow[grid[0].length-1]

}