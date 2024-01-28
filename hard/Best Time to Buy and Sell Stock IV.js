/*
    思路 : 
        買賣股票的最終問題 , 在指定任意k大小的情況下去計算可以得到的最大利益 
        但在Best Time to Buy and Sell Stock III 我們就解過泛化任意k的版本了 

        注意加入k的買賣股票問題 , dp的定義是 : 
        dp[i][k][j] :
        i : 天數 , 即到第i天為止
        k : 最大可交易次數 
        j : 0 or 1 , 代表當下是否持有股票 

        結合起來dp[i][k][j]的語意為 : 在到達第i天 , 並在最大交易次數為k ,且持有/沒有股票的況下目前可得的最大利潤
        我們的答案在 dp[prices.length-1][k-1][0] 

*/


/**
 * @param {number} k
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(k, prices) {
    
    let dp = Array.from(
        new Array(prices.length) , (v) => Array.from(
            new Array(k+1) , (v)=> new Array(2).fill(0) 
        )
    ); 
        
    // 設置base case : 
    // 在第0天的有或沒有股票的情況 
    for (let K = 0 ; K < k+1 ; K++){
        dp[0][K][0] = 0 ; 
        dp[0][K][1] = -prices[0] ;
    }
    // 在沒有辦法做任何交易的情況 , 不管哪天的最大利潤都是0 
    // 這邊特殊case是沒有交易的情況不應該持有股票 , 但初始化為0不影響
    for (let i = 0 ; i < prices.length ; i++){
        dp[i][0][0] = 0 ; 
        dp[i][0][1] = 0 ;  
    }


    for (let i=1 ; i < prices.length ; i++){

        for (let K=1 ; K < k+1 ; K++){
            
            // 沒有股票
            dp[i][K][0] = Math.max( dp[i-1][K][0] , prices[i] + dp[i-1][K][1]  ) ; 

            // 有股票
            dp[i][K][1] = Math.max( dp[i-1][K][1] , dp[i-1][K-1][0] - prices[i] ) ;

        }

    }

    return dp[prices.length - 1 ][k][0] ; 

};