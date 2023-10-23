/**
 * @param {number[][]} triangle
 * @return {number}
 */

/*
    思路 : 

    這一題也是 2D-DP , 要計算走到底的最小path sum 相當於
    min( 最底層的cost + 可以走到該cost的位置的最小path sum )

    這一題比較特別的反而是他的形狀 , 是一個三角形 , 不過這不影響使用2D DP,
    
    dp[i][j] 代表走到該 (i,j)位置的最小path sum , 解在最後一層的minimum 
    
    dp[i][j] = triangle[i][j] + min(   dp[i-1][j]  , dp[i-1][j-1] ) 

*/

var minimumTotal = function(triangle) {
    

    // dp table的size等於 三角形層數 x 最後一層大小 , 但實際上層數=最後一層大小 
    let size = triangle.length ; 

    let dp = Array.from( new Array(size) , (v)=> new Array(size) ) ;

    dp[0][0] = triangle[0][0] ; 
    // 外層loop推進層數往下 , 實際上traverse的方向就在於我們的dp-table中的值需要什麼方向的值優先被算好 
    // 對於這一題來說就很基本的,只要正上與左上  

    for (let i = 1  ; i < size ; i++ ){
        // 注意內迴圈的中止條件 , 我們這邊是針對左下三角的範圍去traverse 
        
        for (let j = 0 ; j <= i ; j ++ ){
            if (j==0){
                dp[i][j] = triangle[i][j] + dp[i-1][j] 
                }             
            else if (j == i){
                dp[i][j] = triangle[i][j] + dp[i-1][j-1] 
            }
            else {
                dp[i][j] = triangle[i][j] + Math.min( dp[i-1][j] ,  dp[i-1][j-1] )
            }
        }
    }
    return Math.min( ...dp[size-1]  )
};

let test_case = [[2],[3,4],[6,5,7],[4,1,8,3]] ; 
minimumTotal(test_case) ;