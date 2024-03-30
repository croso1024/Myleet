/**
 * @param {number[]} prices
 * @return {number}
 */


// DP-solution , dp[i] = ( max profit with shock in day i , max profit without stock in day i )

var maxProfit = function(prices) {

    const dp = Array.from( new Array(prices.length) , (i) => new Array(2) ) ;  
    dp[0] = [-prices[0] , 0]
    let solution = 0 ; 
    for (let i = 1 ; i < prices.length ; i++){
        dp[i][0] = Math.max( 
            dp[i-1][1] - prices[i] , dp[i-1][0]
        )
        
        dp[i][1] = Math.max(
            dp[i-1][0] + prices[i] , dp[i-1][1] 
        )
        solution = Math.max(solution , dp[i][1])
    }
    
    return solution ;
};


var maxProfit = function(prices) {

    let prevStock = -prices[0]
    let prevNon = 0 
    let solution = 0 ; 

    for (let i = 1 ; i < prices.length ; i++){

        let curStock = Math.max( prevNon - prices[i] , prevStock )
        let curNon = Math.max( prevNon , prevStock + prices[i] )

        solution = Math.max(solution ,curNon) 

        prevStock = curStock ; 
        prevNon = curNon ;
    }
    
    return solution ;
};
maxProfit([7,1,5,3,6,4])