/**
 * @param {number[][]} matrix
 * @return {number}
 */

/*
    思路:   
        這一題是東哥動態規劃的範例題之一，作為範例如何定義DP問題的base case / dp table初始值，
        在看東哥版本前自己先解一次。

        這一題dp明顯的地方應該是在於 ,假設我們要求到達某一列k的最小下落路徑 ,
        就等於找 : min( 到達第k列每一個值的左上,上,右上 的最小下落路徑 ) , 
        亦即在DP的處理上 , 每一個值需要仰賴自己左上,上,右上  , 並且dp[i][j]代表了到達這個位置的最小下落路徑和

        在base case上 第一列的值就是原先的matrix[0] 
        從第二列開始traverse填滿這個dp-table 
        
        最後答案就在最後一層中取最小值結束

        note. 題目給了matrix為方陣
*/

/*
    解法一. 這一題基本上就是按照思路走 , 上面的描述已經非常清晰的說明了狀態轉移方程式 , 以及尋訪dp[table]的方向
*/
var minFallingPathSum = function(matrix) {
    
    let size = matrix.length ; 
    if (size==1) {return matrix[0][0];}

    let dp = Array.from(  new Array(size) , (v)=> 
        {return Array.from( new Array(size).fill(null))});

    // 第一列來講base case就是自己本身 
    dp[0] = matrix[0] ; 
    
    // 基本狀態以row為單位 , outer loop以row為單位推進 
    for (let i = 1 ; i < size ; i++){

        // 內層 , 使用累計到上方的minimum failling path sum . 
        for (let j = 0 ; j < size ; j++){
            
            if (j==0){
                dp[i][j] = matrix[i][j] + Math.min( dp[i-1][j] , dp[i-1][j+1] );
            }
            else if (j==size-1){
                dp[i][j] = matrix[i][j] + Math.min( dp[i-1][j-1],dp[i-1][j]) ; 
            }
            else {
                dp[i][j] = matrix[i][j] + Math.min(
                    dp[i-1][j-1] , dp[i-1][j] , dp[i-1][j+1] 
                )
            }

        }
        
    }

    return Math.min(...dp[size-1]); 

};