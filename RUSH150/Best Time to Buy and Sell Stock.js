/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {

    const prefix = new Array(prices.length) ;
    prefix[0] = prices[0] 
    for (let i = 1 ; i < prices.length ; i++){
        prefix[i] = Math.min( prefix[i-1] , prices[i] )  
    }
    
    let solution = 0 ; 
    for (let i = 0 ; i < prices.length ; i++){
        
        solution = Math.max( solution , prices[i] - prefix[i] )
    }
    return solution ;    
};


var maxProfit = function(prices) {

    let minPrices = Number.MAX_VALUE ; 
    let solution = 0 ; 

    for (let i = 0 ; i < prices.length ; i++){
        minPrices = Math.min(minPrices , prices[i]) ; 
        solution = Math.max(  solution , prices[i] - minPrices )

    }
    return solution ;    
};