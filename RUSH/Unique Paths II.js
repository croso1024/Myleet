/**
 * @param {number[][]} obstacleGrid
 * @return {number}
 */


// top down recursion + memo 
var uniquePathsWithObstacles = function(obstacleGrid) {
    
    let n = obstacleGrid.length , m = obstacleGrid[0].length
    let memo = new Map();
    // return the unique path from src to i,j 
    const dp = (i,j) =>{

        if (obstacleGrid[i][j] === 1) {return 0}
        else if( i===0 && j === 0){return 1}
        else if (memo.has([i,j].toString())) {
            return memo.get([i,j].toString()) ; 
        }
        if ( i === 0 ){
            memo.set(  [i,j].toString() , dp(i,j-1) )
        }
        else if (j===0){
            memo.set([i,j].toString() , dp(i-1,j) )  
        }
        else{
            memo.set( [i,j].toString() ,  dp(i,j-1) + dp(i-1,j))            
        }
        return memo.get([i,j].toString())

    }
    return  dp(n-1,m-1) ; 
};



// top down recursion + memo 
var uniquePathsWithObstacles = function(obstacleGrid) {

    let n = obstacleGrid.length , m = obstacleGrid[0].length
    let dp = Array.from( new Array(n) , (i)=> new Array(m) ); 

    for (let i = 0 ; i < n ; i++){

        for (let j = 0 ; j < m ; j++){


            if (obstacleGrid[i][j] ===1){
                dp[i][j] = 0 
            }
            else if (i === 0 && j === 0){
                dp[i][j] = 1 ;
            }
            else if (i===0){
                dp[i][j] = dp[i][j-1] ; 
            }
            else if (j===0){
                dp[i][j] = dp[i-1][j] ; 
            }
            else {
                dp[i][j] = dp[i-1][j] + dp[i][j-1] ;
            }
        }
    }
    return dp[n-1][m-1];

}